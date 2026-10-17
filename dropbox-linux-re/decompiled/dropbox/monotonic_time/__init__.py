# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division
import sys
if sys.platform.startswith('darwin'):
    from monotonic_time_mac import get_monotonic_frequency, get_monotonic_time
elif sys.platform.startswith('win32'):
    from monotonic_time_win32 import get_monotonic_frequency, get_monotonic_time
else:
    from monotonic_time_linux import get_monotonic_frequency, get_monotonic_time

def get_monotonic_time_seconds():
    return get_monotonic_time() / get_monotonic_frequency()

