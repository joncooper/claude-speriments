# Source Generated with Decompyle++
# File: auto_updater.pyc (Python 3.11)

import itertools
from concurrent.futures import Future, InvalidStateError
from enum import Enum
from typing import Callable, Dict, Iterator, Optional, Tuple
from apex._apex import ffi, lib
from dropbox.proto.apex.auto_updater_pb2 import UpdaterEvent

class UpdatePriority(Enum):
    BACKGROUND = 0
    FOREGROUND = 1

UpdaterEventCallback = Callable[([
    UpdaterEvent], None)]
ListenerToken = Tuple[(ffi.CData, int)]
_CALLBACK_ID: 'Iterator[int]' = itertools.count()
_CALLBACK_CONTEXTS: 'Dict[int, UpdaterEventCallback]' = { }

class BrowserType(Enum):
    UNKNOWN = 0
    CHROME = 1
    EDGE = 2


class BrowserExtensionInstallStatus(Enum):
    SUCCESS = 0
    IO_ERROR = 1
    COMMAND_ERROR = 2

_BROWSER_EXTENSION_INSTALL_STATUS_CALLBACK_ID: 'Iterator[int]' = itertools.count()
_BROWSER_EXTENSION_INSTALL_STATUS_CALLBACK_CONTEXTS: 'Dict[int, Future[BrowserExtensionInstallStatus]]' = { }
_DEFAULT_BROWSER_CALLBACK_ID: 'Iterator[int]' = itertools.count()
_DEFAULT_BROWSER_CALLBACK_CONTEXTS: 'Dict[int, Future[BrowserType]]' = { }
register_listener_cb = (lambda context = None, event_bytes = None, event_len = ffi.def_extern(): callback = _CALLBACK_CONTEXTS[int(ffi.cast('unsigned long', context))]event = UpdaterEvent.FromString(bytes(ffi.buffer(event_bytes, event_len)))callback(event))()
browser_extension_install_status_cb = (lambda context = None, status = None: future = _BROWSER_EXTENSION_INSTALL_STATUS_CALLBACK_CONTEXTS.pop(int(ffi.cast('unsigned long', context)))try:
future.set_result(BrowserExtensionInstallStatus(status))Noneexcept InvalidStateError:
None)()
get_default_browser_cb = (lambda context = None, browser_type = None: future = _DEFAULT_BROWSER_CALLBACK_CONTEXTS.pop(int(ffi.cast('unsigned long', context)))try:
future.set_result(BrowserType(browser_type))Noneexcept InvalidStateError:
None)()

class AutoUpdaterClient:
    
    def __init__(self = None, ctx = None):
        self.context = ffi.cast('void *', ctx)

    
    def install_and_register(self = None):
        lib.auto_updater_install_and_register(self.context)

    
    def update(self = None, priority = None, allow_same_version = None):
        lib.auto_updater_update(self.context, priority.value, allow_same_version)

    
    def get_installed_apps(self = None):
        lib.auto_updater_get_installed_apps(self.context)

    
    def install_app(self = None, app_id = None, client_install_data = None, install_data_index = ('app_id', 'str', 'client_install_data', 'Optional[str]', 'install_data_index', 'Optional[str]', 'return', 'None')):
        c_app_id = ffi.new('char[]', app_id.encode('utf-8'))
    # WARNING: Decompyle incomplete

    
    def install_browser_extension(self = None, extension_id = None, browser_type = None, restart_browser_if_necessary_if_necessary = ('extension_id', 'str', 'browser_type', 'BrowserType', 'restart_browser_if_necessary_if_necessary', 'bool', 'return', 'Future[BrowserExtensionInstallStatus]')):
        c_extension_id = ffi.new('char[]', extension_id.encode('utf-8'))
        callback_id = next(_BROWSER_EXTENSION_INSTALL_STATUS_CALLBACK_ID)
        fut = Future()
        _BROWSER_EXTENSION_INSTALL_STATUS_CALLBACK_CONTEXTS[callback_id] = fut
        lib.auto_updater_install_browser_extension(self.context, c_extension_id, browser_type.value, restart_browser_if_necessary_if_necessary, ffi.cast('void *', callback_id), lib.browser_extension_install_status_cb)
        return fut

    
    def get_default_browser(self = None):
        callback_id = next(_DEFAULT_BROWSER_CALLBACK_ID)
        fut = Future()
        _DEFAULT_BROWSER_CALLBACK_CONTEXTS[callback_id] = fut
        lib.auto_updater_get_default_browser(self.context, ffi.cast('void *', callback_id), lib.get_default_browser_cb)
        return fut

    
    def promote(self = None):
        lib.auto_updater_promote(self.context)

    
    def register_listener(self = None, callback = None):
        callback_id = next(_CALLBACK_ID)
        _CALLBACK_CONTEXTS[callback_id] = callback
        listener_token_ptr = lib.auto_updater_register_listener(self.context, ffi.cast('void *', callback_id), lib.register_listener_cb)
        return (listener_token_ptr, callback_id)

    
    def unregister_listener(self = None, listener_token = None):
        (listener_token_ptr, callback_id) = listener_token
        lib.auto_updater_unregister_listener(listener_token_ptr)
        _CALLBACK_CONTEXTS.pop(callback_id)



def get_updater_id():
    updater_id = lib.auto_updater_get_updater_id()
    return ffi.string(updater_id).decode('utf-8') if updater_id != ffi.NULL else None


def is_installing(app_name = None):
    return lib.auto_updater_is_installing(app_name)

