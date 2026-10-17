# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from typing import NewType
CsId = NewType('CsId', int)
HostId = NewType('HostId', int)
NsId = NewType('NsId', int)
ShardId = NewType('ShardId', int)
SJId = NewType('SJId', int)
TeamId = NewType('TeamId', int)
UserId = NewType('UserId', int)
FileId = NewType('FileId', str)

def bytes_to_fileid(fileid = None):
    return FileId(fileid.decode('ascii'))


def fileid_to_bytes(fileid = None):
    return fileid.encode('ascii')

