# Source Generated with Decompyle++
# File: chillout_tracker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import random as insecure_random
from typing import Dict, Optional, Text
from six.moves.urllib import parse as urlparse
from dropbox.client_api.connection_util import ENDPOINT_IMPORTANCE, sleep_using_stoppable_if_possible
from dropbox.exception.reporting import report_assertion_error, report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.sleep import _SleepScheduler
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.trace import TRACE
DEFAULT_CHILLOUT_JITTER = 0.25

class ChilloutTracker(object):
    
    def __init__(self = None, conn_name = None):
        self.conn_name = conn_name
        self._chillouts = { }

    _parse_and_validate_url_path = (lambda url_post_domain = None: parsed_url = urlparse.urlparse(url_post_domain)# WARNING: Decompyle incomplete
)()
    
    def update_chillout(self = None, url_post_domain = None, time_to_chillout = None):
        url_path = self._parse_and_validate_url_path(url_post_domain)
        cur_chillout = self._chillouts.get(url_path, 0)
        new_chillout = get_monotonic_time_seconds() + time_to_chillout
        self._chillouts[url_path] = max(cur_chillout, new_chillout)
        if time_to_chillout != 0:
            TRACE('%s requested backoff of %.2f sec on endpoint %s', self.conn_name, float(time_to_chillout), url_path)
            return None

    
    def wait_for_chillout_async(self = None, url_post_domain = None):
        url_path = self._parse_and_validate_url_path(url_post_domain)
        if url_path not in self._chillouts:
            return ResolvedFuture(None)
        tosleep = None._chillouts[url_path] - get_monotonic_time_seconds()
        if tosleep > 1800 and url_path in ENDPOINT_IMPORTANCE['important_methods']:
            report_bad_assumption(f'''Server is asking us to sleep more than thirty minutes on an important method: {tosleep!r}''')
        if tosleep > 0:
            if _SleepScheduler._is_shutting_down:
                TRACE('%s Skipping chillout sleep during shutdown for path (%s)', self.conn_name, url_path)
                return ResolvedFuture(None)
            TRACE('%s Sleeping (chillout) for %.2f sec as requested by path (%s)', self.conn_name, tosleep, url_path)
            return sleep_async(tosleep)
        return ResolvedFuture(None)

    
    def wait_for_chillout(self = None, url_post_domain = None):
        url_path = self._parse_and_validate_url_path(url_post_domain)
        if url_path not in self._chillouts:
            return None
        tosleep = None._chillouts[url_path] - get_monotonic_time_seconds()
        total_sleep = tosleep
    # WARNING: Decompyle incomplete

    
    def handle_chillout_headers(self = None, base_str = None, jitter_str = None, url_post_domain = ('base_str', 'Optional[str]', 'jitter_str', 'Optional[str]', 'url_post_domain', 'Text', 'return', 'None')):
        base = None
        jitter = None
    # WARNING: Decompyle incomplete


