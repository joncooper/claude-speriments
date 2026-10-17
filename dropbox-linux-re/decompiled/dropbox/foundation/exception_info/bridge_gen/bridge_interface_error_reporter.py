# Source Generated with Decompyle++
# File: bridge_interface_error_reporter.pyc (Python 3.11)

from abc import ABC, abstractmethod
from dropbox.foundation.futures import Future

class ErrorReporterBridgeInterface(ABC):
    report_bad_assumption = (lambda self = None, message = None: pass)()
    internal_report_unhandled_exception = (lambda self = None, js_stack = None: pass)()
    report_handled_exception = (lambda self = None, js_stack = None: pass)()
    report_unrecoverable_error = (lambda self = None, js_stack = None: pass)()
    report_rejected_promise = (lambda self = None, js_stack = None: pass)()
    report_react_format_error = (lambda self = None, message = None, stack = abstractmethod, template = ('message', 'str', 'stack', 'str', 'template', 'str', 'return', 'Future[None]'): pass)()
    report_i18n_error = (lambda self = None, message = None: pass)()
    record_dpi_mismatch = (lambda self = None, js_dpi = None, py_dpi = abstractmethod: pass)()

