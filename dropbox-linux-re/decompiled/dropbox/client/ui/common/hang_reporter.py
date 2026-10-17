# Source Generated with Decompyle++
# File: hang_reporter.pyc (Python 3.11)

from __future__ import absolute_import
import time
from typing import Any, Callable, Text
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.threadutils import SafeValue
from dropbox.trace import dump_python_stacks, TRACE, WARNING

class HangReporter(object):
    
    def __init__(self):
        self.time_func = time.time
        self.index = 0

    
    def set_time_func(self, time_func):
        self.time_func = time_func

    
    def check_for_hang(self = None, timeout = None, post_message = None, thread_display_name = ('timeout', 'float', 'post_message', 'Callable[..., Callable[..., Any]]', 'thread_display_name', 'Text', 'return', 'bool')):
        TRACE('Posting a message to %s to check if it is hung (current_index: %d).', thread_display_name, self.index)
        f = (lambda index = None: TRACE('Processing hang detection index %d', index)1)()
        start_time = self.time_func()
        sv = f(self.index)
        self.time_func() + timeout = self, self.index += 1, .index
        wait_time = max(0, end_time - self.time_func())
        val = sv.wait(wait_time)
        if val == 1:
            TRACE('Successfully posted message to %s (returned in %f seconds)', thread_display_name, self.time_func() - start_time)
            return False
        if None.time_func() > end_time:
            if SystemStatusMonitorWrapper.did_sleep_between(start_time, end_time):
                message = 'Not reporting hang in %s since the host entered sleep.' % thread_display_name
                report_hang = False
            else:
                message = 'Detected hang in %s.  Message was not processed after %d seconds.' % (thread_display_name, timeout)
                report_hang = True
            py_stack = dump_python_stacks()
            report_list = [
                '%s:\n' % message]
            report_list.extend(py_stack)
            WARNING(''.join(report_list))
            return report_hang



class _TestHangActor(Actor):
    pass
# WARNING: Decompyle incomplete


class ActorThreadPoolHangReporter(Destroyable, Actor):
    pass
# WARNING: Decompyle incomplete

