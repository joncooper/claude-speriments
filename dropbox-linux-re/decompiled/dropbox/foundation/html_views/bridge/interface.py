# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABC
from collections import deque
from typing import Any, Deque, Dict, Text, Tuple, Union
from mypy_extensions import TypedDict
from dropbox.foundation.raii2._shared_impl import SuperDestroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.threading import Lock

class ViewBridgeRecord(ABC):
    pass

ViewBridgeSerializable = Union[(Dict[(Text, Any)], Text, int, ViewBridgeRecord)]
ObservablePropUpdate = TypedDict('ObservablePropUpdate', {
    'key': Text,
    'value': Any })

class _InternalObservableBridgeClassMixinBase(SuperDestroyable):
    pass
# WARNING: Decompyle incomplete

