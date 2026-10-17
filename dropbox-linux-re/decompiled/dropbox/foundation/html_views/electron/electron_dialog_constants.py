# Source Generated with Decompyle++
# File: electron_dialog_constants.pyc (Python 3.11)

from enum import Enum
from typing import Callable, List, NamedTuple, Optional, Text
from dropbox.foundation.futures.basic import EasyFuture

class DialogIconType(Enum):
    NONE = ''
    WARNING = 'warning'
    DROPBOX = 'dropbox'


class VisStyles(Enum):
    VIS2020 = 'vis2020'
    VIS2023 = 'vis2023'


class DialogArgs(NamedTuple):
    vis_style: 'Text' = 'DialogArgs'


class ElectronDialogCallbackInfo(NamedTuple):
    dropdown_selected: 'Optional[int]' = 'ElectronDialogCallbackInfo'


class DialogInfo(NamedTuple):
    button_id_future: 'Optional[EasyFuture[Optional[int]]]' = 'DialogInfo'


class QueuedDialogInfo(NamedTuple):
    dialog_info: 'DialogInfo' = 'QueuedDialogInfo'

