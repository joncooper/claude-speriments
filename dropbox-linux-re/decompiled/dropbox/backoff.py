# Source Generated with Decompyle++
# File: backoff.pyc (Python 3.11)

from typing import Protocol
from dropbox.threading import Lock

class Backoff(Protocol):
    
    def next_delay(self = None):
        pass

    
    def reset(self = None):
        pass



class TruncatedExponentialBackoff:
    
    def __init__(self = None, initial_delay = None, max_delay = None, backoff_multiplier = ('initial_delay', 'float', 'max_delay', 'float', 'backoff_multiplier', 'float', 'return', 'None')):
        self._initial_delay = initial_delay
        self._current_delay = 0
        self._max_delay = max_delay
        self._backoff_multiplier = backoff_multiplier
        self._lock = Lock()

    
    def next_delay(self = None):
        self._lock
        if not self._current_delay:
            self._current_delay = self._initial_delay
        else:
            self._current_delay = min(self._current_delay * self._backoff_multiplier, self._max_delay)
        None(None, None)
        return 
        with None:
            if not None, self._current_delay:
                pass

    
    def reset(self = None):
        self._lock
        self._current_delay = 0
        None(None, None)
        return None
        with None:
            if not None:
                pass


