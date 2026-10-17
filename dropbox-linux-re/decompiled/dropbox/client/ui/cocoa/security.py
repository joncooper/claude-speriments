# Source Generated with Decompyle++
# File: security.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import binascii
import hashlib
from macffi.CoreFoundation import CFDataCreate, CFEqual
from macffi.Security import SecCertificateCopySerialNumber, SecCertificateCreateWithData, SecTrustEvaluate, SecTrustGetCertificateAtIndex, SecTrustSetAnchorCertificates
from macffi_native import lib
from dropbox.nts import cert_pinning_disabled
from dropbox.ssl.revoked_certs import REVOKED_SNS
from dropbox.ssl.root_certs import root_certs, root_certs_digest, root_certs_list
if hashlib.sha256(root_certs).hexdigest() != root_certs_digest:
    raise AssertionError(f'''root certs integrity check failed: expected {root_certs_digest!r} got {hashlib.sha256(root_certs).hexdigest()!r}''')
_ROOT_CERTIFICATES = None

def validate_trust(trust_ref):
    pass
# WARNING: Decompyle incomplete


def _load_root_certificates():
    certs = []
# WARNING: Decompyle incomplete


def _is_certificate_revoked(trust_ref):
    certificate = SecTrustGetCertificateAtIndex(trust_ref, 0)
# WARNING: Decompyle incomplete

