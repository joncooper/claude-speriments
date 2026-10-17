# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from functools import wraps
from typing import Any, Callable, List, Mapping, Optional, overload, Sequence, Tuple, Type, TypeVar, Union
from basic import FailedFuture, flatten_future, Future, ResolvedFuture
from sleep import sleep_async
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.trace import TRACE
_K = TypeVar('_K')
_V = TypeVar('_V')
_1 = TypeVar('_1')
_2 = TypeVar('_2')
_3 = TypeVar('_3')
_4 = TypeVar('_4')
_5 = TypeVar('_5')
_6 = TypeVar('_6')
_7 = TypeVar('_7')
_8 = TypeVar('_8')
_9 = TypeVar('_9')
_10 = TypeVar('_10')
_11 = TypeVar('_11')
_12 = TypeVar('_12')
F = Future[_V]
_E = TypeVar('_E', bound = Exception)

class FutureHelpers(object):
    only_uncancelled_mapping = (lambda futures = None: pass# WARNING: Decompyle incomplete
)()
    only_uncancelled_list = (lambda futures = None: 
def back_to_list(result = None):
(lambda .0: [ value for _, value in .0 ])(sorted(result.items())())
list_as_dict = enumerate(futures)()FutureHelpers.only_uncancelled_mapping(list_as_dict).then(back_to_list))()
    all_tuple = (lambda a = None, b = staticmethod: pass)()()
    all_tuple = (lambda a = None, b = staticmethod, c = overload: pass)()()
    all_tuple = (lambda a = None, b = staticmethod, c = overload, d = ('a', 'Future[_1]', 'b', 'Future[_2]', 'c', 'Future[_3]', 'd', 'Future[_4]', 'return', 'Future[Tuple[_1, _2, _3, _4]]'): pass)()()
    all_tuple = (lambda a, b = None, c = staticmethod, d = overload, e = ('a', 'Future[_1]', 'b', 'Future[_2]', 'c', 'Future[_3]', 'd', 'Future[_4]', 'e', 'Future[_5]', 'return', 'Future[Tuple[_1, _2, _3, _4, _5]]'): pass)()()
    all_tuple = (lambda a = None, b = None, c = staticmethod, d = (None, None, None, None, None), e = ('a', 'Optional[Future[_1]]', 'b', 'Optional[Future[_2]]', 'c', 'Optional[Future[_3]]', 'd', 'Optional[Future[_4]]', 'e', 'Optional[Future[_5]]', 'return', 'Union[Future[Tuple[_1, _2]], Future[Tuple[_1, _2, _3]], Future[Tuple[_1, _2, _3, _4]], Future[Tuple[_1, _2, _3, _4, _5]]]'): defined = (a, b, c, d, e)()Future.all_list(defined).then((lambda result: ResolvedFuture(tuple(result))))
)()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass)()()
    flatten = (lambda func = None: pass# WARNING: Decompyle incomplete
)()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass)()()
    ground_and_discard = (lambda func = None: pass# WARNING: Decompyle incomplete
)()
    flatten_0 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_1 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_2 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_3 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_4 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_5 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_method_0 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_method_1 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_method_2 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_method_3 = (lambda func = None: FutureHelpers.flatten(func))()
    flatten_method_4 = (lambda func = None: FutureHelpers.flatten(func))()
    with_retry = (lambda tries = None, max_sleep_secs = None, exceptions = staticmethod, initial_sleep_secs = (None, None, 2, None), can_retry_exception_fn = ('tries', 'int', 'max_sleep_secs', 'Optional[float]', 'exceptions', 'Optional[Tuple[Type[_E], ...]]', 'initial_sleep_secs', 'float', 'can_retry_exception_fn', 'Optional[Callable[[Exception], bool]]', 'return', 'Callable[..., Any]'): pass# WARNING: Decompyle incomplete
)()

