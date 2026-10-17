# Source Generated with Decompyle++
# File: camera_uploads.pyc (Python 3.11)

from typing import Dict, Iterable, Optional, Text
from dropbox.camera import Device
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.camera_upload.camera_handler import CameraHandler
from dropbox.client.camera_upload.camera_upload_context import CameraUploadContext, CameraUploadContextFactory
from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager
from dropbox.client.camera_upload.photoimporter import ActivePhotoImportsCounter
from dropbox.client.photodownloader import create_photodownloader, use_photouploader
from dropbox.client.photodownloader.base import PhotoDownloaderBase
from dropbox.client.ui.common.camera import CameraUI
from dropbox.client.ui.common.camera_wrapper import CameraUIWrapper
from dropbox.client.ui.common.preferences_utils import PanelNames
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals.standard import StandardSignal
from dropbox.functions import frozendict, synchronized_instance
from dropbox.platform import IS_MAC
from dropbox.preferences import OPT_PHOTO, OPT_VIDEO
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class CameraUploads(Destroyable):
    pass
# WARNING: Decompyle incomplete

