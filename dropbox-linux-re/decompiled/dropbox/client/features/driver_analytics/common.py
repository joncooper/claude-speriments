# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from dropbox.foundation.futures.thread import GlobalPool
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from win import record_loaded_dlls_win
run_driver_analytics = (lambda : if IS_WINDOWS:
record_loaded_dlls_win()None)()
