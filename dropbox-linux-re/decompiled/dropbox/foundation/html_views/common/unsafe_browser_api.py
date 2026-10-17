# Source Generated with Decompyle++
# File: unsafe_browser_api.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import cast, Text
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.common.bridge_gen.bridge_interface_unsafe_browser_api import UnsafeBrowserApiBridgeInterface
from dropbox.foundation.raii2 import destroying
from dropbox.harmony.email import open_email
from dropbox.url_info import dropbox_url_info

class UnsafeBrowserApi(UnsafeBrowserApiBridgeInterface):
    open_uncredentialed_browser_with_absolute_url = (lambda url = None: dropbox_url_info.launch_full_url(str(url)))()()
    open_uncredentialed_browser_with_dropbox_url = (lambda path = None: url = dropbox_url_info.construct_full_url(path)dropbox_url_info.launch_full_url(url))()()
    open_program_with_custom_url = (lambda url = None: dropbox_url_info.launch_custom_url(url))()()
    open_mail_program_with_address = (lambda email = None: open_email(email.encode('utf-8')))()()
    open_authenticated_browser_with_dropbox_url = (lambda user_interface = None, url = staticmethod: user = cast(UserContext, user_interface)desktop_login_arc = destroying(DesktopLoginWrapper.from_context(user))desktop_login_arc().login_and_redirect(url, account = user.account)None(None, None)Nonewith None:
if not None:
pass)()()

