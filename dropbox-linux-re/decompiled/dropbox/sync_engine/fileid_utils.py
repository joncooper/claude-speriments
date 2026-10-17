# Source Generated with Decompyle++
# File: fileid_utils.pyc (Python 3.11)

from __future__ import absolute_import
import base64
import zlib
from typing import Tuple
from google.protobuf.message import DecodeError
from dropbox.proto.on_disk.checksummed_buffer_pb2 import ChecksummedBuffer
from dropbox.proto.on_disk.fileid_pb2 import FileIdAndRev
from dropbox.sync_engine_boundary.file_system_constants import PERSISTED_FILEID_PRESERVED_NAME

class CorruptPersistedFileId(Exception):
    pass


class PersistedFileIdDecodeError(Exception):
    pass


def crc32(buf = None):
    return zlib.crc32(buf) & 0xFFFFFFFF


def deserialize_fileid_and_rev(serialized_bytes = None):
    persisted_fileid = ChecksummedBuffer()
    
    try:
        persisted_fileid.ParseFromString(serialized_bytes)
    except DecodeError:
        raise CorruptPersistedFileId()

    if persisted_fileid.crc32 != crc32(persisted_fileid.buffer):
        raise CorruptPersistedFileId()
    fileid_and_rev = FileIdAndRev()
    
    try:
        fileid_and_rev.ParseFromString(persisted_fileid.buffer)
    except DecodeError:
        raise PersistedFileIdDecodeError()

    return (base64.urlsafe_b64encode(fileid_and_rev.fileid).rstrip(b'='), fileid_and_rev.revision)


def serialize_fileid_and_rev(fileid = None, rev = None):
    persisted_fileid = ChecksummedBuffer()
    fileid_and_rev = FileIdAndRev()
    fileid_bytes = base64.urlsafe_b64decode(fileid + b'==')
    fileid_and_rev.fileid = fileid_bytes
    fileid_and_rev.revision = rev
    persisted_fileid.buffer = fileid_and_rev.SerializeToString()
    persisted_fileid.crc32 = crc32(persisted_fileid.buffer)
    return persisted_fileid.SerializeToString()

