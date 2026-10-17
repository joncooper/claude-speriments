# Source Generated with Decompyle++
# File: monotonic_time_mac.pyc (Python 3.11)

from __future__ import absolute_import, division
import time
from macffi.System import sysctl

def _get_boot_time():
    timeval = sysctl('kern.boottime')
    return timeval.tv_sec + float(timeval.tv_usec) / 1e+06


def get_monotonic_time():
    return time.time() - _get_boot_time()


def get_monotonic_frequency():
    return 1

