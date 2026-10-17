# Source Generated with Decompyle++
# File: watcher.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Text
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.connectivity_watch.watch_interface import ConnectivityState
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.foundation.signals import StandardSignal
from dropbox.functions import make_unicode
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.trace import TRACE

class OfflineWatcher(Singleton):
    pass
# WARNING: Decompyle incomplete

