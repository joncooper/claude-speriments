# Source Generated with Decompyle++
# File: assertions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import threading
from contextlib import contextmanager
from typing import Iterator
_DATA = threading.local()

def require_dropbox_ssl_policy():
    return getattr(_DATA, '_require_dropbox_ssl_policy', True)

allow_non_dropbox_ssl_policy = (lambda : pass# WARNING: Decompyle incomplete
)()
