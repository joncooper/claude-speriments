# Source Generated with Decompyle++
# File: platform.pyc (Python 3.11)

from __future__ import absolute_import
import sys
from build_number.platform import IS_LINUX, IS_MAC, IS_WINDOWS

class UnsupportedPlatformError(Exception):
    pass

if IS_WINDOWS:
    platform = 'win'
    return None
if None:
    platform = 'mac'
    return None
if None:
    platform = 'linux'
    return None
raise UnsupportedPlatformError('Unsupported Platform %r' % sys.platform)
