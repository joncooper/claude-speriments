# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import time
from dataclasses import asdict
from enum import Enum
from typing import Any, Dict, List, NamedTuple, Optional, Text
from six import iteritems
from dropbox.client.cloud_docs.constants import CloudDocsEventName, CloudDocsFileLocation, CloudDocsOpenFailureReason, CloudDocsUrlType, CloudDocsWindowsInstallationStatus
from dropbox.client.cloud_docs.extension_constants import LOGGING_NONWHITELISTED_EXT_PLACEHOLDER, LOGGING_WHITELISTED_EXTS
from dropbox.client.cloud_docs.file_validator import CloudDocsValidationException, is_cloud_doc, validate_cloud_doc
from dropbox.client.cloud_docs.locations import get_path_location
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.product_span import ProductSpan
from dropbox.event import report
from dropbox.foundation.native_file_opener.open_with import get_associated_applications
from dropbox.sync_engine_boundary.exceptions import UnsyncablePathError
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
CloudDocsFileInfo = NamedTuple('CloudDocsFileInfo', [
    ('location', CloudDocsFileLocation),
    ('extension', Text),
    ('version', int),
    ('url_type', CloudDocsUrlType),
    ('file_size', Optional[int]),
    ('is_cloud_doc', bool),
    ('default_app', Optional[Text]),
    ('associated_apps', List[Text]),
    ('path_drive', Text)])

def _get_cloud_docs_file_info(nucleus_wrapper = None, file_path = None, version = None, url_type = (None, None, True), should_read_version = ('nucleus_wrapper', 'Optional[NucleusInterface]', 'file_path', 'Text', 'version', 'Optional[int]', 'url_type', 'Optional[CloudDocsUrlType]', 'should_read_version', 'bool', 'return', 'CloudDocsFileInfo')):
    pass
# WARNING: Decompyle incomplete


def _report_cloud_docs_event(event_name = None, file_info = None, extra = None):
    file_info_dict = { }
# WARNING: Decompyle incomplete


def report_cloud_docs_open(nucleus_wrapper, file_path = None, version = None, url_type = None, open_info = (None,), extra = ('nucleus_wrapper', 'Optional[NucleusInterface]', 'file_path', 'Text', 'version', 'int', 'url_type', 'CloudDocsUrlType', 'open_info', 'FileOpenInfo', 'extra', 'Optional[Dict[Text, Any]]', 'return', 'None')):
    file_info = _get_cloud_docs_file_info(nucleus_wrapper, file_path, version = version, url_type = url_type)
# WARNING: Decompyle incomplete


def report_cloud_docs_open_failure(nucleus_wrapper = None, file_path = None, reason = None, open_info = (None,), extra = ('nucleus_wrapper', 'Optional[NucleusInterface]', 'file_path', 'Text', 'reason', 'CloudDocsOpenFailureReason', 'open_info', 'FileOpenInfo', 'extra', 'Optional[Dict[Text, Any]]', 'return', 'None')):
    file_info = _get_cloud_docs_file_info(nucleus_wrapper, file_path, should_read_version = False)
# WARNING: Decompyle incomplete


def report_windows_installation_status(status = None):
    report('cloud_docs', event_name = CloudDocsEventName.WINDOWS_INSTALL.value, extra = dict(is_installed = Text(status in (CloudDocsWindowsInstallationStatus.INSTALLED, CloudDocsWindowsInstallationStatus.REPAIRED)), status = status.value))

