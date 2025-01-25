#!/usr/bin/env python3
import json
import re
import sqlite3
import sys

db = sqlite3.connect(sys.argv[1])
db.executescript("""
pragma user_version = 1;
pragma journal_mode = memory;
create table packages (
    name text primary key,
    error text,
    full_name text,
    hash text
);
""")

for line in sys.stdin:
    pkg = json.loads(line)
    attr = pkg["attr"]

    if "error" in pkg:
        db.execute(
            "insert into packages (name, error) values (?, ?)",
            (attr, pkg["error"]),
        )
        continue

    for output, path in pkg["outputs"].items():
        name = attr
        full = pkg["name"]
        if output != "out":
            name += "." + output
            full += "." + output

        hash = re.search(r"^/nix/store/(\w+)-", path).group(1)

        db.execute(
            "insert into packages (name, full_name, hash) values (?, ?, ?)",
            (name, full, hash),
        )

db.commit()
db.close()
