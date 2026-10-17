# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import re
from types import TracebackType
from typing import Any, cast, Iterable, Optional, Text, Tuple, Union
from dropbox.client.util import get_contents_root
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import JavascriptError
from dropbox.exception.reporting import report_exception, report_js_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.html_views.common.interface import HtmlViewJavaScriptErrorType

class BridgeClassNotFoundException(Exception):
    pass
# WARNING: Decompyle incomplete


class BridgeInstanceNotFoundException(Exception):
    pass
# WARNING: Decompyle incomplete


class BridgeMethodNotFoundException(Exception):
    pass
# WARNING: Decompyle incomplete


class BridgeSignalNotFoundException(Exception):
    pass
# WARNING: Decompyle incomplete


class _Code(object):
    
    def __init__(self = None, name = None, filename = None):
        self.co_filename = filename
        self.co_name = name



class _Frame(object):
    
    def __init__(self = None, code = None, locals_ = None):
        self.f_code = code
        self.f_locals = locals_
        self.f_globals = { }



class _Traceback(object):
    
    def __init__(self, name = None, filename = None, lineno = None, tb_next = ('name', 'Text', 'filename', 'Text', 'lineno', 'int', 'tb_next', "Optional[Union[TracebackType, '_Traceback']]", 'return', 'None')):
        self.tb_lineno = lineno
        self.tb_lasti = -1
    # WARNING: Decompyle incomplete


_JS_STACK_FORMAT_WITH_LINE_AND_COL = re.compile('\n    \\s*at\\s*                            # Literal text "at"\n    (?:\n      (?P<function>\n        (?:new\\s)?                      # Optional "new" keyword if constructing a class\n        [A-Za-z0-9._$<>]+               # Full function name (optional)\n        (\\s+                            # Optional property name (used when a function\'s name differs from the\n                                        # property to which it is assigned, e.g. `x.foo = function bar() {}`).\n         \\[as\\s                         # Literal \'[as \'\n          [A-Za-z0-9_$]+                # function alias\n         \\]                             # Literal \']\'\n        )?\n      )\n      \\s+\\(                             # Open paren (only present if function name was specified)\n    )?\n    (?P<filename>.+)                    # File name (intentionally greedy: \':\' is part of our file names)\n    :(?P<lineno>[0-9]+)                 # Line number\n    :(?P<colno>[0-9]+)                  # Column number\n    (?(function)\\))                     # Close paren (only present if function name was specified)\n', re.VERBOSE)
_JS_STACK_FORMAT_WITH_LINE = re.compile('\n    \\s*at\\s*                            # Literal text "at"\n    (?:\n      (?P<function>\n        (?:new\\s)?                      # Optional "new" keyword if constructing a class\n        [A-Za-z0-9._$<>]+               # Full function name (optional)\n        (\\s+                            # Optional property name (used when a function\'s name differs from the\n                                        # property to which it is assigned, e.g. `x.foo = function bar() {}`).\n         \\[as\\s                         # Literal \'[as \'\n          [A-Za-z0-9_$]+                # function alias\n         \\]                             # Literal \']\'\n        )?\n      )\n      \\s+\\(                             # Open paren (only present if function name was specified)\n    )?\n    (?P<filename>.+)                    # File name (intentionally greedy: \':\' is part of our file names)\n    :(?P<lineno>[0-9]+)                 # Line number\n    (?(function)\\))                     # Close paren (only present if function name was specified)\n', re.VERBOSE)
_JS_STACK_FORMAT = re.compile('\n    \\s*at\\s*                            # Literal text "at"\n    (?:\n      (?P<function>\n        (?:new\\s)?                      # Optional "new" keyword if constructing a class\n        [A-Za-z0-9._$<>]+               # Full function name (optional)\n        (\\s+                            # Optional property name (used when a function\'s name differs from the\n                                        # property to which it is assigned, e.g. `x.foo = function bar() {}`).\n         \\[as\\s                         # Literal \'[as \'\n          [A-Za-z0-9_$]+                # function alias\n         \\]                             # Literal \']\'\n        )?\n      )\n      \\s+\\(                             # Open paren (only present if function name was specified)\n    )?\n    (?P<filename>.+)                    # File name (intentionally greedy: \':\' is part of our file names)\n    (?(function)\\))                     # Close paren (only present if function name was specified)\n', re.VERBOSE)

def _parse_js_stack(js_stack = None):
    pass
# WARNING: Decompyle incomplete

_RANDOM_URI_HOST = re.compile('^(?P<scheme>[-+.a-zA-Z0-9()<> _$]+)://[0-9a-f]{32}')
_WEBPACK_INTERNAL = re.compile('webpack-internal:///./')
_QUERY_AND_FRAGMENT = re.compile('[?#].*$')

def _strip_random_uri_host(filename = None):
    (name_without_host, sub_count) = _RANDOM_URI_HOST.subn('\\g<scheme>://random_host', filename)
    return (name_without_host, sub_count == 1)


def _strip_webpack_internal(filename = None):
    (without_webpack_internal, sub_count) = _WEBPACK_INTERNAL.subn('', filename)
    return (without_webpack_internal, sub_count == 1)


def _normalize_uri_host(filename = None):
    (filename, stripped_random_host) = _strip_random_uri_host(filename)
    (filename, stripped_webpack_internal) = _strip_webpack_internal(filename)
    if not stripped_random_host and stripped_webpack_internal:
        if os.path.isabs(filename):
            real_contents_root = os.path.realpath(get_contents_root())
            real_filename = os.path.realpath(filename)
            common_path = os.path.commonpath([
                real_contents_root,
                real_filename])
            filename = real_filename[len(common_path):].replace('\\', '/').lstrip('/')
        
    (normalized_name, sub_count) = _QUERY_AND_FRAGMENT.subn('', filename)
# WARNING: Decompyle incomplete


def merge_bridged_stacks(js_stack = None, tb = None):
    last_tb = tb
    for name, filename, lineno in _parse_js_stack(js_stack):
        last_tb = _Traceback(name, _normalize_uri_host(filename), lineno, last_tb)
        return cast(TracebackType, last_tb)


def message_from_js_stack(js_stack = None, error_type = None):
    message = js_stack.split('\n')[0]
    if error_type == HtmlViewJavaScriptErrorType.PROMISE_REJECTION:
        return '(Rejected promise) ' + message


def make_py_stack_from_js_stack(js_stack = None):
    last_tb = None
# WARNING: Decompyle incomplete


def report_view_exception(js_stack, message, component, use_js_specific_reporting = None, severity = None, use_message_for_legacy_hash = None, use_electron_transport = (Severity.CRITICAL, False, False, None), sentry_correlation_id = ('js_stack', 'str', 'message', 'str', 'component', 'DesktopComponent', 'use_js_specific_reporting', 'bool', 'severity', 'Severity', 'use_message_for_legacy_hash', 'bool', 'use_electron_transport', 'bool', 'sentry_correlation_id', 'Optional[Text]', 'return', 'None')):
