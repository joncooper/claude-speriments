# Source Generated with Decompyle++
# File: app_info_api.pyc (Python 3.11)

import json
from dropbox.client.config import HIDDEN_FILEID_SET_KEY
from dropbox.client.device_info import get_device_info, UNSAFE_get_raw_machine_uuid
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.app_info_pb2 import ClientInfo, DeviceInfo, DropboxHosts, GetUnlinkCookieReq, HostDisplayName, InstallerTag, MachineId, PlatformInfo, PlatformVersion, UnlinkCookie
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.app_info_api_base import _AppInfoBaseClass
from dropbox.client.fenix.meta_engine_apis.meta_engine_utils import proto_to_authenticated_account_dict
from dropbox.client.util import get_platform_info
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.hostname import get_local_host_display_name
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class AppInfoAPI(_AppInfoBaseClass):
    pass
# WARNING: Decompyle incomplete

