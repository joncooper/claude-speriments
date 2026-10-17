# Source Generated with Decompyle++
# File: threadutils.pyc (Python 3.11)

from __future__ import absolute_import
import functools
import itertools
import os
import threading
from concurrent.futures import Executor, Future
from typing import Any, Dict, Generic, Optional, TypeVar
from six import reraise
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import AtomicCounter
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.native_event import AutoResetEvent
from dropbox.native_queue import Empty, Queue
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threading import Condition
from dropbox.trace import TRACE
if IS_WINDOWS:
    from winerror import ERROR_ACCESS_DENIED, ERROR_INVALID_PARAMETER
    from winffi.kernel32.api import get_thread_name as win_get_thread_name, set_current_thread_name as win_set_current_thread_name
elif IS_MAC:
    from macffi.pthread import get_thread_name
elif IS_LINUX:
    from lib.linuxffi.pthread.api import set_current_thread_name
THREAD_CPU_COUNTER_ID_TO_NAME: 'Dict[int, str]' = { }

def set_thread_cpu_counter_name(name = None):
    if IS_LINUX:
        if is_main_thread():
            return None
        set_current_thread_name(name.encode('ascii')[:15])
        return None
# WARNING: Decompyle incomplete


def get_thread_cpu_counter_name(ident = None):
    if IS_LINUX:
        if ident == os.getpid():
            return threading.main_thread().name
        pth = None % ident
        
        try:
            return open(pth).read().strip()
        except (ProcessLookupError, FileNotFoundError):
            return None
            except Exception:
                report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SHARED_WORKER)
            return None
            if IS_MAC:
                if ident == threading.main_thread().ident:
                    return threading.main_thread().name
                
                try:
                    if not get_thread_name(ident):
                        return None
                    except ProcessLookupError:
                        return None
                    if IS_WINDOWS:
                        
                        try:
                            if not win_get_thread_name(ident):
                                return None
                            except NotImplementedError:
                                return 
                            except OSError:
                                if hasattr(e, 'winerror') or e.winerror not in (ERROR_INVALID_PARAMETER, ERROR_ACCESS_DENIED):
                                    report_exception(severity = Severity.WARN, component = DesktopComponent.SHARED_WORKER)
                                else:
                                    report_exception(severity = Severity.TRACE, component = DesktopComponent.SHARED_WORKER)
                                None = None
                                del e
                                return None
                                e = None
                                del e
                            except Exception:
                                report_exception(severity = Severity.WARN, component = DesktopComponent.SHARED_WORKER)
                                return None
                            raise NotImplementedError('Unsupported platform')




_T = TypeVar('_T')

class ThreadPool(Executor):
    sentinel = object()
    
    def __init__(self, name, pool_size, max_num_threads, max_queue_size, expected_exceptions, account = (0, (), None)):
        pass
    # WARNING: Decompyle incomplete

    
    def submit(self, f, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _cond_wait(self):
        start_time = get_monotonic_time_seconds()
        self.pool_size_cond.wait(timeout = 300)
        if get_monotonic_time_seconds() - start_time > 299:
            report_bad_assumption('pool_size=%d. workers=%d. overflow=%d', self.pool_size, len(self.workers), len(self.overflow_workers))
            return None

    
    def shutdown(self, wait = (True,)):
        self.pool_size_cond
        self.pool_size = 0
        for worker in self.workers:
            self.work_queue.put((None, self.sentinel))
            None(None, None)
        with None:
            if not None:
                pass
    # WARNING: Decompyle incomplete

    
    def set_pool_size(self, new_pool_size, max_num_threads = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_pool_size(self):
        self.pool_size_cond
        None(None, None)
        return 
        with None:
            if not None, self.pool_size:
                pass

    
    def num_active_workers(self):
        return int(self._num_active_workers)

    
    def has_outstanding_work(self = None):
        return self.work_queue.qsize(include_inflight = True) > 0

    
    def _make_workers(self, num_workers, is_overflow_worker, idx = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _process_work(self, is_overflow_worker):
        pass
    # WARNING: Decompyle incomplete

    
    def wakeup(self):
        TRACE('Waking up pool %r', self.name)
        self.pool_size_cond
        for worker in itertools.chain(self.workers, self.overflow_workers):
            worker.wakeup()
            None(None, None)
            return None
            with None:
                if not None:
                    pass



class Stoppable(object):
    pass
# WARNING: Decompyle incomplete


class AccountAvailableMixin(object):
    pass
# WARNING: Decompyle incomplete


class StoppableThread(threading.Thread, Stoppable):
    pass


class StoppableThreadWithAccount(StoppableThread, AccountAvailableMixin):
    pass


class SafeValueCanceledException(Exception):
    pass


def SafeValue():
    '''SafeValue'''
    
    def __init__(self = None):
        self.event = threading.Event()
        self.excepted = False
        self.canceled = False
        self.value = None
        self.exc_info = None

    
    def set(self = None, value = None):
        self.value = value
        self.event.set()

    
    def set_exception(self = None, exc = None, exc_info = None):
        self.value = exc
        self.exc_info = exc_info
        self.excepted = True
        self.event.set()

    
    def is_set(self = None):
        return self.event.is_set()

    
    def wait(self = None, *n, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def cancel(self = None):
        if self.is_set():
            return False
        self.canceled = None
        self.event.set()
        return True


SafeValue = <NODE:27>(SafeValue, 'SafeValue', Generic[_T])

class TimingData(object):
    
    def __init__(self):
        self.thread_name = threading.current_thread().name
        self.start_time = None
        self.end_time = None

    
    def __enter__(self):
        self.start_time = get_monotonic_time_seconds()
        return self

    
    def __exit__(self, type_, value, traceback):
        self.end_time = get_monotonic_time_seconds()



def is_main_thread():
    return threading.current_thread() is threading.main_thread()


def inherit_parent_thread_name(func):
    pass
# WARNING: Decompyle incomplete


class thread_id_properties(object):
    pass
# WARNING: Decompyle incomplete

