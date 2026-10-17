# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from dropbox.client.file_permissions.win import fix_perms_without_prompt_if_needed, show_perms
    return None
from dropbox.client.file_permissions.posix import fix_perms_without_prompt_if_needed, show_perms
