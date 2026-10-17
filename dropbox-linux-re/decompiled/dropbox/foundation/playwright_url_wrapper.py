# Source Generated with Decompyle++
# File: playwright_url_wrapper.pyc (Python 3.11)

from typing import Any, Callable, Optional, TYPE_CHECKING
from dropbox.trace import TRACE
if TYPE_CHECKING:
    from dropbox.url_info import DropboxURLInfo

class PlaywrightURLInfoWrapper:
    
    def __init__(self = None, url_info = None, url_interceptor = None):
        self._url_info = url_info
        self._url_interceptor = url_interceptor

    
    def __getattr__(self = None, name = None):
        return getattr(self._url_info, name)

    
    def launch_full_url(self = None, full_url = None, new_window = None):
        TRACE('PlaywrightURLInfoWrapper: intercepting URL launch: %r', full_url)
        self._url_interceptor(full_url)
        return True

    
    def launch_full_url_with_browser(self = None, full_url = None, preferred_browser = None, new_window = (None, False)):
        TRACE('PlaywrightURLInfoWrapper: intercepting URL launch: %r', full_url)
        self._url_interceptor(full_url)
        return True


