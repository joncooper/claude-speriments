# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Optional, Text, Union
from dropbox.components.desktop_components import DesktopComponent

class BadAssumptionError(Exception):
    pass


class BootError(Exception):
    pass


class RareEvent(Exception):
    pass


class UnexpectedNoneError(BadAssumptionError):
    pass


class FoundationPanicError(Exception):
    pass


class NucleusPanicException(Exception):
    pass


class FsApiPanicException(Exception):
    pass


class ComponentError(Exception):
    pass
# WARNING: Decompyle incomplete


class JavascriptError(ComponentError):
    pass
# WARNING: Decompyle incomplete


class PythonBridgeError(JavascriptError):
    pass
# WARNING: Decompyle incomplete


class SuppressedExceptionMixin:
    pass

