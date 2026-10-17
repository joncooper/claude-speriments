# Source Generated with Decompyle++
# File: camera_upload_context.pyc (Python 3.11)

from typing import cast
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.photocontroller import CameraController
from dropbox.client.camera_upload.photodb import PhotoDb
from dropbox.client.camera_upload.photouploader import PhotoUploader
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import assert_not_none
from dropbox.foundation.raii2 import Destroyable
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.camera_uploads import CameraUploads
    from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
    from dropbox.client.photodownloader.base import PhotoDownloaderBase
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class CameraUploadContext(Destroyable):
    pass
# WARNING: Decompyle incomplete


class CameraUploadContextFactory(object):
    _build_photo_uploader = (lambda cls, camera_uploads = None, config_manager = None, account = classmethod, sync_engine_adapter = ('camera_uploads', 'CameraUploads', 'config_manager', 'ConfigurationManagerInterface', 'account', 'AccountInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'return', 'PhotoUploader'): local_config = config_manager.local_config(account)# WARNING: Decompyle incomplete
)()
    _build_controller = (lambda cls, camera_uploads, account = None, sync_engine_adapter = None, photo_downloader = classmethod, photo_uploader = ('camera_uploads', 'CameraUploads', 'account', 'AccountInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'photo_downloader', 'PhotoDownloaderBase', 'photo_uploader', 'PhotoUploader', 'return', 'CameraController'): CameraController(camera_uploads, account, sync_engine_adapter, photo_downloader, photo_uploader))()
    build = (lambda cls = None, camera_uploads = None, downloader = classmethod, account = ('camera_uploads', 'CameraUploads', 'downloader', 'PhotoDownloaderBase', 'account', 'AccountInterface', 'return', 'CameraUploadContext'): sync_engine_adapter = camera_uploads.get_app().sync_engine_adapter# WARNING: Decompyle incomplete
)()

