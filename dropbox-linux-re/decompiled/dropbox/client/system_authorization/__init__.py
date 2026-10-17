# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_LINUX, IS_MAC
if IS_LINUX:
    from dropbox.client.system_authorization.linux import request_authorization_from_user_and_run
    return None
if None:
    from macffi.Security import request_authorization_from_user_and_run
    return None
