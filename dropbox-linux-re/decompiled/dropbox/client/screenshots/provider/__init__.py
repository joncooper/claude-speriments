# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Type
from dropbox.client.screenshots.provider._base import ScreenshotsProviderBase
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from _windows import ScreenshotsProvider as _SPWin
    ScreenshotsProvider: 'Type[ScreenshotsProviderBase]' = _SPWin
elif IS_MAC:
    from _mac import ScreenshotsProvider as _SPMac
    ScreenshotsProvider = _SPMac
elif IS_LINUX:
    from _linux import ScreenshotsProvider as _SPLinux
    ScreenshotsProvider = _SPLinux
# WARNING: Decompyle incomplete
