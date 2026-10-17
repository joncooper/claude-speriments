# Source Generated with Decompyle++
# File: connection_backoff.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import math
import random as insecure_random
import time
from typing import Callable, Optional, TypeVar, Union
from dropbox.trace import TRACE
_T = TypeVar('_T')

def get_jittered_seconds(hours = None):
    return insecure_random.randint(int(hours * 60 * 60 * 3 // 4), int(hours * 60 * 60 * 5 // 4))


class ConnectionBackoff(object):
    
    def __init__(self = None, max_delay_in_seconds = None):
        self.number_of_retries = 0
        self.max_delay_in_seconds = max_delay_in_seconds
        self.slot_time = min(0.1, self.max_delay_in_seconds)
        self.max_exponent = int(math.log(self.max_delay_in_seconds / self.slot_time) / math.log(2))
        self.keep_going = True

    
    def should_keep_going(self = None):
        return self.keep_going

    
    def success(self = None):
        self.keep_going = False
        self.number_of_retries = 0

    
    def fail(self = None, sleep_fn = None):
        self.number_of_retries = self.number_of_retries + 1
        exponent = min(int(self.number_of_retries * math.sqrt(self.number_of_retries)), self.max_exponent)
        delay = insecure_random.randrange(2 ** exponent) * self.slot_time
        TRACE('Request attempt %d failed. Sleeping for %ss for exponential backoff.', self.number_of_retries, delay)
    # WARNING: Decompyle incomplete


