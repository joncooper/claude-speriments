# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from time import sleep as _sleep, time as _time
from typing import Callable, Dict, List, Text
from apex.metrics import Metric, MetricsReporter
from winffi.wininet.api import InternetCheckConnection
from wininternetcheckapi import register_connectivity_change_callback
from dropbox.assertions import assert_
from dropbox.callbacks import Handler
from dropbox.client.device_info import get_machine_uuid
from dropbox.connectivity_watch.watch_interface import ConnectivityState, ConnectivityWatchInterface
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.gui import running_on_thread_named
from dropbox.threading import Condition, Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

class ConnectivityNotifierThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class ConnectivityWatchThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class ConnectivityWatch(ConnectivityWatchInterface):
    
    def __init__(self = None, metrics_reporter = None):
        self._metrics_reporter = metrics_reporter
        self._notify_thread = db_thread(ConnectivityNotifierThread)(self._metrics_reporter)
        self._watch_thread = db_thread(ConnectivityWatchThread)(self._notify_thread)

    
    def start_watch(self = None):
        self._notify_thread.start()
        self._watch_thread.start()

    
    def register_callback(self = None, host = None, callback_fn = None):
        self._notify_thread.register_callback(host, callback_fn)

    
    def get_connectivity_state(self = None, host = None):
        if InternetCheckConnection():
            state = ConnectivityState.CONNECTED
        else:
            state = ConnectivityState.DISCONNECTED
        return ConnectivityState(state, _time())


