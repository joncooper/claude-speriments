# Source Generated with Decompyle++
# File: abstract_placeholder.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import NamedTuple, Text
from dropbox.shared.placeholder_details import PlaceholderDetails
SimpleStat = NamedTuple('SimpleStat', [
    ('volumeid', int),
    ('inode', int),
    ('mtime', int),
    ('size', int)])

class AbstractPlaceholder(object):
    read = (lambda self = None: pass)()
    prepare_for_write = (lambda self = None, size = None: pass)()
    write = (lambda self = None, data = None, offset = abstractmethod: pass)()
    read_data = (lambda self = None, offset = None, length = abstractmethod: pass)()
    unset = (lambda self = None: pass)()
    reset = (lambda self = None, size = None: pass)()
    is_placeholder = (lambda self = None: pass)()
    file_system_id = (lambda self = None: pass)()
    resolve_path = (lambda self = None: pass)()
    set_file_mtime = (lambda self = None, mtime = None: pass)()
    simple_stat = (lambda self = None: pass)()
    
    def is_owned_by(self = None, uid = None):
        return False


