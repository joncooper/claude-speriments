# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import re
from abc import ABC, abstractmethod
from typing import Callable, Dict, Iterator, List, Mapping, Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.lib.stormcrow.constants import STORMCROW_FEATURE_REGEX
from dropbox.trace import TRACE
GandalfFeatureValue = Tuple[(int, int, Optional[str])]
VARIANT_FORCED_ON = 'FORCED_ON'
_DISALLOWED_OFF = set([
    'OFF'])
_DISALLOWED_OFF_AND_CONTROL = set([
    'OFF',
    'CONTROL'])

class Gandalf(ABC):
    is_valid_key = (lambda key = None: re.match(STORMCROW_FEATURE_REGEX, key) is not None)()
    
    def allows(self = None, feature = None, account = None, treat_control_as_off = (None, False)):
