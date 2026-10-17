# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum
from typing import Optional, Text, Union
SS_AUTOEVICT_POLICY_NAME = 'ss-autoevict-policy'
SS_AUTOEVICT_ADMIN_POLICY_NAME = 'ss-autoevict-admin-policy'

class SSAutoevictPolicy(Enum):
    OFF = 0
    ON = 100
    from_local_config = (lambda value = None: pass# WARNING: Decompyle incomplete
)()
    to_readable_str = (lambda cls = None, enum_value = None: pass# WARNING: Decompyle incomplete
)()

SS_AUTOEVICT_ON_VARIANTS = [
    SSAutoevictPolicy.ON]
SS_AUTOEVICT_MIN_STORAGE_THRESHOLD = 10 * pow(10, 9)
SS_AUTOEVICT_MIN_STORAGE_RATIO = 0
