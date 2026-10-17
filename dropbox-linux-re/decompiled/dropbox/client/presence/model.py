# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Dict, NamedTuple
from dropbox.client.bolt.types import BoltToken, BoltUniqueID
from dropbox.harmony.utility.constants import BeaconPlatform
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.shared.util import safe_navigate

class BeaconContextInfo(NamedTuple):
    token: 'BoltToken' = 'BeaconContextInfo'


class RequestType(Enum):
    Update = 0
    Heartbeat = 1
    Clear = 2


class PresenceStatus(object):
    BEACON_OFFLINE = ''
    OFFLINE = 'offline'
    VIEWER = 'viewer'
    MODIFIER = 'modifier'


class BeaconIdentifiers(NamedTuple):
    identifier: 'str' = 'BeaconIdentifiers'


class BeaconSource(NamedTuple):
    identifier: 'str' = 'BeaconSource'


class BeaconAgent(NamedTuple):
    source: 'BeaconSource' = 'BeaconAgent'


class BeaconInfo(NamedTuple):
    rev: 'int' = 'BeaconInfo'

START_TS_KEY = 'start_ts'

class PresenceInfo(NamedTuple):
    platform: 'int' = 'PresenceInfo'
    is_editing = (lambda self = None: self.status == PresenceStatus.MODIFIER)()
    last_edited = (lambda self = None: 