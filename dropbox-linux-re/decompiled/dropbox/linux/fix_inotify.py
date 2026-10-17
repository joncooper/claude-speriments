# Source Generated with Decompyle++
# File: fix_inotify.pyc (Python 3.11)

from __future__ import absolute_import
import os
import tempfile
import textwrap
from dropbox.functions import make_bytes
from dropbox.linux.sysctl import get_sysctl_values, SysctlParser
from dropbox.platform import IS_LINUX
if IS_LINUX:
    from dropbox.client.system_authorization.linux import request_authorization_from_user_and_run
SYSCTL_FILE_PATH = '/etc/sysctl.d/30-dropbox.conf'
MIN_MAX_USER_INSTANCES = 256
MIN_MAX_USER_WATCHES = 100000

def fix_inotify():
    if not IS_LINUX:
        raise NotImplementedError()
    new_max_user_instances = None
    new_max_user_watches = None
    (max_user_instances, max_user_watches) = get_sysctl_values('fs.inotify.max_user_instances', 'fs.inotify.max_user_watches')()
    if max_user_instances < MIN_MAX_USER_INSTANCES:
        new_max_user_instances = MIN_MAX_USER_INSTANCES
    if new_max_user_watches or new_max_user_instances:
        sysctl_file = SysctlParser()
        if new_max_user_watches:
            sysctl_file.set('fs.inotify.max_user_watches', new_max_user_watches)
        if new_max_user_instances:
            sysctl_file.set('fs.inotify.max_user_instances', new_max_user_instances)
        sysctl_string = str(sysctl_file)
        script = tempfile.NamedTemporaryFile()
        script.write(make_bytes(textwrap.dedent('\n                #!/bin/sh -e\n                cat <<EOF > {sysctl}\n                {sysctl_string}\n                EOF\n                /sbin/sysctl -p {sysctl}').format(sysctl = SYSCTL_FILE_PATH, sysctl_string = sysctl_string)).strip())
        script.flush()
        request_authorization_from_user_and_run('sh', [
            script.name])
        None(None, None)
        return None
    with None:
        if not None if max_user_watches < MIN_MAX_USER_WATCHES else (lambda .0: pass# WARNING: Decompyle incomplete
):
            pass
    return None

