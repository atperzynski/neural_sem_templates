#!/usr/bin/env python3
# Proprietary. All rights reserved. Licence to be determined by the inventors.
"""Refuse a commit or a push that would put data into the repository.

A HOT-NUX-SEM project keeps its model, its data dictionary, its cleaning recipe and its scripts in
Git, and keeps the data on the computers of the people who analyse it. The rule of the project is
that no row of data is ever committed to GitHub, GitLab or any other repository, and this script is
run in three places so that a mistake is caught early, namely i) as the pre-commit hook in
`.githooks/`, ii) in the GitHub workflow, and iii) in the GitLab pipeline.

A file is refused when it is i) anything inside `data/` other than `data/README.md` and
`data/.gitkeep`, ii) a file whose extension is a data format (Stata, SPSS, SAS, Excel, Parquet,
Feather, R data, Mplus data and the like) anywhere in the repository, or iii) a delimited text file
(`.csv`, `.tsv`, `.txt` with many delimited lines) outside `results/`, where the tables of
estimates and fit are kept. A file larger than five megabytes is also refused, because a model,
a dictionary or a script is never that large.

    python tools/check_no_data.py            check the files Git tracks or is about to commit
    python tools/check_no_data.py --staged   check only the files staged for the next commit
    python tools/check_no_data.py PATH ...   check the named files

The script uses the Python standard library only and runs on Python 3.8 or later.
"""
from __future__ import annotations

import os
import subprocess
import sys

DATA_EXTENSIONS = {
    ".sav", ".zsav", ".por", ".dta", ".sas7bdat", ".sas7bcat", ".xpt", ".xls", ".xlsx", ".xlsm",
    ".ods", ".parquet", ".feather", ".arrow", ".rds", ".rda", ".rdata", ".dat", ".h5", ".hdf5",
    ".sqlite", ".db", ".mdb", ".accdb", ".json.gz", ".csv.gz", ".zip", ".gz", ".7z",
}
DELIMITED = {".csv", ".tsv", ".tab", ".psv"}
ALLOWED_IN_DATA = {"data/README.md", "data/.gitkeep"}
MAX_BYTES = 5 * 1024 * 1024


def tracked(staged: bool) -> list[str]:
    """the files Git would hold after the next commit, or only the staged ones"""
    if staged:
        cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    else:
        cmd = ["git", "ls-files", "--cached", "--others", "--exclude-standard"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
        return [line.strip() for line in out.splitlines() if line.strip()]
    except (OSError, subprocess.CalledProcessError):
        # a pipeline image without Git, or a checkout Git will not read, is checked file by file
        found = []
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d != ".git"]
            found += [os.path.relpath(os.path.join(root, f), ".").replace(os.sep, "/") for f in files]
        return found


def looks_delimited(path: str) -> bool:
    """a .txt file with twenty or more lines that each carry the same comma or tab count"""
    try:
        with open(path, encoding="utf8", errors="replace") as fh:
            lines = [fh.readline() for _ in range(40)]
    except OSError:
        return False
    lines = [ln for ln in lines if ln.strip()]
    if len(lines) < 20:
        return False
    for sep in (",", "\t", ";"):
        counts = {ln.count(sep) for ln in lines}
        if len(counts) == 1 and next(iter(counts)) >= 2:
            return True
    return False


def reason(path: str) -> str | None:
    """why a file may not be committed, or None when it may"""
    p = path.replace(os.sep, "/")
    low = p.lower()
    if p.startswith("data/") and p not in ALLOWED_IN_DATA:
        return "it is inside data/, which stays on your computer"
    for ext in sorted(DATA_EXTENSIONS, key=len, reverse=True):
        if low.endswith(ext):
            return f"{ext} is a data format"
    ext = os.path.splitext(low)[1]
    if ext in DELIMITED and not p.startswith("results/"):
        return f"{ext} files hold rows of data, and only the tables in results/ may be committed"
    if ext == ".txt" and not p.startswith("results/") and looks_delimited(path):
        return "the file reads as delimited rows of data"
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return "it is larger than 5 MB, and a model, a dictionary or a script is never that large"
    except OSError:
        pass
    return None


def main(argv: list[str]) -> int:
    staged = "--staged" in argv
    paths = [a for a in argv if not a.startswith("--")] or tracked(staged)
    bad = [(p, r) for p in paths if (r := reason(p))]
    if not bad:
        print(f"No data found in {len(paths)} files.")
        return 0
    print("These files look like data, and data is never committed to this repository:\n")
    for p, r in bad:
        print(f"  {p}: {r}")
    print("\nKeep the data in data/ on your own computer (Git ignores that folder), or move a table of"
          "\nresults into results/. If a file was staged by mistake, run: git restore --staged <file>")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
