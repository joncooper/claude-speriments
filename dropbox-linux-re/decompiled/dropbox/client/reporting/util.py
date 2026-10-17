# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import collections
from typing import Any, Collection, Dict, Optional, Text
from apex.metrics import Counter, Metric, MetricsReporter
from build_number import BUILDID, get_build_channel, is_store_managed
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.util import get_user_agent_dict
from dropbox.client_typing import JSONable
from dropbox.functions import python_version_string
from dropbox.trace import TRACE

class AvroTypeError(TypeError):
    pass


def report_amp_metrics(metrics_reporter = None, events = None, results = None):
    pass
# WARNING: Decompyle incomplete


def get_reporting_metadata(buildno = None, client_session_id = None, channel_id = None):
    return {
        'buildno': buildno,
        'buildid': BUILDID,
        'build_channel': get_build_channel(),
        'channel_id': channel_id,
        'platform_version': get_user_agent_dict().get('version'),
        'machine_id': str(UNSAFE_get_raw_machine_uuid()),
        'client_session_id': client_session_id,
        'python_version': python_version_string(),
        'is_store_managed': is_store_managed() }

