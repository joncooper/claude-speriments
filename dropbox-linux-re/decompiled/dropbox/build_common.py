# Source Generated with Decompyle++
# File: build_common.pyc (Python 3.11)

from __future__ import absolute_import, print_function
from build_number import dropbox_version
PYTHON_DROPBOX_BUILD = 20
DROPBOX_SQLITE_VERSION = '3.32.3'

def get_platform():
    return dropbox_version.platform


def get_build_number():
    return str(dropbox_version)

