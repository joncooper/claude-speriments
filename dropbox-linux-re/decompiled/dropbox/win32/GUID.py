# Source Generated with Decompyle++
# File: GUID.pyc (Python 3.11)

from __future__ import absolute_import
import binascii
import hashlib
from build_number import frozen_version
DROPBOX_VERSION = frozen_version.short
_DROPBOX_NAMESPACE_GUID = 'C01EFC11BCF5EC5B8B4D2B1AA099A076'

def generate_name_based_guid(name = None):
    mymd5 = hashlib.md5()
    namespace = binascii.a2b_hex(_DROPBOX_NAMESPACE_GUID)
    mymd5.update(namespace + name.encode('utf-8'))
    md5_hash = mymd5.digest()
    version = md5_hash[6]
    version = 48 | version & 15
    clock_seq_hi_and_reserved = md5_hash[8]
    clock_seq_hi_and_reserved = 128 | clock_seq_hi_and_reserved & 63
    return '%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x' % (md5_hash[0], md5_hash[1], md5_hash[2], md5_hash[3], md5_hash[4], md5_hash[5], version, md5_hash[7], clock_seq_hi_and_reserved, md5_hash[9], md5_hash[10], md5_hash[11], md5_hash[12], md5_hash[13], md5_hash[14], md5_hash[15])

