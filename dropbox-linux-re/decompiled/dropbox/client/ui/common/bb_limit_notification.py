# Source Generated with Decompyle++
# File: bb_limit_notification.pyc (Python 3.11)

from dataclasses import dataclass
from typing import cast, Dict, FrozenSet, Iterable, Mapping, Optional, Text, Tuple
from typing_extensions import TypeGuard
from dropbox.client.notifications.constants import BB_TEAM_STORAGE_CAMPAIGN_IDS
THRESHOLDS: 'Tuple[int, int, int]' = (80, 90, 100)
TEAM_STORAGE_THRESHOLD = 100
_BYTES_PER_MEGABYTE = 1048576
BBLimitNotificationDecision = <NODE:12>()

def _is_int(value = None):
