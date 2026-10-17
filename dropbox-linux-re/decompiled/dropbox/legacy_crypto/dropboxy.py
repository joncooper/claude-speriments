# Source Generated with Decompyle++
# File: dropboxy.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import hashlib
import os
import zlib
from typing import Tuple
from build_number.legacy_crypto import aes_encrypt, RSACipher
PUBLIC_KEY_TUPLE = (0x9CC73E5870D60035F860E93AB7BFF9928A2480701913EF9D9B88E4E22F08ED6820803173BF44D38D0A2868E1F67082F42D1DDEC6801D766C6F6E59EDD63CB5FB038893655322806E11BC3E8DC1D413B4EB74C7223EF0BB2A73070DC5DBC529313E813BB890C60EE79D077A646E0B35DB10751B1F0AAC0B17529617DCE47E9EC7, 5)
VERSION = 1

def encrypt_blob(header, key = None, version = None, timestamp = None, blob = (True,), compress = ('header', 'bytes', 'key', 'bytes', 'version', 'int', 'timestamp', 'int', 'blob', 'bytes', 'compress', 'bool', 'return', 'bytes')):
    if compress:
        blob = zlib.compress(blob)
    blob += hashlib.md5(blob).digest()
    iv = hashlib.md5(b'%08x' % timestamp).digest()[:16]
    return b'Dropboxy%04d%04d%s%s' % (version, len(header), header, aes_encrypt(key, iv, blob))


def generate_session_key(rsa_tuple = None):
    key = hashlib.md5(os.urandom(32)).digest()
    header = RSACipher().load_key_from_tuple(rsa_tuple).encrypt(key)
    return (header, key)


def encrypt_blob_with_new_session_key(timestamp = None, blob = None, compress = None):
    (header, key) = generate_session_key(PUBLIC_KEY_TUPLE)
    return encrypt_blob(header, key, VERSION, timestamp, blob, compress = compress)

