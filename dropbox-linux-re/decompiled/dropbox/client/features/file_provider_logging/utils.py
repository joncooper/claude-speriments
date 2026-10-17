# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import dataclasses
import gzip
import io
import itertools
import os
import re
import shutil
import subprocess
import time
from typing import Dict, IO, List, Optional, Set, Text, TextIO, Tuple
from build_number import BUILD_KEY
from dropbox.client.high_trace import unsafe_send_mac_log
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.proto.nucleus.app_service_pb2 import FileProviderDumpReq as FileProviderDumpReqProto
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import NSURL, NSURLDocumentIdentifierKey
    from macinfinite.xattr import fgetxattr
    from dropbox.mac.internal import autoreleasepool
    from dropbox.xattrs_posix import flistxattr, XATTR_SHOWCOMPRESSION
FP_DUMP_CATEGORY = 'fp_dump'
FP_LOG_CATEGORY = 'fp_log'
LOG_PREDICATE = '(subsystem == "com.apple.FileProvider") OR ((process == "DropboxFileProvider") AND (sender == "DropboxFileProvider"))'
FP_BUNDLE_ID = f'''com.getdropbox.{BUILD_KEY.lower()}.fileprovider'''
ReconciliationEntry = <NODE:12>()
ParsedDumpInfo = <NODE:12>()

def subproc_and_upload_as_log(f, category = None, cmd = dataclasses.dataclass, footer = dataclasses.dataclass, cmd_timeout = (None, None, None), upload_timeout = ('f', 'IO[bytes]', 'category', 'Text', 'cmd', 'List[Text]', 'footer', 'Optional[Text]', 'cmd_timeout', 'Optional[float]', 'upload_timeout', 'Optional[float]', 'return', 'Tuple[int, int]')):
    TRACE('Invoking "%s"', ' '.join(cmd))
    ts = time.time()
    subprocess.check_call(cmd, bufsize = 1, stdout = f, timeout = cmd_timeout)
# WARNING: Decompyle incomplete

KNOWN_ERRORS = [
    (FileProviderDumpReqProto.POSIX_EXTENDED_ATTRIBUTES_ERROR, 'pending', '.*NSError: POSIX 5.*'),
    (FileProviderDumpReqProto.POSIX_EPERM, 'pending', '.*NSError: POSIX 1.*'),
    (FileProviderDumpReqProto.FILE_PROVIDER_SQLITE_BOM_BUGGY, 'pending', '.*NSError: libfssync.Propagation<libfssync.VFSItem, __C.FPItem>.PropagationError.*')]

def _contains_known_ids(entries = None, ids = None):
    pass
# WARNING: Decompyle incomplete


def _categorize_dump_issue(import_type = None, throttled_imports = None, has_bom_error = None):
