import glob,collections,os
# group __init__.pyc by body length, same hdr8 constant
G=collections.defaultdict(list)
for f in glob.glob('dropbox-dl/py/**/__init__.pyc',recursive=True):
    d=open(f,'rb').read()
    G[(len(d),d[8:16])].append((f,d))
# pick the biggest group
k=max(G,key=lambda k:len(G[k]))
items=G[k]; (ln,hdr8)=k
print(f"group: bodylen={ln-16} hdr8={hdr8.hex()} count={len(items)}")
a=items[0][1][16:]; b=items[1][1][16:]; c=items[2][1][16:]
x_ab=bytes(p^q for p,q in zip(a,b))
x_ac=bytes(p^q for p,q in zip(a,c))
print("fileA:",os.path.relpath(items[0][0],'dropbox-dl/py'))
print("fileB:",os.path.relpath(items[1][0],'dropbox-dl/py'))
print("A^B zero-bytes: %d/%d" % (x_ab.count(0), len(x_ab)))
print("A^C zero-bytes: %d/%d" % (x_ac.count(0), len(x_ac)))
print("A^B hex:", x_ab.hex())
print("A    hex:", a.hex())
print("B    hex:", b.hex())
