# Source Generated with Decompyle++
# File: dock_service.pyc (Python 3.11)

from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.dock_service_pb2 import CloseWindowsEvent
from dropbox.client.fenix.meta_engine_apis.base import GLOBAL_ACCOUNT_ID
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.dock_service_api_base import _DockServiceBaseClass
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DockService(_DockServiceBaseClass):
    pass
# WARNING: Decompyle incomplete

