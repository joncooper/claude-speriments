# Source Generated with Decompyle++
# File: network_response.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, NamedTuple, Optional, Text
from dropbox.sharing.constants.error_tuple import ErrorTuple
NetworkResponse = NamedTuple('NetworkResponse', [
    ('error', Optional[ErrorTuple]),
    ('data', Optional[Dict[(Text, Any)]]),
    ('endpoint', Optional[Text]),
    ('http_code', Optional[Text]),
    ('timeout', Optional[bool])])
NetworkResponse.__new__.__defaults__ = (None,) * len(NetworkResponse._fields)
