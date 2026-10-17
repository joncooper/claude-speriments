# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sys
from functools import total_ordering
from typing import Optional, Tuple
from dropbox.platform import IS_LINUX
MYPY = False
LinuxVersion = <NODE:12>()

def _get_version():
    if not MYPY and sys.platform.startswith('linux'):
        info = ''
    else:
        info = os.uname()[2].split('-')[0]
    info = (lambda .0: pass# WARNING: Decompyle incomplete
)(info())
    version_tuple = info.split('.')
    if len(version_tuple) < 3:
        return None
    
    try:
        return LinuxVersion((int(version_tuple[0]), int(version_tuple[1]), int(version_tuple[2])))
    except Exception:
        return None


if IS_LINUX:
    LINUX_VERSION = _get_version()
    return None
