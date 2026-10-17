# Source Generated with Decompyle++
# File: request_status.pyc (Python 3.11)

import random as insecure_random
from typing import Any, Dict, Optional, Text
from six import iteritems
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report
from dropbox.threading import Lock
MYPY = False
if MYPY:
    from dropbox.sync_engine_adapter.adapter import SyncEngineReportInterface
REPORT_PERCENT_URL: 'Dict[Text, int]' = {
    'subscribe': 0,
    'exception': 0,
    'send_trace': 0,
    'report_formatted_trace': 0,
    'report_events': 1,
    'client/hourly_refresh': 1 }

class RequestStatusReporter:
    
    def __init__(self = None):
        self._sync_engine_adapter = None
        self.report_percentages_account_map = { }
        self.report_percentages_lock = Lock()

    
    def on_sync_engine_ready(self = None, sync_engine_adapter = None, account = None):
        self._sync_engine_adapter = sync_engine_adapter

    
    def report_client_timing(self = None, timing_report = None, account = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def report_failed_request(self = None, url = None, data = None, account = ('url', 'Text', 'data', 'Dict[str, Any]', 'account', 'AccountInterface', 'return', 'None')):
        if not self._random_sample_request_log_by_url(url, account):
            return None
    # WARNING: Decompyle incomplete

    
    def _random_sample_request_log_by_url(self = None, url = None, account = None):
        key = url.split('?')[0]
        if account not in self.report_percentages_account_map:
            self.report_percentages_lock
            self.report_percentages_account_map[account] = {
                'percent_url': { },
                'percent': 100 }
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        timing_report_percent_url = self.report_percentages_account_map[account]['percent_url']
        timing_report_percent = self.report_percentages_account_map[account]['percent']
        percent = min(timing_report_percent_url.get(key, 100), REPORT_PERCENT_URL.get(key, 100), timing_report_percent)
        if percent == 0:
            return False
        if None < 100:
            return insecure_random.randrange(10000) < percent * 100

    
    def report_percentage_values_updated(self = None, timing_report_percent = None, timing_report_percent_url = None, account = ('timing_report_percent', 'int', 'timing_report_percent_url', 'Dict[Text, Any]', 'account', 'AccountInterface', 'return', 'None')):
        self.report_percentages_lock
        self.report_percentages_account_map[account] = {
            'percent_url': timing_report_percent_url,
            'percent': timing_report_percent }
        None(None, None)
        return None
        with None:
            if not None:
                pass


