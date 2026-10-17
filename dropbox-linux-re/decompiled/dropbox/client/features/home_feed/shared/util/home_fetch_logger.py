# Source Generated with Decompyle++
# File: home_fetch_logger.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from build_number import dropbox_version
from dropbox.event import report_aggregate_event
from dropbox.foundation.performance import PerfSession
from dropbox.trace import TRACE

class HomeFetchLogger(object):
    
    def __init__(self = None, name = None):
        sampling_rate = 1 if dropbox_version.is_internal_alpha() else 0.05
        self._perf_session = PerfSession('apollo_home_fetch_{}'.format(name).lower(), sampling_rate = sampling_rate)
        self._name = name
        TRACE('%s started', self._get_trace_prefix())

    
    def _checkpoint(self = None, label = None):
        self._perf_session.checkpoint(label)

    
    def _get_trace_prefix(self = None):
        return f'''{self._name!s} FETCH_LOGGER | start_time: {self._perf_session.start_time!r} |'''

    
    def mark_fetch_initiated(self = None):
        self._checkpoint('fetch_start')

    
    def mark_server_fetch_response(self = None, success = None):
        report_aggregate_event('assistant-network-worker-response', {
            str(self._name) + '-successes': 1 } if success else {
            str(self._name) + '-failures': 1 })
        self._checkpoint('fetch_complete')

    
    def mark_response_body_deserialization_complete(self = None):
        self._checkpoint('deserialization_complete')

    
    def mark_done(self = None):
        TRACE('%s ended', self._get_trace_prefix())
        self._perf_session.end()


