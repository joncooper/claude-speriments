# Source Generated with Decompyle++
# File: markup_api.pyc (Python 3.11)

from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.markup_pb2 import CopyImageToClipboardReq, CopyLinkReq, OpenErrorDialogReq, SetMacScreenshotThumbnailsReq
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.markup_api_base import _MarkupBaseClass
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.client.screenshots.provider.utils import set_mac_screenshot_thumbnails
from dropbox.client.screenshots.utils import copy_image_to_clipboard
from dropbox.client.ui.common.markup import MarkupStrings
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.electron_dialog_constants import DialogIconType, VisStyles
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2 import destroying
from dropbox.shared.server_path import ServerPath
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class MarkupAPI(_MarkupBaseClass):
    pass
# WARNING: Decompyle incomplete

