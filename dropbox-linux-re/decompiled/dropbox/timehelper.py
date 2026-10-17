# Source Generated with Decompyle++
# File: timehelper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import time
from datetime import datetime
from typing import Text, Tuple

def tz_offset_minutes(datetime_obj = None):
    timestamp = time.mktime(datetime_obj.timetuple())
    offset = datetime.fromtimestamp(timestamp) - datetime.utcfromtimestamp(timestamp)
    return (offset.days * 24 * 60 * 60 + offset.seconds) // 60


def tz_offset_string(datetime_obj = None):
    offset_minutes = tz_offset_minutes(datetime_obj)
    sign = '-' if offset_minutes < 0 else '+'
    offset_minutes = abs(offset_minutes)
    dummy_time = time.struct_time((1, 0, 0, offset_minutes // 60, offset_minutes % 60, 0, 0, 0, 0))
    return sign + time.strftime('%H%M', dummy_time)


def get_system_time_tuple():
    (utime, stime) = os.times()[:2]
    return (time.time(), utime, stime)

