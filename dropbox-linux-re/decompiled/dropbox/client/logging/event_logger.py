# Source Generated with Decompyle++
# File: event_logger.pyc (Python 3.11)

import json
import os
import random as insecure_random
import threading
from io import BytesIO
from time import time as _time
from typing import Any, Callable, Dict, List, Optional, Text
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.reporting.debug import should_trace_event_pipeline
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes, make_unicode
from dropbox.legacy_crypto.dropboxy import encrypt_blob, generate_session_key, PUBLIC_KEY_TUPLE
from dropbox.threading import Lock
from dropbox.trace import TRACE

class AggregateEvent:
    
    def __init__(self = None, data = None, ts = None, timeout = (None,), metadata = ('data', 'Dict[Text, int]', 'ts', 'float', 'timeout', 'float', 'metadata', 'Optional[Dict[str, JSONable]]', 'return', 'None')):
        self.min_ts = ts
        self.max_ts = ts
        self.data = data.copy()
        self.timeout_ts = timeout + _time()
    # WARNING: Decompyle incomplete

    
    def update(self = None, data = None, ts = None, metadata = (None,)):
        self.min_ts = min(self.min_ts, ts)
        self.max_ts = max(self.max_ts, ts)
    # WARNING: Decompyle incomplete

    
    def is_ready_to_log(self = None):
        return _time() > self.timeout_ts



class EventLogger:
    pass
# WARNING: Decompyle incomplete


def _get_writable_chunk_log_path(log_dir = None, prefix = None, trace_start = None):
    log_prefix = 1
    fn = os.path.join(log_dir, '%s%d-%04x-%08x' % (prefix, log_prefix, insecure_random.getrandbits(16), trace_start))
    if not os.path.isfile(fn):
        pass
    else:
        log_prefix += 1
    return fn

