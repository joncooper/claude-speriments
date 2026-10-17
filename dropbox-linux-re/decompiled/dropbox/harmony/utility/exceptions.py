# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Optional
SEVERITY_BENIGN = 'benign'
SEVERITY_CRITICAL = 'critical'

class StateNotAvailableError(Exception):
    pass
# WARNING: Decompyle incomplete


class ConnectionRequestError(Exception):
    pass
# WARNING: Decompyle incomplete


class ConnectionStateError(Exception):
    pass


class MoveToDropboxError(Exception):
    pass


class PluginMoveError(Exception):
    pass


class PluginRemoveFailedError(PluginMoveError):
    pass

