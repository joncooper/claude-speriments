# Source Generated with Decompyle++
# File: local_time_getter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
from datetime import datetime
from dropbox.platform import IS_MAC, IS_WINDOWS

class SYSTEMTIME(ctypes.Structure):
    _fields_ = [
        ('wYear', ctypes.c_int16),
        ('wMonth', ctypes.c_int16),
        ('wDayOfWeek', ctypes.c_int16),
        ('wDay', ctypes.c_int16),
        ('wHour', ctypes.c_int16),
        ('wMinute', ctypes.c_int16),
        ('wSecond', ctypes.c_int16),
        ('wMilliseconds', ctypes.c_int16)]


class LocalTimeGetter:
    get_local_time = (lambda : if IS_WINDOWS:
system_time = SYSTEMTIME()lp_system_time = ctypes.pointer(system_time)ctypes.windll.kernel32.GetLocalTime(lp_system_time)datetime(year = system_time.wYear, month = system_time.wMonth, day = system_time.wDay, hour = system_time.wHour, minute = system_time.wMinute, second = system_time.wSecond)if None:
tzlocal = tzlocalimport dateutil.tzdatetime.now(tzlocal())datetime.now())()

