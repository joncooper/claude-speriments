# Source Generated with Decompyle++
# File: menu_actions.pyc (Python 3.11)

from typing import Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.features.file_requests.models.constants import CREATE_FROM_DESKTOP_URL, FileRequestEventType, FileRequestInadequatePermissionsError
from dropbox.client.features.file_requests.models.create_file_request import report_file_request_event, validate_path_and_build_url_params
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.icon_overlay import IconOverlayStrings
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.types.local_path import NonSyncingLocalPathException
from dropbox.trace import TRACE

def create_file_request(ui_kit, desktop_login = None, sync_engine_adapter = None, account = None, path = ('ui_kit', 'BaseUIKit', 'desktop_login', 'DesktopLogin', 'sync_engine_adapter', 'SyncEngineAdapter', 'account', 'AccountInterface', 'path', 'Text')):
    
    try:
        url_params = validate_path_and_build_url_params(sync_engine_adapter, account, path)
        desktop_login.login_and_redirect(f'''{CREATE_FROM_DESKTOP_URL!s}?{url_params!s}''', account = account)
        report_file_request_event(FileRequestEventType.FILE_REQUEST_ADD_MENU_ITEM_CLICKED, account)
        return None
    except FileRequestInadequatePermissionsError:
        dialog_future = ui_kit.show_native_blocking_dialog(caption = IconOverlayStrings.file_request_error_heading, message = IconOverlayStrings.file_request_error_inadequate_permissions, buttons = [
            IconOverlayStrings.ok_button], dialog_source_type = DialogSourceTypes.OTHER)
        dialog_future.block()
        report_file_request_event(FileRequestEventType.FILE_REQUEST_ADD_MENU_ITEM_FAILED, account, error_type = 'inadequate_permissions')
        return None
        except NonSyncingLocalPathException:
            dialog_future = ui_kit.show_native_blocking_dialog(caption = IconOverlayStrings.file_request_error_heading, message = IconOverlayStrings.file_request_error_item_has_not_synced, buttons = [
                IconOverlayStrings.ok_button], dialog_source_type = DialogSourceTypes.OTHER)
            dialog_future.block()
            report_file_request_event(FileRequestEventType.FILE_REQUEST_ADD_MENU_ITEM_FAILED, account, error_type = 'not_synced')
            return None
        except Exception:
            TRACE('%r', path, account = account)
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.FILE_EVENTS)
            return None


