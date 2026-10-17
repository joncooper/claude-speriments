# Source Generated with Decompyle++
# File: debugging.pyc (Python 3.11)

from __future__ import absolute_import
import code
import functools
import inspect
import os
import pprint
import random as insecure_random
import sys
import threading
import time
from collections import defaultdict
from typing import Callable, DefaultDict, Dict, Text
from six import iteritems
from dropbox.threading import Lock
from dropbox.trace import TRACE

def get_default_call_site_name(frames_to_skip = None):
    frames_to_skip += 1
# WARNING: Decompyle incomplete


def trace_calls(f = None, call_stack_idx = None):
    pass
# WARNING: Decompyle incomplete

SKIPPED_FUNCTION_NAMES = set([
    '__enter__',
    '__exit__',
    'acquired',
    'read_lock',
    'released',
    'reserved_lock',
    'waiting',
    'wrapped',
    'write_lock'])

def last_caller(skipped_function_names = (None,)):
    pass
# WARNING: Decompyle incomplete


def is_caller_in_stack(function):
    frame = inspect.currentframe().f_back
# WARNING: Decompyle incomplete

_caller_count_lock = Lock()
_functions_to_caller_counts: 'Dict[str, DefaultDict[str, int]]' = { }

def record_callers_dec(blacklist = (None,)):
    pass
# WARNING: Decompyle incomplete


def print_callers():
    _caller_count_lock
    for k, counts in iteritems(_functions_to_caller_counts):
        pprint.pprint(f'''{k!s}: {pprint.pformat(dict(counts))!s}''')
        None(None, None)
        return None
        with None:
            if not None:
                pass

DEBUG_SHELL_THREAD_NAME = 'DEBUG_SHELL'

def _interactive_shell(env = None, on_error = None):
    
    try:
        ipython_present = True
        
        try:
            InteractiveShellEmbed = InteractiveShellEmbed
            import IPython.terminal.embed
            
            try:
                pass
            except ImportError:
                ipython_present = False
                
                try:
                    pass
                try:
                    if ipython_present:
                        shell = InteractiveShellEmbed(user_ns = env)
                        shell.display_banner = False
                        shell.quiet = True
                        shell()
                        return None
                    code.interact(local = env)
                    return None
                except Exception:
                    on_error()
                    return None






def run_interactive_shell(env = None, on_error = None):
    debug_shell_thread = threading.Thread(target = _interactive_shell, kwargs = dict(env = env, on_error = on_error), name = DEBUG_SHELL_THREAD_NAME)
    debug_shell_thread.daemon = True
    debug_shell_thread.start()
    del debug_shell_thread

