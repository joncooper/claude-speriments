# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, List, NamedTuple, NewType, Text
import six
from mypy_extensions import TypedDict
BoltAppID = NewType('BoltAppID', Text)
BoltUniqueID = NewType('BoltUniqueID', Text)
BoltToken = NewType('BoltToken', Text)
BoltChannelId = NamedTuple('BoltChannelId', [
    ('app_id', BoltAppID),
    ('unique_id', BoltUniqueID)])
BoltRevisionInfo = NamedTuple('BoltRevisionInfo', [
    ('revision', int),
    ('token', BoltToken)])
BoltChannelState = NamedTuple('BoltChannelState', [
    ('channel_id', BoltChannelId),
    ('revision_info', BoltRevisionInfo)])
BoltPayload = NamedTuple('BoltPayload', [
    ('revision', int),
    ('payload', Any)])
BoltChannelPayloads = NamedTuple('BoltChannelPayloads', [
    ('channel_state', BoltChannelState),
    ('payloads', List[BoltPayload])])
BoltEncodedChannelId = TypedDict('BoltEncodedChannelId', {
    'app_id': BoltAppID,
    'unique_id': BoltUniqueID })
BoltEncodedChannelState = TypedDict('BoltEncodedChannelState', {
    'channel_id': BoltEncodedChannelId,
    'revision': Text,
    'token': BoltToken })

def encode_channel_id(channel_id = None):
    return {
        'app_id': channel_id.app_id,
        'unique_id': channel_id.unique_id }


def decode_channel_id(channel_id = None):
    return BoltChannelId(app_id = channel_id['app_id'], unique_id = channel_id['unique_id'])


def encode_channel_state(channel_id = None, revision_info = None):
    return {
        'channel_id': encode_channel_id(channel_id),
        'revision': str(revision_info.revision),
        'token': revision_info.token }


def decode_channel_state(channel_state = None):
    channel_id = decode_channel_id(channel_state['channel_id'])
    revision_info = BoltRevisionInfo(revision = int(channel_state['revision']), token = channel_state['token'])
    return BoltChannelState(channel_id = channel_id, revision_info = revision_info)


def validate_channel_id(channel_id = None):
    _app_type = BoltAppID.__supertype__
    _uid_type = BoltUniqueID.__supertype__
# WARNING: Decompyle incomplete


def validate_revision_info(revision_info = None):
    pass
# WARNING: Decompyle incomplete


def validate_channel_state(channel_state = None):
    pass
# WARNING: Decompyle incomplete

