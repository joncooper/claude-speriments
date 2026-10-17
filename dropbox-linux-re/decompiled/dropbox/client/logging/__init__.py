# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os.path as os
from typing import Any, Callable, Dict, List, Optional, Text
from typing_extensions import Protocol
from dropbox.trace import TraceSegment

def _is_temporary_log_path(path = None):
    basename = os.path.basename(path)
    return basename[0] == '~'


def _ts_from_log_path(path = None):
    return int(path[-8:], 16)

