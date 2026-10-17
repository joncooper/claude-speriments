# Source Generated with Decompyle++
# File: fingerprint.pyc (Python 3.11)

import base64
import dataclasses
import json
from cryptography.hazmat.primitives import hashes
from stone.backends.python_rsrc.stone_serializers import json_encode
from dropbox.api.v2.datatypes.ekms import AsymmetricEncryptionAlgorithm, AsymmetricEncryptionAlgorithm_validator
from dropbox.client.features.encrypted_folder.base58 import encode_base58
from dropbox.proto.nucleus.sync_engine_pb2 import SyncEngineCreateArgs
KeyFingerprint = <NODE:12>()

class TeamKeyFingerprint(KeyFingerprint):
    deserialize = (lambda json_str = None: base_fingerprint = KeyFingerprint.deserialize(json_str)TeamKeyFingerprint(fingerprint = base_fingerprint.fingerprint, is_approved = base_fingerprint.is_approved))()
    
    def to_sync_engine_arg(self = None):
        return SyncEngineCreateArgs.TeamKeyFingerprint(fingerprint = self.fingerprint)


