# Source Generated with Decompyle++
# File: microsoft_store.pyc (Python 3.11)

from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from os import startfile as _startfile

def launch_microsoft_store():
    MS_STORE_CENTENNIAL_PRODUCT_DETAILS_PAGE = 'ms-windows-store://pdp/?ProductId=9NK4T08DHQ80'
    
    try:
        _startfile(MS_STORE_CENTENNIAL_PRODUCT_DETAILS_PAGE)
        return None
    except WindowsError:
        e = None
        report_app_framework_event_restricted('microsoft_store_launch_failed', error = e.__class__.__name__, error_msg = str(e))
        e = None
        del e
        return None
        e = None
        del e


