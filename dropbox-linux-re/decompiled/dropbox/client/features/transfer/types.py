# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, NewType, Optional, Text, TypedDict
FileTransfersApiResponse = Dict[(Text, Any)]
ApiFileId = NewType('ApiFileId', Text)
TRANSFER_API_BAIL_ERRORS = [
    'no_permission_error']
TransferSettings = <NODE:12>()

class FileAddSource(Enum):
    DRAG_DROP = 0
    DROPBOX_CHOOSER_ADDITIONAL = 1
    DROPBOX_CHOOSER_INITIAL = 2
    UPLOAD_BUTTON_ADDITIONAL = 3
    UPLOAD_BUTTON_INITIAL = 4
    DESKTOP_CONTEXT_MENU = 5
    COLLAB_BROWSE = 6


class UpsellVariables(TypedDict):
    send_size_limit: 'int' = 'UpsellVariables'


class ProductConfigConstants(TypedDict):
    premium_upsell_variables: 'Optional[UpsellVariables]' = 'ProductConfigConstants'


class ProductConfig(TypedDict):
    features: 'Optional[Dict[str, bool]]' = 'ProductConfig'


class UserMetadata(TypedDict):
    should_notify_creator_on_download: 'bool' = 'UserMetadata'

