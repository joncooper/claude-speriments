# Source Generated with Decompyle++
# File: handlers.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sys
import time
import traceback
from typing import Dict
import build_number
import psutil
from dropbox.trace import TRACE

def webdebugger_handler_wid():
    WebDebugger = WebDebugger
    import dropbox.webdebugger.server
    wid = WebDebugger().wid
# WARNING: Decompyle incomplete


def webdebugger_handler_memory():
    process = psutil.Process(os.getpid())
    return {
        'memory': process.memory_info().rss }


def webdebugger_handler_num_fds():
    process = psutil.Process(os.getpid())
    
    try:
        num_fds = process.num_fds()
    except Exception:
        num_fds = -1

    return {
        'num_fds': num_fds }


def webdebugger_handler_threads():
    threads = []
    for thread_id, stack in sys._current_frames().items():
        threads.append({
            'id': '%u' % thread_id,
            'stack': traceback.format_stack(stack) })
        return {
            'threads': threads }


def webdebugger_handler_cpu():
    proc = psutil.Process(os.getpid())
    return {
        'cpu': proc.cpu_percent(interval = 1) }


def webdebugger_handler_version():
    return {
        'version': build_number.dropbox_version.short }


def webdebugger_handler_yappi_start():
    TRACE('Starting YAPPI profiler')
    import yappi
    yappi.start()
    return {
        'status': 'ok' }


def webdebugger_handler_yappi_stop(filename = (None,)):
