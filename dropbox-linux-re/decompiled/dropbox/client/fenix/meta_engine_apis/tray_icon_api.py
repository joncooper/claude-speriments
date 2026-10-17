# Source Generated with Decompyle++
# File: tray_icon_api.pyc (Python 3.11)

from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.tray_icon_pb2 import CanPromoteTrayIconReply, CanPromoteTrayIconReq, GetIsTrayIconPromotedReply
from dropbox.client.fenix.journeys.tray.icon_utils import can_promote_tray_icon, is_tray_icon_promoted
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.tray_icon_api_base import _TrayIconBaseClass
from dropbox.client.fenix.meta_engine_apis.meta_engine_utils import proto_to_authenticated_account_dict
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class TrayIconAPI(_TrayIconBaseClass):
    pass
# WARNING: Decompyle incomplete

