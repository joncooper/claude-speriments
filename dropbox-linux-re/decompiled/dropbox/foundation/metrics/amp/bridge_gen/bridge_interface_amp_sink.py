# Source Generated with Decompyle++
# File: bridge_interface_amp_sink.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import List
from dropbox.foundation.futures import Future
from dropbox.foundation.metrics.amp.bridge_gen.amp_span import AmpSpan

class AmpSinkBridgeInterface(ABC):
    report = (lambda self = None, data = None: pass)()

