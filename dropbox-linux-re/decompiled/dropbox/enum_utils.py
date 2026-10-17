# Source Generated with Decompyle++
# File: enum_utils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import enum
import json
from typing import Any, Callable, List, Optional
MYPY = False
auto = enum.auto

class AutoNameEnum(enum.Enum):
    _generate_next_value_ = (lambda name = None, start = None, count = staticmethod, last_values = ('name', 'str', 'start', 'int', 'count', 'int', 'last_values', 'List[Any]', 'return', 'Any'): name)()


class AutoLowerNameEnum(enum.Enum):
    _generate_next_value_ = (lambda name = None, start = None, count = staticmethod, last_values = ('name', 'str', 'start', 'int', 'count', 'int', 'last_values', 'List[Any]', 'return', 'Any'): name.lower())()


class StrAsPrefixlessValueTrait(_MixinBase):
    
    def __str__(self = None):
        return self.value


_default_encoder: 'Optional[Callable[[json.JSONEncoder, Any], Any]]' = None

def _enum_aware_encoder(self = None, o = None if MYPY else None):
    if isinstance(o, AutoNameJsonEnum):
        return o._value_
# WARNING: Decompyle incomplete


def _register_json_encoder():
    global _default_encoder
    if not _default_encoder:
        _default_encoder = json.JSONEncoder.default
        json.JSONEncoder.default = _enum_aware_encoder
        return None


class AutoNameJsonEnum(AutoNameEnum):
    _register_json_encoder()

