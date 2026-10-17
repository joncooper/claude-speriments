# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

import contextlib
from abc import abstractmethod
from typing import Callable, Generator, Optional, Text, TypeVar
from bridge_gen.bridge_interface_perf_session import PerfSessionBridgeInterface
from dropbox.foundation.futures import Future
_V = TypeVar('_V')

class PerfSessionInterface(PerfSessionBridgeInterface):
    
    def __init__(self = None):
        self.sub_group_name = None

    span = (lambda self = None, name = contextlib.contextmanager: pass)()()
    async_span = (lambda self = None, name = None, async_callback = abstractmethod: pass)()
    add_extra = (lambda self = None, tag = None, value = abstractmethod: pass)()
    end = (lambda self = None, last_checkpoint_name = None: pass)()

