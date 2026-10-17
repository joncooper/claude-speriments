# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import subprocess
from build_number import IS_MAC, IS_WINDOWS
from build_number.platform import IS_LINUX
from dropbox.trace import TRACE
_COPY_IMAGE_ASCRIPT = '\non run argv\nset imagePath to item 1 of argv\nset the clipboard to (read (POSIX file imagePath) as «class PNGf»)\nend run\n'

def copy_image_to_clipboard(local_path = None):
    if IS_WINDOWS:
        TRACE('SCREENSHOTS: copy_image_to_clipboard is not supported for Windows')
        return None
    if None:
        subprocess.run([
            '/usr/bin/osascript',
            '-e',
            _COPY_IMAGE_ASCRIPT,
            '--',
            local_path])
        return None
    if None:
        subprocess.run([
            'xclip',
            '-selection',
            'clipboard',
            '-t',
            'image/png',
            '-i',
            local_path])
        return None

