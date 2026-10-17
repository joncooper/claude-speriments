# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from time import time as _time
from typing import Any, Callable, Dict, Optional, Text
from apex.metrics import MetricsReporter
from CoreFoundation import CFRunLoopAddSource, CFRunLoopGetMain, kCFRunLoopCommonModes, kCFRunLoopDefaultMode
from SystemConfiguration import kSCNetworkFlagsConnectionRequired, kSCNetworkFlagsReachable, SCDynamicStoreCreate, SCDynamicStoreCreateRunLoopSource, SCDynamicStoreKeyCreateProxies, SCDynamicStoreRef, SCDynamicStoreSetNotificationKeys, SCNetworkReachabilityCreateWithName, SCNetworkReachabilityGetFlags, SCNetworkReachabilityRef, SCNetworkReachabilityScheduleWithRunLoop, SCNetworkReachabilitySetCallback
from build_number import BUILD_KEY
from dropbox.callbacks import Handler
from dropbox.client.message_queue import MessageQueueThread
from dropbox.connectivity_watch.watch_interface import ConnectivityState, ConnectivityWatchInterface
from dropbox.db_thread import db_thread
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.mac.internal import autoreleasepool
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.trace import TRACE

class _ConnectivityWatchThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ConnectivityWatchThread = db_thread(_ConnectivityWatchThreadImpl)
on_connectivity_watch_thread = ConnectivityWatchThread.on_queue

class ConnectivityWatch(ConnectivityWatchInterface):
    INITIAL_CHANGE_WINDOW_SECS = 5
    
    def __init__(self = None, metrics_reporter = None):
        self._metrics_reporter = metrics_reporter
        self._callbacks = { }
        self._lock = Lock()
        self._reachability_map = { }
        self._reachability_flags_by_host = { }
        self._dynamic_store = None

    
    def start_watch(self = None):
        self._thread = ConnectivityWatchThread()
        self._thread.start()

    register_callback = (lambda self = None, host = None, callback_fn = handle_exceptions: if not isinstance(host, Text):
raise TypeError('Host name %r should be a unicode string!' % host)if host.startswith('http'):
raise ValueError('Host name %r should not start with http!' % host)needs_init = Falseself._lockif host not in self._callbacks:
self._callbacks[host] = Handler(recursive = False, handle_exc = report_exception)needs_init = TrueNone(None, None))()
    _create_dynamic_store_if_necessary = (lambda self = None: if self._dynamic_store:
Noneautoreleasepool()self._dynamic_store = SCDynamicStoreCreate(None, '%s-Store' % BUILD_KEY, self._on_proxy_change, None)dynamic_store = SCDynamicStoreCreate(None, '%s-Store' % BUILD_KEY, self._on_proxy_change, None)SCDynamicStoreSetNotificationKeys(dynamic_store, [
SCDynamicStoreKeyCreateProxies(None)], None)update_source = SCDynamicStoreCreateRunLoopSource(None, dynamic_store, 0)CFRunLoopAddSource(CFRunLoopGetMain(), update_source, kCFRunLoopDefaultMode)None(None, None)Nonewith None:
if not None:
pass)()
    
    def _create_reachability(self = None, host = None):
        autoreleasepool()
        reachability = None(SCNetworkReachabilityCreateWithName, host.encode('ascii'))
        (success, initial_flags) = SCNetworkReachabilityGetFlags(reachability, None)
        TRACE('Initializing mac reachability for %r to %r', host, initial_flags)
        if success:
            self._lock
            self._reachability_flags_by_host[host] = initial_flags
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        current_state = self.get_connectivity_state(host)
        self._reachability_map[reachability] = ConnectivityState(current_state.state, get_monotonic_time_seconds())
        SCNetworkReachabilitySetCallback(reachability, self._on_connectivity_change, host)
        SCNetworkReachabilityScheduleWithRunLoop(reachability, CFRunLoopGetMain(), kCFRunLoopCommonModes)
