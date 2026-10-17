# Source Generated with Decompyle++
# File: bolt_client_for_app.pyc (Python 3.11)

from typing import List, Text, Tuple
from dropbox.client.bolt import BoltChannelId, BoltChannelState
from dropbox.client.bolt.types import BoltAppID, BoltRevisionInfo, BoltToken, BoltUniqueID
from dropbox.client.features.bolt.bolt_client_wrapper import AppSignal, BoltClientWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.signals import StandardSignal

def channel_data_for_identifiers(access_token = None, app_id = None, revision_id = None, unique_id = ('access_token', 'Text', 'app_id', 'BoltAppID', 'revision_id', 'int', 'unique_id', 'Text', 'return', 'Tuple[BoltChannelId, BoltChannelState]')):
    bolt_token = BoltToken(access_token)
    revision_info = BoltRevisionInfo(revision_id, bolt_token)
    unique_id = BoltUniqueID(unique_id)
    channel_id = BoltChannelId(app_id, unique_id)
    channel_state = BoltChannelState(channel_id, revision_info)
    return (channel_id, channel_state)


class BoltClientForApp(Actor):
    pass
# WARNING: Decompyle incomplete

