# Source Generated with Decompyle++
# File: dbxlog_logger.pyc (Python 3.11)

import os
from typing import Any, Callable, Dict, List
from apex.context import DebugLoggingConfig, DiskLoggingConfig, LoggingConfig
from apex.dbxlog import Level, Logger
from dropbox.client.util import safe_to_str
from dropbox.trace import TraceSegment

class DbxLogger:
    name = 'dbxlog'
    
    def __init__(self = None, inner = None):
        self.inner = inner

    
    def get_stats(self = None):
        return self.inner.stats()

    
    def log(self = None, ts = None, seg = None):
        self.inner.log(Level.CRITICAL if seg.emphasis else Level.INFO, seg.threadname.strip(), seg.filename, seg.lineno, seg.segment.decode('utf-8'), {
            'host_int': str(seg.host_int) } if seg.host_int else { })

    
    def add_redacted_value(self = None, redacted_value = None, placeholder = None):
