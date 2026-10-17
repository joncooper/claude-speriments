# Source Generated with Decompyle++
# File: logging_event.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict, Optional
from uuid import uuid4
from google.protobuf.message import Message
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.components.desktop_components import DesktopComponent
from dropbox.pap_event_logging.utils import EventFieldParser, to_snake_case
from dropbox.proto.pap.event_state_pb2 import EventState as PAPEventState
USER_EVENTS_AMP_NAMESPACE = 'desktop_consolidated_user'
UDCL_EVENTS_AMP_NAMESPACE = 'udcl'
ENG_EVENTS_AMP_NAMESPACE = 'desktop_consolidated_eng'

def to_pap_event_state(event_state = None):
    return PAPEventState.Value(event_state.name)


class _GenericLoggingEvent(ABC):
    is_time_to_resolution_event: 'bool' = '_GenericLoggingEvent'
    
    def __eq__(self, other):
