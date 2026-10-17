# Source Generated with Decompyle++
# File: _interface.pyc (Python 3.11)

from abc import abstractmethod, abstractproperty
from enum import auto, Enum
from typing import Any, Callable, Dict, List, Optional, Text, Tuple, Union
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal
JSONDict = Dict[(Text, Any)]
JSONish = Union[(Text, int, float, bool, None, List[Any], Tuple[(Any, Any)], JSONDict)]

class ElectronIpcConnectionState(Enum):
    NOT_CONNECTED = auto()
    CONNECTED = auto()
    DISCONNECTED = auto()


class ElectronIpc(Destroyable):
    server_address = (lambda self = None: pass)()
    send_message = (lambda self = None, topic = None, payload = abstractmethod, default_serializer = (None,): pass)()
    add_message_handler = (lambda self = None, topic = None, callback = abstractmethod: pass)()
    clear_message_handlers = (lambda self = None, topic = None: pass)()
    connection_state = (lambda self = None: pass)()
    on_connection_state_changed = (lambda self = None: pass)()

