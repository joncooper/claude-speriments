# Source Generated with Decompyle++
# File: preauth.pyc (Python 3.11)

from typing import Any, Callable, Dict, Text
from mypy_extensions import DefaultNamedArg
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.setup_wizard.setup_wizard_constants import DEVICE_LIMIT_EXCEEDED
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxResponseClientError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.hostname import get_local_host_display_name
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
try_preauth = (lambda account, app, conn = None, preauth_nonce = None, on_success = on_background_thread(), on_failure = ('account', 'AccountInterface', 'app', 'DropboxApplication', 'conn', 'DropboxConnection', 'preauth_nonce', 'Text', 'on_success', 'Callable[[Dict[Text, Any]], None]', 'on_failure', "Callable[[str, bool, DefaultNamedArg(DropboxResponseClientError, 'error'), DefaultNamedArg(dict, 'extra_context')], None]", 'return', 'None'): display_name = Text('localhost')try:
display_name = get_local_host_display_name()except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.SETUP_WIZARD)TRACE('preauth: try to link host %r', account.host_int)try:
result_dict = conn.link_host_with_ret(host_secret = account.host_secret, email = account.email, password = None, display_name = display_name, is_sso_link = False, post_2fa_token = '', is_preauth_link = True, tag_str = make_unicode(app.installer_tag), preauth_nonce = preauth_nonce, install_type = app.install_type, client_info = app.get_client_info())_handle_result_dict(app, result_dict, on_success, on_failure)Noneexcept DropboxResponseClientError:
e = Nonereport_exception(severity = Severity.TRACE, component = DesktopComponent.SETUP_WIZARD)on_failure(e.args[0], False, error = e)e = Nonedel eNonee = Nonedel e)()

def _handle_result_dict(app = None, result_dict = None, on_success = None, on_failure = ('app', 'DropboxApplication', 'result_dict', 'dict', 'on_success', 'Callable[[Dict[Text, Any]], None]', 'on_failure', "Callable[[str, bool, DefaultNamedArg(dict, 'extra_context')], None]", 'return', 'None')):
    status = result_dict.get('ret', None)
    if status and status == 'ok':
        TRACE('Preauth succeeded!')
        app.handle_deal_response(result_dict)
        on_success(result_dict)
        return None
    TRACE('Preauth failed. response: %r', result_dict)
    if status == 'fail':
        if not result_dict.get('errors'):
            reason = result_dict.get('reason_type')
            fully_deprecated = result_dict.get('fully_deprecated', False)
            if reason == DEVICE_LIMIT_EXCEEDED:
                extra_context = {
                    'device_limit_sw_nonce': result_dict.get('device_limit_sw_nonce', None) }
                on_failure(str(reason), fully_deprecated, extra_context = extra_context)
                return None
            on_failure(str(reason), fully_deprecated)
            return None
        if not result_dict.get('errors'):
            report_bad_assumption('Server returned malformed result for preauth: %r', result_dict)
    on_failure(status, False)

