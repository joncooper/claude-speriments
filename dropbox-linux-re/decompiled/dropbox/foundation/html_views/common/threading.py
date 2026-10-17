# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import functools
from typing import Callable, Optional, TypeVar
from dropbox.client.ui.common.uikit import MainMessageQueue
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import EasyFuture, Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.basic import BaseFuture
from dropbox.foundation.navigation_service.threading import assert_on_navigation_service_thread, on_navigation_service_thread, on_navigation_service_thread_returns_none
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.gui import event_handler
from dropbox.trace import WARNING
on_html_view_thread = on_navigation_service_thread
on_html_view_thread_returns_none = on_navigation_service_thread_returns_none
assert_on_html_view_thread = assert_on_navigation_service_thread
on_html_view_thread_future = make_on_thread_future_decorator(on_html_view_thread, 'on_html_view_thread_future')
assert_on_ui_thread = MainMessageQueue.assert_on_queue
background_event_handler = functools.partial(event_handler, thread_name = None)
ValueType = TypeVar('ValueType')

def UiEventFuture():
    '''UiEventFuture'''
    pass
# WARNING: Decompyle incomplete

UiEventFuture = <NODE:27>(UiEventFuture, 'UiEventFuture', EasyFuture[ValueType])

def LatencySensitiveBridgeFuture():
    '''LatencySensitiveBridgeFuture'''
    pass
# WARNING: Decompyle incomplete

LatencySensitiveBridgeFuture = <NODE:27>(LatencySensitiveBridgeFuture, 'LatencySensitiveBridgeFuture', BaseFuture[ValueType])

class UiEventTimeoutException(Exception):
    pass


def UiEventTimeoutFuture():
    '''UiEventTimeoutFuture'''
    pass
# WARNING: Decompyle incomplete

UiEventTimeoutFuture = <NODE:27>(UiEventTimeoutFuture, 'UiEventTimeoutFuture', UiEventFuture[ValueType])
