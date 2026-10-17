# Source Generated with Decompyle++
# File: async_tools.pyc (Python 3.11)

import functools
import threading
from typing import Any, Callable, cast, Iterable, Optional, overload, TypeVar
from typing_extensions import Protocol
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.threadutils import SafeValue
_T = TypeVar('_T')

def assert_on_actor_thread(actor = None):
    actual_thread = threading.current_thread().name
    expected_thread = actor._actor_thread_name
    msg = 'Function called on the wrong thread [{}] expected [{}]'.format(actual_thread, expected_thread)
# WARNING: Decompyle incomplete


def assert_not_on_actor_thread(actor = None):
    actual_thread = threading.current_thread().name
    actor_thread = actor._actor_thread_name
    msg = 'Function called on the wrong thread [{}] '.format(actual_thread)
# WARNING: Decompyle incomplete

_SameCallable = TypeVar('_SameCallable', bound = Callable)

def future_function(base_function = None):
    pass
# WARNING: Decompyle incomplete

FutureGenerator = Callable[([], Future[None])]
FutureGeneratorGeneric = Callable[([], Future[_T])]

def is_invalid_predicate_default(rez = None):
    return False


def future_sequence(generators = None, is_invalid_predicate = None, should_return_early = None):
    pass
# WARNING: Decompyle incomplete


def future_pipeline(generators = None, first_value = None):
    pass
# WARNING: Decompyle incomplete


def if_none(func = None):
    pass
# WARNING: Decompyle incomplete


def safe_value_to_future(safe_value = None):
    pass
# WARNING: Decompyle incomplete

_ExecCtx = TypeVar('_ExecCtx', bound = ExecutionContext)
_Arg0 = TypeVar('_Arg0')
_Arg1 = TypeVar('_Arg1')
_Arg2 = TypeVar('_Arg2')
_Arg3 = TypeVar('_Arg3')
_Arg4 = TypeVar('_Arg4')
_Arg5 = TypeVar('_Arg5')
_Arg6 = TypeVar('_Arg6')
_Result = TypeVar('_Result')

class IdentityFutureProtocol(Protocol):
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _IdentityFutureProtocol__func = None: pass)()


class WrapsFutureProtocol(Protocol):
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()
    __call__ = (lambda self = None, _WrapsFutureProtocol__func = None: pass)()


def async_queued_local_function(actor_ctx = None):
    pass
# WARNING: Decompyle incomplete

