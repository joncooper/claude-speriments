# Source Generated with Decompyle++
# File: root_certs.pyc (Python 3.11)

import hashlib
from bazel_generated._root_certs import root_certs as root_certs_list
root_certs: 'bytes' = b''.join(root_certs_list)
root_certs_digest = '5567b61fc868cd2472cfe0708f0543195322adfe4efe0521696676a73a13db98'
if hashlib.sha256(root_certs).hexdigest() != root_certs_digest:
    raise AssertionError(f'''root certs integrity check failed: expected {root_certs_digest!r} got {hashlib.sha256(root_certs).hexdigest()!r}''')
