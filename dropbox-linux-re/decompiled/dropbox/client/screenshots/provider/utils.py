# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import subprocess
from build_number import IS_MAC
from dropbox.trace import TRACE

def set_mac_screenshot_thumbnails(enable = None):
    if not IS_MAC:
        TRACE('SCREENSHOTS: set_mac_screenshot_thumbnails is not supported for Windows')
        return None
    
    try:
        subprocess.run([
            '/usr/bin/defaults',
            'write',
            'com.apple.screencapture',
            'show-thumbnail',
            '-bool',
            'true' if enable else 'false'], check = True)
        TRACE('Screenshot thumbnail preview set to %s', 'enabled' if enable else 'disabled')
        return None
    except subprocess.CalledProcessError:
        e = None
        TRACE('An error occurred: %s', e)
        e = None
        del e
        return None
        e = None
        del e


