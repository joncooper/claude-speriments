# Source Generated with Decompyle++
# File: photoimporter.pyc (Python 3.11)

import collections
import datetime
import errno
import itertools
import operator
import os
import pprint
import re
import struct
import threading
import time
from contextlib import contextmanager
from hashlib import md5
from typing import Any, Callable, cast, Dict, IO, Iterable, Iterator, List, Optional, Set, Text, Tuple, TypeVar
from six import iteritems
from six.moves import filter as ifilter, range, zip as izip
from dropbox.fsutil import fsutil
from dropbox.build_common import get_build_number
from dropbox.camera import Device, PhotoDetails, PhotoImportCanceled, PhotoImportDeviceLocked, PhotoImportDisconnected, PhotoImportExceptionBase, PhotoImportLowDropboxSpace, PhotoImportPhotoFailedToImport, PhotoImportSelectiveSync
from dropbox.camera.filetypes import mp4_video, video
from dropbox.camera.util import is_apple_device
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.camera_upload_metric_logger import MetricsLogger
from dropbox.client.camera_upload.photo_constants import DEFAULT_UPLOAD_LOCATION
from dropbox.client.flow_tracker import BlockingFlow
from dropbox.client.status.label import StatusLabel
from dropbox.client.util import get_platform_info
from dropbox.client_api.hashing import BetterDropboxHasher, DROPBOX_MAX_BLOCK_SIZE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import LowDiskSpaceError
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes, make_str
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.metadata.metadata import EXIF_CUSTOMRENDERED, EXIF_DATETIME, EXIF_HEIFSIG, EXIF_IMAGE_MAKE, EXIF_IMAGE_MODEL, EXIF_IMAGE_ORIENTATION, EXIF_LENGTH, EXIF_THUMBNAIL, EXIF_WIDTH, get_exif_metadata, PHOTO_EXIF_WHITELIST
from dropbox.metadata.mp4_parser import MoovSkimmer
from dropbox.metrics.camera_upload import CameraEvent, CameraExtraMetric
from dropbox.native_event import AutoResetEvent
from dropbox.observable import Observable, ObservableIterator, ObservableList
from dropbox.platform import IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.types import AdditionalAttributes
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.threading import RLock
from dropbox.timehelper import tz_offset_string
from dropbox.trace import reraise_exc_handler, TRACE
if IS_WINDOWS:
    from dropbox.client.photodownloader.win.helpers import is_disconnected_error
MYPY = False
if MYPY:
    from typing import Deque
    from dropbox.client.camera_upload.camera_handler import SessionContext
    from dropbox.client.camera_upload.photouploader import PhotoUploader
    from dropbox.client.main import DropboxApplication
IMPORT_FREE_SPACE_BUFFER = 52428800
CU_HASH_8_BYTES = 8192
NUM_READ_RETRIES = 10
XATTR_EXIF_MANUFACTURER = 'exif_manufacturer'
XATTR_EXIF_MODEL = 'exif_model'
XATTR_EXIF_DATETIME = 'exif_datetime'
XATTR_DEVICE_MANUFACTURER = 'device_manufacturer'
XATTR_DEVICE_MODEL = 'device_model'
XATTR_DEVICE_NAME = 'device_name'
XATTR_DEVICE_UID = 'device_uid'
XATTR_DEVICE_SERIALNUM = 'device_serialnum'
XATTR_CLIENT_IMPORT_TIME = 'client_import_time'
XATTR_CLIENT_PLATFORM = 'client_platform'
XATTR_CLIENT_BUILDSTRING = 'client_buildstring'
XATTR_CLIENT_USERID = 'client_userid'
XATTR_CLIENT_TIMEOFFSET = 'client_timeoffset'
XATTR_FILE_DATETIME = 'file_datetime'
XATTR_FILE_HASHFULL = 'file_hashfull'
XATTR_FILE_NAMEORIG = 'file_nameorig'
CAMERA_XATTRS = [
    XATTR_EXIF_MANUFACTURER,
    XATTR_EXIF_MODEL,
    XATTR_EXIF_DATETIME,
    XATTR_DEVICE_MANUFACTURER,
    XATTR_DEVICE_MODEL,
    XATTR_DEVICE_NAME,
    XATTR_DEVICE_UID,
    XATTR_DEVICE_SERIALNUM,
    XATTR_CLIENT_IMPORT_TIME,
    XATTR_CLIENT_PLATFORM,
    XATTR_CLIENT_BUILDSTRING,
    XATTR_CLIENT_USERID,
    XATTR_CLIENT_TIMEOFFSET,
    XATTR_FILE_DATETIME,
    XATTR_FILE_HASHFULL]
CAMERA_XATTRS_PLAT = 'dropbox_camera_upload'
XATTR_COLLECTION_GIDS = 'collection_gids'
COLLECTION_XATTRS_PLAT = 'dropbox_collection_gid'
PHOTOIMPORT_EXCEPTIONS_RERAISE = (PhotoImportExceptionBase, LowDiskSpaceError)
EXIF_TO_CAMERA_ATTR = {
    EXIF_DATETIME: XATTR_EXIF_DATETIME,
    EXIF_IMAGE_MODEL: XATTR_EXIF_MODEL,
    EXIF_IMAGE_MAKE: XATTR_EXIF_MANUFACTURER }
EXIF_DATETIME_STRPTIME_FMTS = [
    '%Y:%m:%d %H:%M:%S',
    '%Y:%m:%d:%H:%M:%S',
    '%Y:%m:%d %I:%M:%S %p']
MYSTERIOUS_QUELEA_FILE_SIZE = 4194304
_T = TypeVar('_T')
ByBasenameType = List[Tuple[(Text, List['PhotoDetails'])]]
ByTimestampType = List[ByBasenameType]

def parse_exif_datetime(data = None, strptime_fn = None):
    normalized_data = make_str(data).replace('/', ':').replace('-', ':').replace('.', '')
    for i, pattern in enumerate(EXIF_DATETIME_STRPTIME_FMTS):
        
        return None, strptime_fn(normalized_data, pattern)
        except ValueError:
            if i == len(EXIF_DATETIME_STRPTIME_FMTS) - 1:
                raise 
            continue
        raise ValueError


def _nexus_datetime_from_path(taken_at = None, path = None):
