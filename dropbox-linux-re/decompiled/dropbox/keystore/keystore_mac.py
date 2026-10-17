# Source Generated with Decompyle++
# File: keystore_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import os
from errno import ENOENT
from typing import Any, Optional, Text, Tuple, Union
from uuid import UUID
import build_number
from pymac.helpers.disk import get_volume_uuid
from pymac.helpers.security import KeychainItem
from keystore_posix import KeyStoreFileBacked
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fileutils import safe_remove
from dropbox.trace import TRACE

def noop(*n, **kw):
    pass


class KeyStoreMac(KeyStoreFileBacked):
    pass
# WARNING: Decompyle incomplete

