#!/usr/bin/env python3
# Operates on already-extracted *text* strings dumps (not executable). Run with -I.
import re, sys, collections

paths = sys.argv[1:]
rs_paths = collections.Counter()
mod_paths = collections.Counter()
crates = collections.Counter()
for p in paths:
    data = open(p, 'r', errors='replace').read()
    # Rust source file paths like desktop/rust/<...>.rs  or src/.../*.rs
    for m in re.finditer(r'[A-Za-z0-9_./\-]+?\.rs\b', data):
        s = m.group(0)
        if len(s) < 120:
            rs_paths[s] += 1
    # crate::module::path style (2+ segments)
    for m in re.finditer(r'\b[a-z][a-z0-9_]+(?:::[a-z][a-z0-9_]+){1,6}\b', data):
        s = m.group(0)
        mod_paths[s] += 1
        crates[s.split('::')[0]] += 1

def dump(title, counter, n, keyfilter=None):
    print(f"\n===== {title} ({len(counter)} unique) =====")
    items = counter.most_common()
    if keyfilter:
        items = [(k,v) for k,v in items if keyfilter(k)]
    for k,v in items[:n]:
        print(f"{v:5d}  {k}")

# Top-level crates
dump("CRATES (top-level module roots)", crates, 60)
# Rust source dirs (collapse to directory)
dirs = collections.Counter()
for k,v in rs_paths.items():
    d = k.rsplit('/',1)[0] if '/' in k else k
    dirs[d] += v
dump("RUST SOURCE DIRECTORIES", dirs, 120)
