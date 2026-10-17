# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import re
from typing import Any, Callable, Dict, Optional, Text, TYPE_CHECKING, TypeVar
from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.internal import enum_type_wrapper
from google.protobuf.message import Message
from dropbox.proto.pap.event_state_pb2 import EventState
if TYPE_CHECKING:
    EnumValue = TypeVar('EnumValue', bound = int)
    EnumType = enum_type_wrapper._EnumTypeWrapper[EnumValue]
else:
    EnumValue = TypeVar('EnumValue')
    EnumType = TypeVar('EnumType')

def to_snake_case(camel_case = None):
    parts = re.findall('[A-Z][A-Z]+(?=[A-Z_]|$)|[A-Z][^A-Z_]*|[^A-Z_]+', camel_case)
    return (lambda .0: [ a.lower() for a in .0 ])(parts())


def is_predefined_event(event = None):
    return event.DESCRIPTOR.full_name.startswith('pap.events')


def has_event_class(event = None):
    return hasattr(event, 'event_class')


def get_enum_value_for_string(enum = None, key = None):
    pass
# WARNING: Decompyle incomplete


class EventFieldParser:
    
    def __init__(self = None, event = None):
        self._event = event
        self._values = event.ListFields()()
        self._all_fields = event.DESCRIPTOR.fields()

    
    def get_field(self = None, name = None):
        return self._all_fields.get(name, None)

    
    def get_typed_value(self = None, name = None, field_type = None, expected_type = ('name', 'Text', 'field_type', 'int', 'expected_type', 'type', 'return', 'Optional[Any]')):
        field = self.get_field(name)
        if field or field.type != field_type:
            return None
        value = None._values.get(name, None)
    # WARNING: Decompyle incomplete

    
    def get_default_value(self = None, name = None):
        field = self.get_field(name)
        return field.default_value if field else None

    
    def _get_enum_value_string(self = None, field = None, int_value = None):
        
        try:
            return field.enum_type.values_by_number[int_value].name.lower()
        except Exception:
            return None


    
    def get_enum_value(self = None, name = None):
        field = self.get_field(name)
        if not field:
            return None
        int_value = None.get_typed_value(name, FieldDescriptor.TYPE_ENUM, int)
    # WARNING: Decompyle incomplete

    
    def action_surface(self = None):
        return self.get_typed_value('action_surface', FieldDescriptor.TYPE_STRING, str)

    
    def event_class(self = None):
        value = self.get_enum_value('event_class')
    # WARNING: Decompyle incomplete

    
    def event_state(self = None):
        value = self._values.get('event_state', None)
    # WARNING: Decompyle incomplete

    
    def event_state_string(self = None):
        value = self._values.get('event_state', None)
    # WARNING: Decompyle incomplete

    
    def event_properties(self = None):
        properties = { }
    # WARNING: Decompyle incomplete


