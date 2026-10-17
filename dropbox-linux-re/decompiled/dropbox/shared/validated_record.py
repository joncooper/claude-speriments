# Source Generated with Decompyle++
# File: validated_record.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import inspect
import itertools
from abc import ABCMeta
from enum import IntEnum, StrEnum
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Tuple, Type, TypeVar, Union
from six import integer_types, iteritems
from dropbox.fastdetails import FastDetails
T = TypeVar('T')

class Field(object):
    __slots__ = ('field_type', 'is_optional', 'default')
    
    def __init__(self = None, field_type = None, is_optional = None, default = (False, None)):
        self.field_type = None
        if field_type in integer_types:
            self.field_type = integer_types
        elif field_type is float:
            self.field_type = (float,) + integer_types
        else:
            self.field_type = field_type
        if isinstance(self.field_type, type) and issubclass(self.field_type, Mapping) and inspect.isabstract(getattr(self.field_type, '__origin__', self.field_type)):
            raise TypeError(f'''Mapping class {self.field_type!r} is a non-coercable abstract type.''')
        self.is_optional = is_optional
        self.default = default

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def check_value(self = None, field_name = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    
    def coerce(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    required = (lambda cls = None, field_type = None: Field(field_type))()
    optional = (lambda cls = None, field_type = None, default = classmethod: Field(field_type, is_optional = True, default = default))()

BaseString = bytes

class ValidatedRecordMetaclass(ABCMeta):
    pass
# WARNING: Decompyle incomplete

_SelfT = TypeVar('_SelfT', bound = 'ValidatedRecord', covariant = True)

def ValidatedRecord():
    '''ValidatedRecord'''
    pass
# WARNING: Decompyle incomplete

ValidatedRecord = <NODE:27>(ValidatedRecord, 'ValidatedRecord', Iterable[Tuple[(str, Any)]], metaclass = ValidatedRecordMetaclass)
