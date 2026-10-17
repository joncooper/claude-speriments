# Source Generated with Decompyle++
# File: monitored_thread_pool_metrics.pyc (Python 3.11)

import random as insecure_random
from time import monotonic
from typing import Any, Callable, Dict, Optional, Text, TypeVar
from apex.metrics import Metric, MetricsReporter
from build_number import dropbox_version
from build_number.channel import BuildChannel
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.ui.common.hang_reporter import HangReporter
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.metrics.function_usage import CachedThunk
from dropbox.platform import IS_LINUX
from dropbox.threadutils import SafeValue
_T = TypeVar('_T')
AMP_NAMESPACE = 'amp_namespace'
METRIC_NAME_PREFIX = 'metric_name_prefix'
METRIC_QUEUE_LENGTH = '/queue_length'
METRIC_EXECUTION_TIME = '/execution_time'
METRIC_QUEUE_TIME = '/queue_time'
METRIC_TOTAL_TIME = '/total_time'
METRIC_HANG = '/hang'
THREAD_HANG_REPORTER = 'thread_hang_reporter'
HANG_TIMEOUT_SECONDS = 30
PERIODIC_THREAD_HANG_CHECK_MINUTES = 1
OPT_IN_RATE = {
    BuildChannel.stable: 0.0001,
    BuildChannel.beta: 0.005,
    BuildChannel.internal_alpha: 1 }.get(dropbox_version.channel, 0.0001)
SAMPLE_RATE = 0.1

class SampledThreadPoolMetrics:
    
    def __init__(self = None, amp_metrics_reporter = None, logging_data = None, tags = (None,), kill_switch = ('amp_metrics_reporter', 'MetricsReporter', 'logging_data', 'Dict[Text, Text]', 'tags', 'Optional[Dict[Text, Text]]', 'kill_switch', 'Optional[Callable[[], bool]]')):
