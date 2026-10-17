# Source Generated with Decompyle++
# File: bridge_interface_unsafe_browser_api.pyc (Python 3.11)

from abc import ABC, abstractmethod
from dropbox.foundation.futures import Future
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface

class UnsafeBrowserApiBridgeInterface(ABC):
    open_uncredentialed_browser_with_absolute_url = (lambda url = None: pass)()
    open_uncredentialed_browser_with_dropbox_url = (lambda path = None: pass)()
    open_authenticated_browser_with_dropbox_url = (lambda user = None, path = None: pass)()
    open_program_with_custom_url = (lambda url = None: pass)()
    open_mail_program_with_address = (lambda email = None: pass)()

