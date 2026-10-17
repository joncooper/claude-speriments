# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

import json
import time
from typing import List, Text
import pywintypes
from dropbox.client.device_info import get_process_start_time
from dropbox.client.file_activation.constants import FileActivationError, FileOpenStage
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.file_activation.handler import FileActivationHandler
from dropbox.client.util.win import get_long_path
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.raii2 import Destroyable
from dropbox.trace import TRACE
from dropbox.win32.copy_data import create_copy_data_window, destroy_copy_data_window, find_copy_data_window, send_copy_data_message
COPYDATA_WND_CLASS = 'FileActivationHandler'

class WindowsFileActivationHelper(Destroyable):
    pass
# WARNING: Decompyle incomplete

