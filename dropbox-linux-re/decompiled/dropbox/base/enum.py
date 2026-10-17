# Source Generated with Decompyle++
# File: enum.pyc (Python 3.11)

from __future__ import absolute_import
from enum import Enum, IntEnum

class StrEnum(Enum, str):
    
    def __str__(self = None):
        return self.value



class OldStyleIntEnum(IntEnum):
    
    def __str__(self = None):
        return f'''{type(self).__name__}.{self.name}'''


