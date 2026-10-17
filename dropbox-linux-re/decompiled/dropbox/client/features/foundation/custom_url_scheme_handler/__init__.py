# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod, abstractproperty
from typing import Text
from six.moves.urllib.parse import ParseResult
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import StandardSignal

class CustomURLSchemeHandler(Destroyable):
    
    def listen_to(self = None, signal = None):
        self._autodestroy(signal.listen(self._handle_url, 'CustomURLSchemeHandler'))

    scheme = (lambda self = None: pass)()
    _handle_url = (lambda self = None, url = None: pass)()

