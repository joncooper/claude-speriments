# Source Generated with Decompyle++
# File: file_transfer_manager.pyc (Python 3.11)

from typing import Dict, Optional, Text, TypedDict
from dropbox.client.features.link_copier.model.client_shmodel_wrapper import ClientShmodelWrapper
from dropbox.client.features.transfer.logger import FileTransfersLogger
from dropbox.client.features.transfer.types import ProductConfig, TransferSettings
from dropbox.client.features.transfer.upload_manager import UploadManager
from dropbox.client.features.transfer.upload_network_interface import FileTransfersContentUploadNetworkInterface
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.journeys.file_transfer.contacts_typeahead import ContactsTypeahead
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.signals import SignalConnection, StandardSignal

class FileTransferSignals(TypedDict):
    product_config_updated: 'StandardSignal[None]' = 'FileTransferSignals'


class FileTransferSessionState:
    
    def __init__(self = None, tracking_id = None):
        self.transfer_id = None
        self.transfer_shared = False
        self.transfer_settings = TransferSettings(ttl_days = 7)
        self.transfer_tracking_id = tracking_id
        self.upload_in_progress = False



class FileTransferContextManager:
    pass
# WARNING: Decompyle incomplete

