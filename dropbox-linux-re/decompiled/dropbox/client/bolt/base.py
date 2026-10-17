# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import random as insecure_random
import threading
from abc import abstractmethod
from collections import defaultdict
from enum import Enum
from typing import Any, Callable, Dict, Generic, Iterable, List, Mapping, Optional, TypeVar
from six import iteritems
from dropbox.callbacks import HandlerDict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelPayloads, BoltChannelState, BoltEncodedChannelState, BoltRevisionInfo, decode_channel_id, encode_channel_state, validate_channel_id, validate_channel_state
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import ClientInitiatedDisconnect, ClientInitiatedReconnect, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import CancelledFutureException, Future
from dropbox.threading import Condition
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE, WARNING

class BoltThreadState(Enum):
    WAITING = 0
    ACTIVE = 1
    NOTIFYING = 2

_BoltDataType = TypeVar('_BoltDataType', BoltChannelPayloads, BoltChannelState)

def ProcessedResponse():
    '''ProcessedResponse'''
    __slots__ = ('data', 'invalid_channels')
    
    def __init__(self = None, data = None, invalid_channels = None):
        self.data = list(data)
        self.invalid_channels = list(invalid_channels)

    
    def has_items(self = None):
