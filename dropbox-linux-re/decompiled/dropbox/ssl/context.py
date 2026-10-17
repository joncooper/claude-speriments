# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import hashlib
import ssl
from typing import Optional
from  import root_certs, ssl_policy
from dropbox.nts import cert_pinning_disabled
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threading import Lock

def _create_context():
    if hashlib.sha256(root_certs.root_certs).hexdigest() != root_certs.root_certs_digest:
        raise AssertionError(f'''root certs integrity check failed: expected {root_certs.root_certs_digest!r} got {hashlib.sha256(root_certs.root_certs).hexdigest()!r}''')
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
    if cert_pinning_disabled():
        load_default_certs_in_context(ctx)
# WARNING: Decompyle incomplete


def load_default_certs_in_context(ctx = None):
    if IS_WINDOWS:
        ctx.load_default_certs()
        return None
    if None:
        DBSecRetrieveTrustedCertificates = DBSecRetrieveTrustedCertificates
        import macffi.Security
        autoreleasepool = autoreleasepool
        import dropbox.mac.internal
        autoreleasepool()
        certs = DBSecRetrieveTrustedCertificates()
        None(None, None)
    else:
        with None:
            if not None:
                pass
# WARNING: Decompyle incomplete

_DROPBOX_SSL_CONTEXT: 'Optional[ssl.SSLContext]' = None
_DROPBOX_SSL_CONTEXT_LOCK = Lock()

def get_dropbox_ssl_context(force_new = None):
    pass
# WARNING: Decompyle incomplete

