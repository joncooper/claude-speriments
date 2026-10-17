# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import division
import json
from dropbox.client.features.transfer.logger import AnalyticsExtra
from dropbox.client.features.transfer.types import FileAddSource
from dropbox.client.features.transfer.upload_manager import total_size
MYPY = False
if MYPY:
    from typing import Optional, Text

def file_source_logging_string(source = None):
    if source == FileAddSource.DRAG_DROP.value:
        return 'drag_drop'
    if None == FileAddSource.DROPBOX_CHOOSER_ADDITIONAL.value:
        return 'dropbox_chooser_additional'
    if None == FileAddSource.DROPBOX_CHOOSER_INITIAL.value:
        return 'dropbox_chooser_initial'
    if None == FileAddSource.UPLOAD_BUTTON_ADDITIONAL.value:
        return 'upload_button_additional'
    if None == FileAddSource.UPLOAD_BUTTON_INITIAL.value:
        return 'upload_button_initial'
    if None == FileAddSource.DESKTOP_CONTEXT_MENU.value:
        return 'desktop_context_menu'
    if None == FileAddSource.COLLAB_BROWSE.value:
        return 'collab_browse'


def build_feedback_url(transfer_id = None):
    pass
# WARNING: Decompyle incomplete


def build_view_url(transfer_id = None):
    return 'transfer/%s?referrer=desktop' % transfer_id


def build_manage_url(transfer_id = None):
    return 'transfer/manage?&referrer=desktop&transfer_id=%s' % transfer_id


def log_files_count_and_size_in_extra(all_files = None, extra_json = None):
    dropbox_files = list(filter((lambda f: f.src_dropbox_file_id is not None), all_files))
    extra = json.loads(extra_json) if extra_json else { }
    extra['dropbox_item_count'] = len(dropbox_files)
    extra['computer_item_count'] = len(all_files) - len(dropbox_files)
    extra['total_item_count'] = len(all_files)
    if 'transfer_size' not in extra:
        extra['transfer_size'] = total_size(all_files)
    return extra

