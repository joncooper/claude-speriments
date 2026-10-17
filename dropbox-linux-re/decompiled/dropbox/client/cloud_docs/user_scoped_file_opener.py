# Source Generated with Decompyle++
# File: user_scoped_file_opener.pyc (Python 3.11)

import datetime
import os
import time
from typing import NamedTuple, Optional, Text
from apex.metrics import Metric
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.cloud_docs.constants import CLOUD_DOCS_PERF_METRICS_NAMESPACE, CloudDocsUrlType, CloudDocsValidationErrorCode, CloudEditor
from dropbox.client.cloud_docs.events import report_cloud_docs_open, report_cloud_docs_open_failure
from dropbox.client.cloud_docs.extension_constants import LOGGING_NONWHITELISTED_EXT_PLACEHOLDER, LOGGING_WHITELISTED_EXTS
from dropbox.client.cloud_docs.file_validator import CloudDocsValidationException, validate_cloud_doc
from dropbox.client.cloud_docs.opener_utils import extend_query_params
from dropbox.client.cloud_docs.utils import create_cloud_docs_metrics_reporter
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.file_activation.constants import FileOpenStage
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.flow_tracker import BlockingFlow
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import fileid_to_bytes
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import InvalidDropboxPathException, NonSyncingLocalPathException
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
OpenSuccessInfo = NamedTuple('OpenSuccessInfo', [
    ('version', int),
    ('url_type', CloudDocsUrlType)])

class UserScopedCloudDocsFileOpener(Destroyable):
    pass
# WARNING: Decompyle incomplete

