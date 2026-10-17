# Source Generated with Decompyle++
# File: fp_dump.pyc (Python 3.11)

import dataclasses
import os
import subprocess
import tempfile
from datetime import datetime
from build_number.platform import IS_MAC
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.file_provider_logging.utils import FP_BUNDLE_ID, FP_DUMP_CATEGORY, FP_LOG_CATEGORY, LOG_PREDICATE, ls_dir_extra, parse_dump_for_import_errors, subproc_and_upload_as_log
from dropbox.client_api.exceptions import HTTPError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.proto.nucleus.app_service_pb2 import FileProviderDumpReq as FileProviderDumpReqProto
from dropbox.proto.nucleus.published_event_pb2 import FileProviderDumpRequestedEvent as FileProviderDumpRequestedEventProto
from dropbox.trace import TRACE

def file_provider_dump(account = None, request = None):
    if not IS_MAC:
        raise NotImplementedError('file provider dump is not supported on this platform')
    MAC_VERSION = MAC_VERSION
    VENTURA_13_3 = VENTURA_13_3
    import dropbox.mac.version
    request_id = request.id
    args = FileProviderDumpReqProto()
    args.id = request_id
    args.can_skip_import = False
# WARNING: Decompyle incomplete

