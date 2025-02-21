#!/bin/sh
set -xe

arch=$1
os=$2
channel=$3

dbfile="$arch-$os-$channel.db"

nix-eval-jobs --workers 4 --max-memory-size 3000 --flake "./nixpkgs#\"$channel\".legacyPackages.$arch-$os" 2>/dev/null | pv --line-mode --size 125000 | ./mkdb.py "$dbfile"
zstd -T0 -19 "$dbfile"
