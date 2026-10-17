# Source Generated with Decompyle++
# File: apollo_alerts.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, NamedTuple, Optional, Sequence, Text
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.threading import Lock
from dropbox.trace import TRACE
AlertResult = NamedTuple('AlertResult', [
    ('button_index', Optional[int]),
    ('checkbox_checked', Optional[bool])])

class ApolloAlerts(Singleton):
    pass
# WARNING: Decompyle incomplete

