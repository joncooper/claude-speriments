# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from build_number.features import feature_enabled
from build_number.platform import IS_LINUX

def is_low_ui_mode():
    if not IS_LINUX:
        pass
    return not feature_enabled('electron-ui-kit')

