# Source Generated with Decompyle++
# File: notification_state.pyc (Python 3.11)

import re
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, cast, Dict, FrozenSet, Iterable, List, Optional, Set, Tuple, TypedDict
from dropbox.threading import Lock
BB_NOTIFICATION_THRESHOLDS: 'Tuple[int, int, int]' = (80, 90, 100)
BB_MODAL_TYPES: 'Tuple[str, str, str]' = ('monthly', 'team_storage', 'combo')
BB_MODAL_COOLDOWN = timedelta(hours = 24)
_RFC3339_UTC_RE = re.compile('^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|\\+00:00)$')

def BBMonthlyUploadNotificationState():
    '''BBMonthlyUploadNotificationState'''
    handled_thresholds: 'List[int]' = 'BBMonthlyUploadNotificationState'

BBMonthlyUploadNotificationState = <NODE:27>(BBMonthlyUploadNotificationState, 'BBMonthlyUploadNotificationState', TypedDict, total = False)

def BBTeamStorageNotificationState():
    '''BBTeamStorageNotificationState'''
    handled_thresholds: 'List[int]' = 'BBTeamStorageNotificationState'

BBTeamStorageNotificationState = <NODE:27>(BBTeamStorageNotificationState, 'BBTeamStorageNotificationState', TypedDict, total = False)

def BBModalCooldownState():
    '''BBModalCooldownState'''
    combo: 'datetime' = 'BBModalCooldownState'

BBModalCooldownState = <NODE:27>(BBModalCooldownState, 'BBModalCooldownState', TypedDict, total = False)

class BBLimitNotificationVariant(Enum):
    MONTHLY_UPLOAD = 'monthly'
    TEAM_STORAGE = 'team_storage'
    COMBINED = 'combo'

BBNotificationInFlightKey = <NODE:12>()

def _is_int(value = None):
