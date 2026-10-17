# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

import dataclasses
from typing import Any, Optional
from typing_extensions import Protocol
from apex._apex import ffi, lib
from apex.analytics import AnalyticsClient
from apex.auth import OAuthClient
from apex.auto_updater import AutoUpdaterClient
from apex.config import HostInformation
from apex.dbxlog import Logger
from apex.health import HealthMonitoring
from apex.lifecycle import set_shutdown
from apex.metrics import MetricsReporter
from apex.metrics.metrics import MetricsReporterImpl
from apex.stormcrow import StormcrowClient
from build_number import is_test
DatabaseConfig = <NODE:12>()
CommonConfig = <NODE:12>()

class FallbackWriteFunction(Protocol):
    
    def __call__(self = None, trace_start = None, encrypted = None, err = ('trace_start', 'int', 'encrypted', 'bytes', 'err', 'str', 'return', 'None')):
        pass


DiskLoggingConfig = <NODE:12>()
DebugLoggingConfig = <NODE:12>()
LoggingConfig = <NODE:12>()
MetricsConfig = <NODE:12>()
AnalyticsConfig = <NODE:12>()
StormcrowConfig = <NODE:12>()
AutoUpdaterConfig = <NODE:12>()
Config = <NODE:12>()

class FailedToOpenDatabase(Exception):
    pass


class ApexContext:
    
    def __init__(self = None, inner = None):
        self._inner = inner
        self._health_monitoring = None
        self._trace_logger = None
        self._metrics_reporter = None
        self._event_logger = None
        self._stormcrow_client = None
        self._oauth_client = None
        self._auto_updater = None
        self._callback = None

    create = (lambda host_info = None, cert_pinning = None, force_http1 = staticmethod: c_host_info = host_info.to_ffi()ApexContext(lib.apex_context_create(c_host_info[0], cert_pinning, force_http1)))()
    _initialize_from_main_thread = (lambda : ctx = lib.apex_context_get_current()if ctx == ffi.NULL:
raise ValueError('Current context was not set!')py_ctx = ApexContext(ctx)py_ctx._trace_logger = Logger(py_ctx._inner)py_ctx._stormcrow_client = StormcrowClient(py_ctx._inner)py_ctx)()
    
    def configure(self = None, config = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cleanup(self = None):
        if not is_test():
            set_shutdown()
        lib.apex_context_cleanup(self._inner)

    
    def cleanup_and_destroy_for_tests(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def raw_ptr(self = None):
        return int(ffi.cast('uintptr_t', self._inner))

    inner = (lambda self = None: self._inner)()
    
    def get_channel_id(self = None):
        p = lib.apex_context_get_channel_id(self._inner)
        if p == ffi.NULL:
            return None
        
        try:
            lib.apex_context_free_string(p)
            return ffi.string(p).decode('utf-8')
        except:
            lib.apex_context_free_string(p)


    trace_logger = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    event_logger = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    metrics_reporter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    stormcrow_client = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    oauth_client = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    health = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    auto_updater = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

