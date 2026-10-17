# Source Generated with Decompyle++
# File: file_transfer_service.pyc (Python 3.11)

import json
from collections import defaultdict
from datetime import datetime, timezone
from os import path
from typing import Any, Dict, List, Mapping, Optional, Text, Union
from uuid import uuid4
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.features.link_copier.model.client_shmodel_wrapper import ClientShmodelWrapper
from dropbox.client.features.transfer.constants import FileTransferEntryPoint, FileTransfersApiTooManyEmailsError, FileTransfersApiTransientError, FileTransfersFileNotFoundError
from dropbox.client.features.transfer.launch_transfer import launch_file_transfer_mev
from dropbox.client.features.transfer.logger import AnalyticsEventType, AnalyticsLoggingFields, FileTransfersLogger
from dropbox.client.features.transfer.strings import TransferUIStrings
from dropbox.client.features.transfer.transfer_helpers import create_transfer, get_product_config, get_user_metadata, persist_user_default_settings, send_email_to_recipients, share_transfer_with_settings_blocking, update_metadata
from dropbox.client.features.transfer.types import ProductConfig, UserMetadata
from dropbox.client.features.transfer.upload_manager import UploadManager
from dropbox.client.features.transfer.upload_network_interface import FileTransfersContentUploadNetworkInterface
from dropbox.client.features.transfer.utils import build_view_url, file_source_logging_string, log_files_count_and_size_in_extra
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.journeys.file_transfer.bridge_dicts import DesktopFileInfo, FileTransferServiceErrorTypes
from dropbox.client.fenix.journeys.file_transfer.contacts_typeahead import ContactsTypeahead, ContactToken
from dropbox.client.fenix.journeys.file_transfer.file_transfer_manager import FileTransferContextManager
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import StandardSignal
from dropbox.model.types import FileId
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.file_system_exceptions import FSInvalidArgumentError, OperationNotPermittedError
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class FileTransferService(Actor):
    pass
# WARNING: Decompyle incomplete

