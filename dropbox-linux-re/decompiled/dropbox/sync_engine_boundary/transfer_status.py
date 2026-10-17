# Source Generated with Decompyle++
# File: transfer_status.pyc (Python 3.11)

from __future__ import absolute_import, division
import functools
from enum import Enum
from typing import List, Optional
from dropbox.shared.validated_record import Field, ValidatedRecord

class ProgressBottleneck(Enum):
    OPS_RATE = 1
    BYTES_RATE = 2


class TransferStatusSnapshot(ValidatedRecord):
    pass
# WARNING: Decompyle incomplete

