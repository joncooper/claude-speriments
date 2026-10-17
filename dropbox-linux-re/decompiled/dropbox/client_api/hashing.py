# Source Generated with Decompyle++
# File: hashing.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
from binascii import b2a_base64
from hashlib import sha256
from typing import Any, Callable, List, Optional, Sequence, Text, Union
MYPY = False
if MYPY:
    from hashlib import _Hash as Hash
DROPBOX_HASH_LENGTH = 43
DROPBOX_MAX_BLOCK_SIZE = 4194304
_to_websafe = bytes.maketrans(b'+/', b'-_')
_from_websafe = bytes.maketrans(b'-_~', b'+/=')

def digest_to_base64(digest = None):
    return b2a_base64(digest)[:-2].translate(_to_websafe)


def base64_to_digest(b64_digest = None):
    return base64.decodebytes(b64_digest.translate(_from_websafe) + b'=')


def is_valid_blocklist(blocklist = None):
    
    try:
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(split_blocklist(blocklist)())
    except (TypeError, AttributeError):
        return False



class DropboxHasher(object):
    __slots__ = ('d', 'total')
    
    def __init__(self = None):
        self.d = sha256()
        self.total = 0

    
    def update(self = None, data = None):
        self.d.update(data)

    
    def digest(self = None):
        pass
    # WARNING: Decompyle incomplete



class BetterDropboxHasher(object):
    
    def __init__(self = None, block_handler = None):
        self.hashes = []
        self.cur_hash_left = 0
        self.block_handler = block_handler
        self.data = []

    
    def _handle_block_handler(self = None):
        if self.block_handler or self.hashes:
            last_block_sha1 = digest_to_base64(self.hashes[-1].digest())
            block_data = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.data())
            self.block_handler(last_block_sha1, block_data)
            return None
        return None

    
    def update(self = None, buf = None):
        offset = 0
        size = len(buf)
        if not buf:
            self._handle_block_handler()
    # WARNING: Decompyle incomplete

    
    def blocklist(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.hashes())



def dropbox_hash(contents = None):
    h = DropboxHasher()
    h.update(contents)
    return h.digest()


def split_blocklist(s = None):
    if not s:
        return ()
    if isinstance(s, Text):
        s = s.encode('ascii')
    return tuple(s.split(b','))


def make_blocklist(digest_arr = None):
    return b','.join(digest_arr)


def get_block_size(hash_ = None, blocklist = None, file_size = None):
    if not blocklist.endswith(hash_):
        return DROPBOX_MAX_BLOCK_SIZE
    return (None - 1) % DROPBOX_MAX_BLOCK_SIZE + 1

