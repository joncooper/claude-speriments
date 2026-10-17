# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import
from enum import Enum
FILE_REQUEST_DESKTOP_CREATION_FEATURE = 'desktop-file-request-creation'
CREATE_FROM_DESKTOP_URL = 'requests/cfd'

class FileRequestInadequatePermissionsError(Exception):
    pass


class FileRequestEventType(Enum):
    FILE_REQUEST_ADD_MENU_ITEM_EXPOSED = 'file_request_add_menu_item_exposed'
    FILE_REQUEST_ADD_MENU_ITEM_CLICKED = 'file_request_add_menu_item_clicked'
    FILE_REQUEST_ADD_MENU_ITEM_FAILED = 'file_requestS_add_menu_item_failed'
    FILE_REQUEST_CB_ADD_MENU_ITEM_EXPOSED = 'file_request_cb_add_menu_item_exposed'
    FILE_REQUEST_CB_ADD_MENU_ITEM_CLICKED = 'file_request_cb_add_menu_item_clicked'
    FILE_REQUEST_CB_ADD_MENU_ITEM_FAILED = 'file_requestS_cb_add_menu_item_failed'

