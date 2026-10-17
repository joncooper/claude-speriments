# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum

class FileOpenStage(Enum):
    SYSTEM_STARTUP = 'system_startup'
    SYSTEM = 'system'
    CREATE = 'create'
    NATIVE_FILE_OPENER = 'native_file_opener'
    DEBUG = 'debug'
    DESKTOP_SHELL = 'desktop_shell'


class FileActivationError(Enum):
    SHORT_PATH_CONVERSION = 'short_path_conversion'

