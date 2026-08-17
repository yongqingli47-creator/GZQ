from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify PostgreSQL connectivity for this workspace."
    )
    parser.add_argument(
        "--require-postgis",
        action="store_true",
        help="Fail if PostGIS is not available in the connected database cluster.",
    )
    return parser.parse_args()


def build_connection_kwargs() -> dict[str, Any]:
    dsn = os.getenv("POSTGRES_DSN", "").strip()
    if dsn:
        return {"conninfo": dsn}

    user = os.getenv("PGUSER", "").strip() or os.getenv("USER", "").strip()
    kwargs: dict[str, Any] = {
        "host": os.getenv("PGHOST", "127.0.0.1").strip() or "127.0.0.1",
        "port": int(os.getenv("PGPORT", "5432") or "5432"),
        "dbname": os.getenv("PGDATABASE", "postgres").strip() or "postgres",
        "user": user,
        "connect_timeout": int(os.getenv("PGCONNECT_TIMEOUT", "5") or "5"),
    }

    password = os.getenv("PGPASSWORD", "")
    sslmode = os.getenv("PGSSLMODE", "disable").strip()
    if password:
        kwargs["password"] = password
    if sslmode:
        kwargs["sslmode"] = sslmode
    return kwargs


def fetch_one(cursor: psycopg.Cursor[Any], query: str) -> dict[str, Any]:
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        raise SystemExit(f"Query returned no rows: {query}")
    return dict(row)


def main() -> None:
    load_dotenv(ROOT / ".env")
    args = parse_args()

    conn_kwargs = build_connection_kwargs()
    with psycopg.connect(**conn_kwargs, row_factory=dict_row) as connection:
        with connection.cursor() as cursor:
            identity = fetch_one(
                cursor,
                """
                select
                    current_user as current_user,
                    current_database() as current_database,
                    inet_server_addr()::text as server_addr,
                    inet_server_port() as server_port,
                    version() as server_version
                """,
            )
            postgis_available = fetch_one(
                cursor,
                """
                select
                    default_version,
                    installed_version
                from pg_available_extensions
                where name = 'postgis'
                """,
            )

    print(f"Connected user: {identity['current_user']}")
    print(f"Connected database: {identity['current_database']}")
    print(f"Server address: {identity['server_addr'] or 'local'}:{identity['server_port']}")
    print(f"Server version: {identity['server_version']}")
    print(f"PostGIS available version: {postgis_available['default_version']}")

    installed_version = postgis_available.get("installed_version")
    if installed_version:
        print(f"PostGIS installed in current database: {installed_version}")
    else:
        print("PostGIS is available but not installed in the current database.")

    if args.require_postgis and not postgis_available.get("default_version"):
        raise SystemExit("PostGIS is not available in this PostgreSQL installation.")


if __name__ == "__main__":
    main()