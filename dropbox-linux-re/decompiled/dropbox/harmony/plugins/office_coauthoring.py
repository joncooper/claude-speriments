# Source Generated with Decompyle++
# File: office_coauthoring.pyc (Python 3.11)

from build_number import BuildVersion
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.harmony.models.types import ApplicationID
from dropbox.harmony.window_tracking.supported_applications import harmony_supported_apps
if IS_MAC:
    COAUTHORING_MINIMUM_VERSION = '16.60.410'
elif IS_WINDOWS:
    COAUTHORING_MINIMUM_VERSION = '16.0.17029.20068'

def application_supports_coauthoring(app_id = None, version = None):
    if not IS_MAC and IS_WINDOWS:
        return False
# WARNING: Decompyle incomplete

