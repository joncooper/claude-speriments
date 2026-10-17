# Source Generated with Decompyle++
# File: client_key_pair.pyc (Python 3.11)

import base64
import dataclasses
import json
from stone.backends.python_rsrc.stone_serializers import json_decode, json_encode
from dropbox.api.v2.datatypes.ekms import AsymmetricEncryptionAlgorithm, AsymmetricEncryptionAlgorithm_validator
from dropbox.client.features.encrypted_folder.fingerprint import KeyFingerprint
from dropbox.proto.nucleus.sync_engine_pb2 import SyncEngineCreateArgs
ClientKeyPair = <NODE:12>()
