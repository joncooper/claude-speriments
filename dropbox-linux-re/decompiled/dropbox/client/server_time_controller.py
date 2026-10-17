# Source Generated with Decompyle++
# File: server_time_controller.pyc (Python 3.11)

from typing import Optional
from dropbox.monotonic_time import get_monotonic_time_seconds

class ServerTimeController:
    
    def __init__(self = None):
        self._server_time = None
        self._monotonic_time = 0

    
    def get_server_time(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_server_time(self = None, server_time = None):
        self._server_time = server_time
        self._monotonic_time = get_monotonic_time_seconds()


