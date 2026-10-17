# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import Dict, List, Text
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.scheme_handler.types import CustomSchemeHandlerResult, CustomSchemeUrlRequest
CUSTOM_SCHEME_HANDLER_AMP_NAMESPACE = 'desktop_custom_scheme_handler'

class CustomSchemeHandlerInterface(Destroyable):
    process_request = (lambda self = None, path = None, args = abstractmethod, request = ('path', 'Text', 'args', 'Dict[Text, List[Text]]', 'request', 'CustomSchemeUrlRequest', 'return', 'Future[CustomSchemeHandlerResult]'): pass)()


class CustomSchemeRouterInterface(Destroyable):
    scheme_name = (lambda self = None: pass)()()
    domain = (lambda self = None: pass)()()
    add_handler = (lambda self = None, prefix = None, handler = abstractmethod: pass)()
    process_request = (lambda self = None, request = None: pass)()

