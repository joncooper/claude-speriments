# Source Generated with Decompyle++
# File: event_publisher.pyc (Python 3.11)

import datetime
from concurrent.futures import Future as CFuture
from typing import Any, Callable, Dict, List, Optional, Text, Union
from google.protobuf.service import RpcController
from tprt import ConnectionReset, TransportCancel, TransportError
from thin_client.base import NucleusThinClient
from common import is_tprt_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread, db_thread_with_task_timing
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.fs_api.fs_api_thin_client import FsApiThinClient
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.proto.apex.metrics_sink_tprt_client import StreamingQueue
from dropbox.proto.nucleus.published_event_pb2 import GetPublishedEventsReq as GetPublishedEventsReqProto, PublishedEvent as PublishedEventProto
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
PUBLISHED_EVENT_THREAD_NAME = 'NUCLEUS_PUBLISHED_EVENTS'
STREAMED_EVENTS_THREAD_NAME = 'NUCLEUS_STREAMED_EVENTS'
FSAPI_STREAMED_EVENTS_THREAD_NAME = 'FS_API_STREAMED_EVENTS'

class _PublishedEventsThread(InstrumentedMessageQueueThread):
    pass
# WARNING: Decompyle incomplete


class _StreamedEventMetrics:
    
    def __init__(self = None):
        self._lock = Lock()
        self._current_length = 0
        self._max_length = 0

    
    def update(self = None, current_queue_length = None):
        self._lock
        self._current_length = current_queue_length
        if self._current_length > self._max_length:
            self._max_length = self._current_length
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get(self = None, should_report = None, ts = None):
        self._lock
        max_length = self._max_length
        if should_report:
            self._max_length = 0
        None(None, None)
        return 
        with None:
            if not None, {
                'previous_length': self._current_length,
                'max_length': max_length }:
                pass



class PublishedEventPerfSession:
    
    def __init__(self = None, start_time = None, group_name = None):
        self._published_event_perf_session = PerfSession.create_with_start_time(start_time = start_time, group_name = group_name, sampling_rate = 1, log_to_amp_namespace = PerfSessionAmpLoggingNamespace.CLIENT_SYNC_BOUNDARY)

    
    def add_extra(self = None, tag = None, value = None, log_to_amp = (False,)):
        if self._published_event_perf_session:
            self._published_event_perf_session.add_extra(tag, value, log_to_amp)
            return None

    
    def checkpoint(self = None, name = None):
        time = datetime.datetime.now().timestamp()
        self._published_event_perf_session.checkpoint_bridge_internal(name, time)

    
    def checkpoint_overriding_timestamp(self = None, name = None, time = None):
        self._published_event_perf_session.checkpoint_overriding_timestamp(name, time)

    
    def end(self = None):
        self._published_event_perf_session.end('sync_progress_perf_session_end')



def _get_job_name_for_monitoring(published_event = None):
    published_event_type = published_event.WhichOneof('event')
    if published_event_type != 'reactive':
        return published_event_type
    return None.reactive.WhichOneof('payload')


class PublishedEventWrapper:
    
    def __init__(self, event = None, prev_checkpoints = None, gandalf = None, account = ('event', 'PublishedEventProto', 'prev_checkpoints', 'List[int]', 'gandalf', 'Gandalf', 'account', 'AccountInterface', 'return', 'None')):
        self.event = event
        self.perf_session = None
        event_monitoring_enabled = gandalf.allows('desktop-published-event-monitoring', account = account)
        if not event_monitoring_enabled:
            return None
    # WARNING: Decompyle incomplete

    
    def add_extra(self = None, tag = None, value = None, log_to_amp = (False,)):
        if self.perf_session:
            self.perf_session.add_extra(tag, value, log_to_amp)
            return None

    
    def mark_checkpoint(self = None, name = None):
        if not self.perf_session:
            return None
        None.perf_session.checkpoint(name)

    
    def end_perf_session(self = None):
        if not self.perf_session:
            return None
        None.perf_session.end()



class _StreamedEventsThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class EventPublisher:
    
    def __init__(self, handle_publish_event, account, nucleus_thin_client, periodic_metrics_reporter = None, gandalf = None, backup_mode = None, fs_api_thin_client = ('handle_publish_event', 'Callable[[PublishedEventWrapper], None]', 'account', 'AccountInterface', 'nucleus_thin_client', 'NucleusThinClient', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'gandalf', 'Gandalf', 'backup_mode', 'Optional[BackupModeArgs]', 'fs_api_thin_client', 'Optional[FsApiThinClient]')):
        self._handle_published_event_internal = handle_publish_event
        self._gandalf = gandalf
        self._account = account
        self._backup_mode = backup_mode
        self._fs_api_thin_client = fs_api_thin_client
        self.tprt_streaming_allowed = is_tprt_enabled()
        TRACE('[TPRT] TPRT streaming enabled: %r', self.tprt_streaming_allowed)
        self.periodic_metrics_reporter = periodic_metrics_reporter
        self._nucleus_thin_client = nucleus_thin_client
        self._streamed_fs_api_events_thread = None
        if self.tprt_streaming_allowed:
            self._create_streamed_events_thread()
            return None
        self._published_events_thread = db_thread_with_task_timing(_PublishedEventsThread, DesktopComponent.NUCLEUS, _PublishedEventsThread.instrumented_name())(self._account, backup_mode)

    
    def _create_streamed_fs_api_events_thread(self = None):
        if self._fs_api_thin_client:
            TRACE('Creating streamed_fs_api_events_thread')
            self._streamed_fs_api_events_thread = db_thread(_StreamedEventsThread)(thin_client = self._fs_api_thin_client, handle_published_event_internal = self._handle_published_event_internal, gandalf = self._gandalf, account = self._account, tag = 'FS_API', backup_mode = self._backup_mode)
            
            try:
                metric_name = self._tprt_metric_name(is_fs_api = True)
                TRACE('[TPRT] Registering TPRT metrics under name=%s', metric_name)
                self.periodic_metrics_reporter.add_reporter(name = metric_name, reporter = self._streamed_fs_api_events_thread.get_metrics)
                return None
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.NUCLEUS)
                return None
                return None


    
    def _create_streamed_events_thread(self = None):
        TRACE('Creating streamed_events_thread')
        self._streamed_events_thread = db_thread(_StreamedEventsThread)(thin_client = self._nucleus_thin_client, handle_published_event_internal = self._handle_published_event_internal, gandalf = self._gandalf, account = self._account, tag = '', backup_mode = self._backup_mode)
        
        try:
            metric_name = self._tprt_metric_name(is_fs_api = False)
            TRACE('[TPRT] Registering TPRT metrics under name=%s', metric_name)
            self.periodic_metrics_reporter.add_reporter(name = metric_name, reporter = self._streamed_events_thread.get_metrics)
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.NUCLEUS)

        self._create_streamed_fs_api_events_thread()

    
    def _tprt_metric_name(self = None, is_fs_api = None):
        metric_name = 'tprt' if self._account.is_primary else 'secondary_tprt'
        if self._backup_mode:
            metric_name = 'bkup_' + metric_name
        if is_fs_api:
            metric_name = 'fsapi_' + metric_name
        return metric_name

    
    def register_fs_api_client(self = None, fs_api_thin_client = None):
        self._fs_api_thin_client = fs_api_thin_client
    # WARNING: Decompyle incomplete

    
    def set_connection_reset(self = None):
        self._streamed_events_thread.set_connection_reset()
        if self._streamed_fs_api_events_thread:
            self._streamed_fs_api_events_thread.set_connection_reset()
            return None

    
    def restart_event_streaming(self = None):
        if self.tprt_streaming_allowed:
            TRACE('Stopping events streaming...')
            self.stop()
            TRACE('Restarting events streaming...')
            self._create_streamed_events_thread()
            self._streamed_events_thread.start()
            if self._streamed_fs_api_events_thread:
                self._streamed_fs_api_events_thread.start()
                return None
            return None

    
    def handle_published_event(self = None, published_event_wrapper = None):
        pass
    # WARNING: Decompyle incomplete

    
    def start(self = None):
        TRACE('EventPublisher starting...')
        if self.tprt_streaming_allowed:
            self._streamed_events_thread.start()
            if self._streamed_fs_api_events_thread:
                self._streamed_fs_api_events_thread.start()
                return None
            return None
        None._published_events_thread.start()

    
    def stop(self = None):
        TRACE('EventPublisher stopping...')
        if self.tprt_streaming_allowed:
            self._streamed_events_thread.signal_stop()
            metric_name = self._tprt_metric_name(is_fs_api = False)
            self.periodic_metrics_reporter.remove_reporter(metric_name)
            if self._streamed_fs_api_events_thread:
                self._streamed_fs_api_events_thread.signal_stop()
                metric_name = self._tprt_metric_name(is_fs_api = True)
                self.periodic_metrics_reporter.remove_reporter(metric_name)
                return None
            return None
        None._published_events_thread.signal_stop()


