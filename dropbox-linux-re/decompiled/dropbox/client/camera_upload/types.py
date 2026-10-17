# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import NamedTuple, NewType, Optional
from dropbox.client.multiaccount.constants import Role
CameraSplashResponse = NamedTuple('CameraSplashResponse', [
    ('import_video', Optional[bool]),
    ('role', Optional[Role])])
CUDeviceUID = NewType('CUDeviceUID', str)

class CameraImportAction(Enum):
    SPLASH = 0
    IMPORT = 1
    DISABLE = 2

