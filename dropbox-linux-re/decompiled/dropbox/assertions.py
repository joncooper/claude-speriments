# Source Generated with Decompyle++
# File: assertions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Callable, Optional
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.trace import is_debugging
_report_assertion_error_impl: 'Optional[Callable[..., Any]]' = None
_report_exception_impl: 'Optional[Callable[..., Any]]' = None

def register_assertion_reporters(assertion_error_reporter = None, exception_reporter = None):
    global _report_assertion_error_impl, _report_exception_impl
    _report_assertion_error_impl = assertion_error_reporter
    _report_exception_impl = exception_reporter


def report_assertion_error(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def report_exception(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def assert_(predicate = None, *args, **kwargs):
    if not is_debugging():
        pass
    do_reraise = kwargs.get('always_raise', False)
    severity = Severity.TRACE if do_reraise else Severity.CRITICAL
    exc_str = ''
    if args:
        exc_str = args[0]
    error_string = None
# WARNING: Decompyle incomplete

