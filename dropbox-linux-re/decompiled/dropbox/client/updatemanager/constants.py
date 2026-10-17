# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Text, TypeVar
RESTART_WAIT_TIME_SECONDS = 900
StrOrText = TypeVar('StrOrText', str, Text)

class RestartFailureError(Exception):
    pass


class PermissionError(Exception):
    pass

IN_APP_UPDATE_CONFIG_KEY = 'last_update'
UPDATEMANAGER_CONFIG_KEY = 'last_updatemanager'
DESKTOP_RELEASE_AMP_NAMESPACE = 'desktop_release'

class PromoteFromHelperResult(Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    NO_HELPER = 'no_helper'
    TIMEOUT = 'timeout'

