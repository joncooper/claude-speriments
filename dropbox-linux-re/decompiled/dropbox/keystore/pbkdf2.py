# Source Generated with Decompyle++
# File: pbkdf2.pyc (Python 3.11)

from __future__ import absolute_import, division
import hashlib
import hmac
from hmac import HMAC
from struct import pack
from typing import Callable
MYPY = False
if MYPY:
    from hashlib import _Hash as Hash

def pbkdf2(password = None, salt = None, itercount = None, keylen = (hashlib.sha1,), hashfn = ('password', 'bytes', 'salt', 'bytes', 'itercount', 'int', 'keylen', 'int', 'hashfn', 'Callable[..., Hash]', 'return', 'bytes')):
    
    try:
        digest_size = hashfn().digest_size
    except TypeError:
        digest_size = hashfn.digest_size

    l = keylen // digest_size
    if keylen % digest_size != 0:
        l += 1
    h = hmac.new(password, None, hashfn)
    T = b''
    for i in range(1, l + 1):
        T += pbkdf2_F(h, salt, itercount, i)
        return T[0:keylen]


def xorstr(a = None, b = None):
    if len(a) != len(b):
        raise ValueError('xorstr(): lengths differ')
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(a, b)())


def prf(h = None, data = None):
    hm = h.copy()
    hm.update(data)
    return hm.digest()


def pbkdf2_F(h = None, salt = None, itercount = None, blocknum = ('h', 'HMAC', 'salt', 'bytes', 'itercount', 'int', 'blocknum', 'int', 'return', 'bytes')):
    U = prf(h, salt + pack('>i', blocknum))
    T = U
    for i in range(2, itercount + 1):
        U = prf(h, U)
        T = xorstr(T, U)
        return T

