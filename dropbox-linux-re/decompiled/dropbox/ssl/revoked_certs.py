# Source Generated with Decompyle++
# File: revoked_certs.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from build_number.legacy_crypto import dropbox_backend
from cryptography.x509 import load_der_x509_certificate

class RevokedCertificateException(Exception):
    pass

REVOKED_SNS = frozenset([
    0x275C76C1E643C2649886B0E763AC3E9,
    0x27AB71BA41865C,
    0x2B734779DB8012])

def check_revocation_status(cert_der = None):
    serial = load_der_x509_certificate(cert_der, dropbox_backend()).serial_number
    if serial in REVOKED_SNS:
        raise RevokedCertificateException('Certificate %s presented by the server is revoked' % serial)

