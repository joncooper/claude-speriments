# Source Generated with Decompyle++
# File: file_system.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from mac_finder_comment_attr_wrapper import mac_finder_comment_file_system
from posix_attrs_wrapper import executable_attribute_file_system
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
MYPY = False
if MYPY:
    from abstract_file_system import AbstractFileSystem as BaseFileSystem
elif IS_WINDOWS:
    from windows import FileSystem as BaseFileSystem
elif IS_MAC:
    from macosx import MacOSXFileSystem as BaseFileSystem
elif IS_LINUX:
    from linux import FileSystem as BaseFileSystem

def FileSystem():
    return mac_finder_comment_file_system(executable_attribute_file_system(BaseFileSystem()))

# WARNING: Decompyle incomplete
