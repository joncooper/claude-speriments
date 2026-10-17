import sys,glob,collections,os
files=[f for f in glob.glob('py/**/__init__.pyc',recursive=True)]
bylen=collections.defaultdict(list)
for f in files:
    d=open(f,'rb').read(); bylen[len(d)].append((f,d))
# find the most common small size (likely empty __init__)
for ln,items in sorted(bylen.items())[:6]:
    if len(items)<2: continue
    print(f"\n--- {len(items)} files of length {ln} ---")
    for f,d in items[:4]:
        print(f"  hdr8={d[8:16].hex()} body16={d[16:32].hex()} {os.path.relpath(f,'py')}")
    # do any two share identical body?
    bodies=collections.Counter(d[16:] for f,d in items)
    print(f"  distinct bodies among {len(items)}: {len(bodies)}")
