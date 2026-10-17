# Source Generated with Decompyle++
# File: product_span.pyc (Python 3.11)

from enum import Enum
from typing import Optional, Text
from uuid import UUID, uuid4
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import RLock

class ProductSpanState(Enum):
    IDLE = 'IDLE'
    ACTIVE = 'ACTIVE'
    EXPIRING = 'EXPIRING'


class ProductSpan:
    pass
# WARNING: Decompyle incomplete

