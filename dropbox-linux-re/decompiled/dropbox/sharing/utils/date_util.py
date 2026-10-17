# Source Generated with Decompyle++
# File: date_util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from datetime import datetime
from typing import Text
from dropbox.client_api.dropbox_connection import DROPBOX_TIMESTAMP_FORMAT

def convert_time_last_seen_to_seconds(time_last_seen = None):
    seen_state_datetime = datetime.strptime(time_last_seen, DROPBOX_TIMESTAMP_FORMAT)
    now_datetime = datetime.utcnow()
    secs = (now_datetime - seen_state_datetime).total_seconds()
    return secs

