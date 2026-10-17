# Source Generated with Decompyle++
# File: monotonic_time_win32.pyc (Python 3.11)

from pynt.dlls.kernel32 import kernel32

def get_monotonic_time():
    return kernel32.GetTickCount64()


def get_monotonic_frequency():
    return 1000

