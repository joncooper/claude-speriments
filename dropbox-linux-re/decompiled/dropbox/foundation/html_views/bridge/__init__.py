# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, NewType, Text
from mypy_extensions import TypedDict
BRIDGE_EXCEPTION_UNCAUGHT = 10501
BridgeInstanceId = NewType('BridgeInstanceId', Text)
BridgeInstanceToken = TypedDict('BridgeInstanceToken', {
    'instance_id': BridgeInstanceId,
    'type': Text,
    'properties': Dict[(Text, Any)] })
BridgeRecordToken = TypedDict('BridgeRecordToken', {
    '__data__': Any,
    '__type__': Text })
