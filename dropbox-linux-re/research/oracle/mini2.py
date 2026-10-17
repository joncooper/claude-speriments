import os,zipfile,marshal
ZIP=os.environ["ORACLE_ZIP"]
body=zipfile.ZipFile(ZIP).read("apex/dbxconn.pyc")[16:]
os.write(2,("MINI len=%d head=%s\n"%(len(body),body[:16].hex())).encode())
c=marshal.loads(body)
os.write(2,("MINI decoded co_name=%s argcount=%d\n"%(c.co_name,c.co_argcount)).encode())
