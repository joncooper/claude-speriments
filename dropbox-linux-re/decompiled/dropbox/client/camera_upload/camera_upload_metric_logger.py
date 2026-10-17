# Source Generated with Decompyle++
# File: camera_upload_metric_logger.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Any, Dict, Optional, Text
from dropbox import event_names
from dropbox.camera import CameraFileLogger, CameraSessionLogger, Device, File, PhotoDetails
from dropbox.camera.filetypes import video
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.metadata import metadata
from dropbox.metrics.camera_upload import CameraDeviceMetric, CameraEvent, CameraExtraMetric
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.photodb import PendingPhoto
    from dropbox.client.camera_upload.session_context import SessionContext

class MetricsLogger(object):
    report_camera_event = (lambda event_name = None, session_context = None: 