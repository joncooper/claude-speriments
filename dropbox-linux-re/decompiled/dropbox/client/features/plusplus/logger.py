# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from enum import Enum
from typing import Any, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report, sanitize_event_extra_dict

class EventAction(Enum):
    select = 0


class EventObject(Enum):
    backup_set_up = 4
    vault_set_up = 5
    vault_open = 20
    passwords_set_up = 3


class PlusPlusActionSurface(Enum):
    finder_explorer = 0


def _report_event(account, event_action, event_object = None, action_surface = None, device_type = None, application_name = ('desktop', 'Dropbox', None), application_id = ('account', 'Optional[AccountInterface]', 'event_action', 'EventAction', 'event_object', 'EventObject', 'action_surface', 'PlusPlusActionSurface', 'device_type', 'str', 'application_name', 'Optional[str]', 'application_id', 'Optional[str]', 'extra_dict', 'Any'), **extra_dict):
    extra_dict = sanitize_event_extra_dict(extra_dict)
    event_name = '{}_{}'.format(event_action.name, event_object.name)
    report('sync-everything-plus_plus_events', account = account, event_name = event_name, event_action = event_action.name, event_object = event_object.name, action_surface = action_surface.name, device_type = device_type, application_id = application_id, application_name = application_name, extra = extra_dict)


class PlusPlusLogger:
    report_event_hive = (lambda cls, account, event_action, event_object = None, action_surface = None, device_type = classmethod, application_name = ('desktop', 'Dropbox', None), application_id = ('account', 'AccountInterface', 'event_action', 'EventAction', 'event_object', 'EventObject', 'action_surface', 'PlusPlusActionSurface', 'device_type', 'str', 'application_name', 'Optional[str]', 'application_id', 'Optional[str]', 'extra_dict', 'Any'): pass# WARNING: Decompyle incomplete
)()

