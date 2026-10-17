# Source Generated with Decompyle++
# File: meta_engine_api.pyc (Python 3.11)

import enum
from abc import ABCMeta, abstractmethod
from typing import Callable, Dict, Optional
from build_number.features import feature_enabled
from dropbox.client.fenix.event_hub import EventHub
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BackupType(enum.Enum):
    COMPUTER_BACKUP = 'COMPUTER_BACKUP'
    EXTERNAL_DRIVE_BACKUP = 'EXTERNAL_DRIVE_BACKUP'
    UNKNOWN = 'UNKNOWN'


def MetaEngineBaseClass():
    '''MetaEngineBaseClass'''
    pass
# WARNING: Decompyle incomplete

MetaEngineBaseClass = <NODE:27>(MetaEngineBaseClass, 'MetaEngineBaseClass', Actor, metaclass = ABCMeta)
