# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Text
from apex.metrics import MetricsReporter
from dropbox.connectivity_watch.watch_interface import ConnectivityState, ConnectivityWatchInterface

class ConnectivityWatch(ConnectivityWatchInterface):
    
    def __init__(self = None, metrics_reporter = None):
        pass

    
    def register_callback(self = None, host = None, callback_fn = None):
        pass

    
    def get_connectivity_state(self = None, host = None):
        return ConnectivityState(ConnectivityState.CONNECTED, 1)

    
    def start_watch(self = None):
        pass


