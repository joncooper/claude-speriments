# Source Generated with Decompyle++
# File: configuration_manager.pyc (Python 3.11)

from typing import Callable, Dict, Iterable, Optional, Set, Text, Tuple, Union
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, CameraExtraMetric, MetricsLogger
from dropbox.client.camera_upload.photo_constants import ENABLED_BY_ADMIN, FIRST_USE, OLD_PHOTO_ACTION
from dropbox.client.camera_upload.photodb import PhotoDb
from dropbox.client.camera_upload.types import CameraImportAction, CameraSplashResponse, CUDeviceUID
from dropbox.client.multiaccount.constants import Role
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event, Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2 import Destroyable
from dropbox.preferences import OPT_OPT_VIDEO_UNSYNCED, OPT_PHOTO, OPT_VIDEO
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.camera import Device
    from dropbox.client.camera_upload.camera_uploads import CameraUploadContext, CameraUploads
    from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
DeviceListing = Iterable[Tuple[(CUDeviceUID, Optional[Text], Optional[Role])]]

class CameraConfigurationManager(Destroyable):
    pass
# WARNING: Decompyle incomplete

