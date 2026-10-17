# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import json
GLOBAL_ACCOUNT_ID = ''
from functools import partial, wraps
from typing import Any, Callable, cast, Optional, Type, TypeVar, Union
from google.protobuf.json_format import MessageToJson, Parse
from google.protobuf.message import Message
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.html_views.electron.ipc import JSONDict, JSONish
TRequest = TypeVar('TRequest', bound = Message)
TResponse = TypeVar('TResponse', bound = Message)

def deserialize_protobuf_request(request_data = None, message_class = None):
    message = message_class()
    if isinstance(request_data, dict):
        request_json = json.dumps(request_data)
    elif isinstance(request_data, str):
        request_json = request_data
    else:
        raise ValueError(f'''Expected str or dict, got {type(request_data)}''')
    return Parse(request_json, message)


def serialize_protobuf_response(message = None):
    return MessageToJson(message, preserving_proto_field_name = False)


def named_partial(func = None, name = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def wrap_typed_handler(typed_method = None, request_class = None, response_class = None):
    pass
# WARNING: Decompyle incomplete

