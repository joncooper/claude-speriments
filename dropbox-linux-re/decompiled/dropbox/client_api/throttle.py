# Source Generated with Decompyle++
# File: throttle.pyc (Python 3.11)

from __future__ import absolute_import, division
from typing import Optional
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.trace import TRACE

class ThrottlePrefs(object):
    THROTTLE_AUTOMATIC = 'THROTTLE_AUTOMATIC'
    THROTTLE_MANUAL = 'THROTTLE_MANUAL'
    THROTTLE_NONE = 'THROTTLE_NONE'
    __slots__ = [
        'ul_throttle_type',
        'dl_throttle_type',
        'ul_speed',
        'dl_speed']
    
    def __eq__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''ul: {self.ul_throttle_type!s}({self.ul_speed!s}) dl: {self.dl_throttle_type!s}({self.dl_speed!s})'''

    
    def __init__(self = None, ul_throttle_type = None, dl_throttle_type = None, ul_speed = (None, None, None, None), dl_speed = ('ul_throttle_type', 'Optional[str]', 'dl_throttle_type', 'Optional[str]', 'ul_speed', 'Optional[float]', 'dl_speed', 'Optional[float]', 'return', 'None')):
