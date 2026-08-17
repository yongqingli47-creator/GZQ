from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ModuleNotFoundError as exc:
    if exc.name == "dotenv":
        raise SystemExit(
            "Missing dependency 'python-dotenv'. Use ./.venv/bin/python or run the 'Python: install research dependencies' task."
        ) from exc
    raise

try:
    from pyzotero import zotero
except ModuleNotFoundError as exc:
    if exc.name == "pyzotero":
        raise SystemExit(
            "Missing dependency 'pyzotero'. Use ./.venv/bin/python or run the 'Python: install research dependencies' task."
        ) from exc
    raise


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON_PATH = ROOT / "literature" / "metadata" / "zotero_items.json"
DEFAULT_MD_PATH = ROOT / "literature" / "metadata" / "zotero_items.md"
SKIP_ITEM_TYPES = {"attachment", "note", "annotation"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync Zotero metadata and abstracts into repository-local files."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit after fetching the library snapshot.",
    )
    parser.add_argument(
        "--include-children",
        action="store_true",
        help="Include child items instead of only top-level library entries.",
    )
    parser.add_argument(
        "--collection-key",
        default=None,
        help="Optional Zotero collection key to sync instead of the whole library.",
    )
    parser.add_argument(
        "--output-json",
        default=None,
        help="Override JSON output path.",
    )
    parser.add_argument(
        "--output-md",
        default=None,
        help="Override Markdown output path.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate API access without writing output files.",
    )
    return parser.parse_args()


def env_flag(name: str, default: bool) -> bool:
    raw_value = os.getenv(name)
    if raw_value is None:
        return default
    return raw_value.strip().lower() in {"1", "true", "yes", "on"}


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def extract_year(raw_date: str) -> str:
    digits = "".join(character if character.isdigit() else " " for character in raw_date)
    for token in digits.split():
        if len(token) == 4:
            return token
    return ""


def clean_text(value: str) -> str:
    return " ".join(value.split())


def creator_name(creator: dict[str, Any]) -> str:
    if creator.get("name"):
        return str(creator["name"]).strip()

    last_name = str(creator.get("lastName", "")).strip()
    first_name = str(creator.get("firstName", "")).strip()
    if last_name and first_name:
        return f"{last_name}, {first_name}"
    return last_name or first_name


def normalize_item(item: dict[str, Any]) -> dict[str, Any] | None:
    data = item.get("data", {})
    item_type = str(data.get("itemType", "")).strip()
    if item_type in SKIP_ITEM_TYPES:
        return None

    publication = (
        data.get("publicationTitle")
        or data.get("bookTitle")
        or data.get("proceedingsTitle")
        or data.get("university")
        or ""
    )
    creators = [name for name in (creator_name(entry) for entry in data.get("creators", [])) if name]
    tags = [entry.get("tag", "") for entry in data.get("tags", []) if entry.get("tag")]
    abstract = clean_text(str(data.get("abstractNote", "")))

    return {
        "key": data.get("key", ""),
        "itemType": item_type,
        "title": clean_text(str(data.get("title", "Untitled"))),
        "creators": creators,
        "year": extract_year(str(data.get("date", ""))),
        "date": str(data.get("date", "")),
        "publication": clean_text(str(publication)),
        "doi": str(data.get("DOI", "")),
        "url": str(data.get("url", "")),
        "abstract": abstract,
        "collections": data.get("collections", []),
        "tags": tags,
    }


def fetch_items(client: zotero.Zotero, collection_key: str | None, top_level_only: bool) -> list[dict[str, Any]]:
    if collection_key:
        raw_items = client.collection_items(collection_key)
    elif top_level_only:
        raw_items = client.top()
    else:
        raw_items = client.items()

    return list(client.everything(raw_items))


def write_json(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "count": len(items),
        "items": items,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_markdown(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Zotero Library Snapshot",
        "",
        f"Total items: {len(items)}",
        "",
    ]

    for index, item in enumerate(items, start=1):
        creators = "; ".join(item["creators"]) or "Unknown"
        year = item["year"] or "n.d."
        publication = item["publication"] or "No venue"
        lines.extend(
            [
                f"## {index}. {item['title']}",
                "",
                f"- Key: {item['key']}",
                f"- Type: {item['itemType']}",
                f"- Authors: {creators}",
                f"- Year: {year}",
                f"- Publication: {publication}",
                f"- DOI: {item['doi'] or 'N/A'}",
                f"- URL: {item['url'] or 'N/A'}",
                f"- Tags: {', '.join(item['tags']) if item['tags'] else 'None'}",
                f"- Abstract: {item['abstract'] or 'No abstract in Zotero'}",
                "",
            ]
        )

    path.write_text("\n".join(lines), encoding="utf-8")


def resolve_output_path(explicit: str | None, env_name: str, fallback: Path) -> Path:
    configured = explicit or os.getenv(env_name, "").strip()
    if not configured:
        return fallback
    return ROOT / configured


def main() -> None:
    load_dotenv(ROOT / ".env")
    args = parse_args()

    library_id = require_env("ZOTERO_USER_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user").strip() or "user"
    api_key = require_env("ZOTERO_API_KEY")
    top_level_only = not args.include_children and env_flag("ZOTERO_TOP_LEVEL_ONLY", True)
    collection_key = args.collection_key or os.getenv("ZOTERO_COLLECTION_KEY", "").strip() or None
    limit = args.limit or int(os.getenv("ZOTERO_LIMIT", "0") or "0") or None
    output_json = resolve_output_path(args.output_json, "ZOTERO_METADATA_JSON", DEFAULT_JSON_PATH)
    output_md = resolve_output_path(args.output_md, "ZOTERO_METADATA_MD", DEFAULT_MD_PATH)

    client = zotero.Zotero(library_id, library_type, api_key)
    normalized_items = []
    for raw_item in fetch_items(client, collection_key=collection_key, top_level_only=top_level_only):
        normalized = normalize_item(raw_item)
        if normalized is not None:
            normalized_items.append(normalized)

    normalized_items.sort(key=lambda item: ((item["year"] or "0000"), item["title"].lower()), reverse=True)
    if limit is not None:
        normalized_items = normalized_items[:limit]

    if args.dry_run:
        print(f"Verified Zotero access for {len(normalized_items)} items.")
        if normalized_items:
            print(f"First item: {normalized_items[0]['title']}")
        if collection_key:
            print(f"Collection key: {collection_key}")
        return

    write_json(output_json, normalized_items)
    write_markdown(output_md, normalized_items)

    print(f"Wrote {len(normalized_items)} items to {output_json}")
    print(f"Wrote Markdown digest to {output_md}")
    if collection_key:
        print(f"Collection key: {collection_key}")


if __name__ == "__main__":
    main()