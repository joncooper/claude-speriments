# Source Generated with Decompyle++
# File: analytics.pyc (Python 3.11)

import dataclasses
from typing import Optional
from apex._apex import ffi, lib
from apex.lifecycle import raise_if_shutdown
from google.protobuf.message import Message
AccountInformation = <NODE:12>()

class AnalyticsClient:
    __init__ = (lambda self = None, ctx = None: self.context = ctx)()
    log_event = (lambda self = None, event = None, account_info = raise_if_shutdown, session_id = (None, None): raw_event = event.SerializeToString()c_event_name = ffi.new('char[]', event.DESCRIPTOR.name.encode('utf-8'))c_event_bytes = ffi.new('char[]', raw_event)if account_info:
c_account_info = ffi.new('AccountInformation *', dataclasses.asdict(account_info))else:
c_account_info = ffi.NULLif session_id:
c_session_id = ffi.new('char[]', session_id.encode('utf-8'))else:
c_session_id = ffi.NULLlib.analytics_client_log_event(self.context, c_event_name, c_event_bytes, len(raw_event), c_account_info, c_session_id))()

