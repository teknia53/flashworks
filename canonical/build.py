#!/usr/bin/env python3
"""Regenerate every FlashWorks data copy from canonical/vocab.json.

canonical/vocab.json is the single source of truth for the BBG vocabulary
(mirroring Bill's desktop-app master database). This script pushes it to:
  1. FlashWorksWeb.sqlite            (this repo's queryable copy)
  2. index.html + site/index.html    (embedded array for the web app)
  3. ../FlashWorksApp/assets/databases/FlashWorks.sqlite  (iPhone app;
     ships with the next app build — its `codes` table is left untouched)

After editing vocab.json (or re-exporting from the desktop master):
    python3 canonical/build.py
then deploy the web app:
    npx wrangler pages deploy site --project-name flashworks
and commit both repos.
"""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLS = ["dbSequence", "dbChapter", "dbGK", "dbDifficulty", "dbFrequency", "dbType",
        "dbSetDiffWordAuto", "dbCounter", "dbWord", "dbSayWordFile", "dbMeaning",
        "dbPrincipalParts"]

rows = json.load(open(ROOT / "canonical" / "vocab.json"))
assert rows == sorted(rows, key=lambda r: r["dbSequence"]), "vocab.json must be in dbSequence order"
assert len({r["dbSequence"] for r in rows}) == len(rows), "duplicate dbSequence values"

# 1 + 3: the two sqlite copies
for db in (ROOT / "FlashWorksWeb.sqlite",
           ROOT.parent / "FlashWorksApp" / "assets" / "databases" / "FlashWorks.sqlite"):
    con = sqlite3.connect(db)
    con.execute("DELETE FROM flash")
    con.executemany(
        f"INSERT INTO flash ({','.join(COLS)}) VALUES ({','.join('?' * len(COLS))})",
        [tuple(r[c] for c in COLS) for r in rows])
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM flash").fetchone()[0]
    con.close()
    print(f"{db}: {n} rows")

# 2: embedded arrays in the web app HTML
embedded = json.dumps(
    [{"s": r["dbSequence"], "c": r["dbChapter"], "g": r["dbGK"], "f": r["dbFrequency"],
      "t": r["dbType"] or "", "w": r["dbWord"] or "", "m": r["dbMeaning"] or "",
      "p": r["dbPrincipalParts"] or ""} for r in rows],
    ensure_ascii=False, separators=(",", ":"))
for path in (ROOT / "index.html", ROOT / "site" / "index.html"):
    html = path.read_text()
    start = html.find('[{"s":1,')
    end = html.find("}]", start)
    assert start > 0 and end > 0, f"embedded array not found in {path}"
    path.write_text(html[:start] + embedded + html[end + 2:])
    print(f"{path}: embedded array updated")
