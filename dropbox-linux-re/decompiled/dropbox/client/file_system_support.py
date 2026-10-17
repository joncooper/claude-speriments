# Source Generated with Decompyle++
# File: file_system_support.pyc (Python 3.11)

import os
import sys
from typing import Dict, Optional, Text
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric, SimpleMetricCategoryWhitelist
from dropbox.client.util import fs_supports_attrs, get_fs_type
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
if IS_MAC:
    SUPPORTED_FS_NAMES = {
        'apfs',
        'hfs'}
elif IS_WINDOWS:
    SUPPORTED_FS_NAMES = {
        'ntfs'}
elif IS_LINUX:
    SUPPORTED_FS_NAMES = {
        'ext4'}
    SUPPORTED_FS_NAMES.update({
        'btrfs',
        'ecryptfs'})
    if sys.maxsize > 0x100000000:
        SUPPORTED_FS_NAMES.add('zfs')
        SUPPORTED_FS_NAMES.add('xfs')
FILE_SYSTEM_SUPPORT_EVENT_ALLOWED_KEYS = {
    'fs_supported',
    'exception_type',
    'xattr_supported',
    'detected_fs_type',
    'overall_supported'}

class UnsupportedFSDetectionMissingFolder(Exception):
    pass


class UnsupportedFSDetectionUnknownFSType(Exception):
    pass


def report_file_system_support_event(event_name = None, extra = None):
    if not extra:
        extra = { }
        if not set(extra.keys()).issubset(FILE_SYSTEM_SUPPORT_EVENT_ALLOWED_KEYS):
            report_bad_assumption('Invalid keys for fs eos event')
    report('filesystem-support', event = event_name, extra = sanitize_event_extra_dict(extra))


def _get_existing_current_or_parent_path(path = None):
    if os.path.exists(path):
        return path
    parent_path = None.path.dirname(path)
    if os.path.exists(parent_path):
        TRACE('[fs type] Using parent folder for detection since %s does not exist', path)
        return parent_path
    TRACE('[fs type] Cannot find existing folder or parent folder on %s', path)


def is_supported_fs_type(path = None, should_enforce_xattr = None):
    TRACE('[Unsupported FS] Checking is_supported for path: %s', path)
    fs_supported = True
    xattr_supported = True
    fs_name = None
    exception = None
# WARNING: Decompyle incomplete

