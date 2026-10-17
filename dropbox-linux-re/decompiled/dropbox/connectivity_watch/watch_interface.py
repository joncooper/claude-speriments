# Source Generated with Decompyle++
# File: watch_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from abc import ABCMeta, abstractmethod
from typing import Callable, Dict, NamedTuple, Optional, Text
from six import add_metaclass

def ConnectivityState():
    '''ConnectivityState'''
    UNKNOWN = 'unknown'
    PROXY_INVALID = 'proxy-invalid'
    CONNECTED = 'connected'
    DISCONNECTED = 'disconnected'

ConnectivityState = <NODE:27>(ConnectivityState, 'ConnectivityState', NamedTuple('ConnectivityState', [
    ('state', str),
    ('timestamp', float)]))
ConnectivityWatchInterface = <NODE:12>()
ConnectivityReadAPI = <NODE:12>()
