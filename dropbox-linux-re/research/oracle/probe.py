import os,sys
os.write(2, b"DRIVER-START\n")
os.write(2, ("ver=%s\n"%sys.version).encode())
os.write(2, ("path=%r\n"%(sys.path,)).encode())
