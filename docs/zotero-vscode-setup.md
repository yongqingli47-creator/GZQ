
# VS Code And Zotero Setup

This repository uses Zotero official API access through `pyzotero` and bibliography auto-export through Better BibTeX.

## 1. Get Zotero User ID And API Key

1. Sign in at `https://www.zotero.org/`.
2. Open `https://www.zotero.org/settings/keys`.
3. Copy the numeric User ID shown on that page.
4. Create a new private key for this workflow.
5. Grant library read permission.
6. Keep write permission disabled unless you explicitly need it later.

Put the values into the local environment file:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
ZOTERO_LIBRARY_TYPE=user
ZOTERO_USER_ID=21200666
ZOTERO_API_KEY=yyBILMHuMd1nWjelZRnk8hiB
ZOTERO_COLLECTION_KEY=
```

## 2. Configure Better BibTeX Auto-Export

1. Install Better BibTeX in Zotero.
2. Open Zotero Preferences and confirm the Better BibTeX pane is available.
3. In Zotero, right-click `My Library` or a target collection.
4. Choose `Export Library...` or `Export Collection...`.
5. Select `Better BibTeX` as the format.
6. Enable `Keep Updated`.
7. Save the export into this repository:

```text
literature/bib/library.bib
```

If you want collection-level exports, keep them in the same folder, for example:

```text
literature/bib/innovation-review.bib
literature/bib/board-governance.bib
```

## 3. Prepare The VS Code Python Environment

Create and activate the local environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The repository already includes:

- `.vscode/settings.json` for interpreter and `.env` wiring
- `.vscode/tasks.json` for one-click dependency install and metadata sync
- `.vscode/extensions.json` for recommended extensions

## 4. Sync Zotero Metadata And Abstracts

Run the sync script from VS Code terminal:

```bash
python scripts/zotero_sync.py
```

Optional examples:

```bash
python scripts/zotero_sync.py --limit 50
python scripts/zotero_sync.py --collection-key ABCD1234
python scripts/zotero_sync.py --include-children
```

Generated outputs:

- `literature/metadata/zotero_items.json`
- `literature/metadata/zotero_items.md`

## 5. Recommended Working Loop

1. Add or tag papers in Zotero.
2. Let Better BibTeX update `literature/bib/library.bib`.
3. Rerun `python scripts/zotero_sync.py`.
4. Use repository prompt files and skills for literature organization, review drafting, and outline generation.

## 6. VS Code Tasks

Open Command Palette, run `Tasks: Run Task`, then choose one of:

- `Python: install research dependencies`
- `Zotero: sync metadata snapshot`
