# Source Generated with Decompyle++
# File: desktop_login_wrapper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Optional
from dropbox.client.desktop_login import DesktopLogin
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.threading import Lock
MYPY = False
if MYPY:
    Parent = DesktopLogin
else:
    Parent = object

class DesktopLoginWrapper(Parent, Singleton):
    pass
# WARNING: Decompyle incomplete

