# Source Generated with Decompyle++
# File: file_validator.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import os
from builtins import open as _builtin_open
from concurrent.futures import TimeoutError
from typing import Any, Dict, Optional, Text, Tuple, Union
from six.moves.urllib.parse import ParseResult, urlparse
from extension_constants import CLOUD_DOC_EXTS, CLOUD_ENHANCED_EXTS, SHORTCUT_CLOUD_DOC_EXTS
from opener_utils import EXTENSION_TO_OPEN_INFO
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.cloud_docs.constants import CLOUD_DOC_URL_PATH_PREFIX, CloudDocsUrlType, CloudDocsValidationErrorCode, MAX_CLOUD_DOCS_FILE_SIZE, MAX_CLOUD_DOCS_RECALL_TIME
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.platform import IS_MAC
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.url_info import dropbox_url_info

class CloudDocsValidationException(Exception):
    pass
# WARNING: Decompyle incomplete


def is_cloud_docs_extension(local_path = None):
    return os.path.splitext(Text(local_path))[1] in CLOUD_DOC_EXTS


def _is_cloud_doc_nucleus(nucleus_client = None, path = None):
    local_path = path if isinstance(path, LocalPath) else nucleus_client.file_system.make_path(path)
    props = nucleus_client.lookup_properties_by_local_path(local_path).block().result()
# WARNING: Decompyle incomplete


def is_cloud_doc(sync_engine_info = None, path = None):
    if not is_cloud_docs_extension(path):
        return False
    
    try:
        if isinstance(sync_engine_info, NucleusInterface):
            is_cloud_content = _is_cloud_doc_nucleus(sync_engine_info, path)
        elif isinstance(sync_engine_info, SyncEngineClassicInterface):
            is_cloud_content = sync_engine_info.is_cloud_content(sync_engine_info.file_system.make_path(path))
        else:
            (account, sync_engine_adapter) = sync_engine_info
            local_path = sync_engine_adapter.file_system.make_path(path)
            if not account:
                (account, _) = sync_engine_adapter.get_account_for_path(local_path)
            if account:
                api = sync_engine_adapter.nucleus_api(account)
                if api:
                    is_cloud_content = _is_cloud_doc_nucleus(api, local_path)
                else:
                    is_cloud_content = False
            else:
                is_cloud_content = False
    except FileNotFoundError:
        return True

    return is_cloud_content


def is_cloud_enhanced_doc(path = None):
    return os.path.splitext(Text(path))[1] in CLOUD_ENHANCED_EXTS


def is_shortcut(path = None):
    return os.path.splitext(Text(path))[1] in SHORTCUT_CLOUD_DOC_EXTS


def _fp_ensure_available(path = None):
    pass
# WARNING: Decompyle incomplete


def validate_cloud_doc(path = None, wrapper = None):
    pass
# WARNING: Decompyle incomplete


def _get_url_type(parsed_url = None):
    if parsed_url.netloc == dropbox_url_info.webserver_host:
        if parsed_url.path.startswith(CLOUD_DOC_URL_PATH_PREFIX):
            return CloudDocsUrlType.DROPBOX_CLOUD_DOC
        return None.DROPBOX_UNKNOWN
    if _netloc_ends_with(parsed_url.netloc, 'dev.corp.dropbox.com') and parsed_url.path.startswith(CLOUD_DOC_URL_PATH_PREFIX):
        return CloudDocsUrlType.DROPBOX_DEV_CLOUD_DOC
    if _netloc_ends_with(parsed_url.netloc, 'dropbox.com'):
        return CloudDocsUrlType.DROPBOX_UNKNOWN
    return None.UNKNOWN


def _netloc_ends_with(netloc = None, suffix = None):
    netloc_parts = netloc.split('.')
    suffix_parts = suffix.split('.')
    return netloc_parts[-len(suffix_parts):] == suffix_parts

