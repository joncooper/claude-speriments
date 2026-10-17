# Source Generated with Decompyle++
# File: key_crypto.pyc (Python 3.11)

from cryptography.hazmat.backends.openssl import backend as openssl_backend
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKeyWithSerialization, generate_private_key, SECP256R1
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat
from dropbox.api.v2.datatypes.ekms import AsymmetricEncryptionAlgorithm
from dropbox.client.features.encrypted_folder.client_key_pair import ClientKeyPair

def _generate_secp256k1_key_pair():
    private_eckey = generate_private_key(SECP256R1(), backend = openssl_backend)
# WARNING: Decompyle incomplete


def generate_key_pair():
    return _generate_secp256k1_key_pair()

