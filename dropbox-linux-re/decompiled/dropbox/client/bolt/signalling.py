# Source Generated with Decompyle++
# File: signalling.pyc (Python 3.11)

import abc
from typing import Callable, List, Optional, Set, Text
from apex.metrics import Metric, MetricsReporter, Timer
from six import add_metaclass
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.bolt.base import BaseClient, ProcessedResponse
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelState, BoltEncodedChannelState, decode_channel_state
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.foundation.futures.basic import Future
from dropbox.threading import Condition
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

def BoltClient():
    '''BoltClient'''
    pass
# WARNING: Decompyle incomplete

BoltClient = <NODE:27>(BoltClient, 'BoltClient', BaseClient[BoltChannelState])
BoltLongPollHandlerBase = <NODE:12>()

class BoltLongPoller(StoppableThread):
    pass
# WARNING: Decompyle incomplete

