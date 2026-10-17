# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, Tuple
import dropbox.api.v2.datatypes.auth as dropbox
from dropbox.client_api.exceptions import HTTP401Error, HTTP403Error, HTTP409Error

class APIv2AuthError(HTTP401Error):
    pass
# WARNING: Decompyle incomplete


class APIv2AccessError(HTTP403Error):
    pass
# WARNING: Decompyle incomplete


class APIv2EndpointError(HTTP409Error):
    pass
# WARNING: Decompyle incomplete

