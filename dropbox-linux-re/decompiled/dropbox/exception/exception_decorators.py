# Source Generated with Decompyle++
# File: exception_decorators.pyc (Python 3.11)

import functools
from typing import Any, Callable, cast, Optional, TypeVar, Union
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
CallableT = TypeVar('CallableT', bound = Callable)

def _handle_exceptions_ex(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    pass
# WARNING: Decompyle incomplete

_Arg0 = TypeVar('_Arg0')
_Arg1 = TypeVar('_Arg1')
_Arg2 = TypeVar('_Arg2')
_Arg3 = TypeVar('_Arg3')
_Arg4 = TypeVar('_Arg4')
_Result = TypeVar('_Result')
_Return = TypeVar('_Return')
_ReturnResult = Union[(_Result, _Return)]
_CBOptional = TypeVar('_CBOptional', bound = Callable[(..., Optional[Any])])

def handle_exceptions_ex_0(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_1(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_2(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_3(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_4(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_5(should_raise = None, return_value = None, severity = None, component = (False, None, None, DesktopComponent.TRACES)):
    return _handle_exceptions_ex(should_raise, return_value, severity, component)


def handle_exceptions_ex_returns_optional(should_raise = None, severity = None, component = None):
    return _handle_exceptions_ex(should_raise = should_raise, return_value = None, severity = severity, component = component)

handle_exceptions = handle_exceptions_ex_returns_optional()
report_exceptions = cast(Callable[([
    CallableT], CallableT)], _handle_exceptions_ex(should_raise = True))
