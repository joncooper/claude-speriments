# Source Generated with Decompyle++
# File: stub_folder_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import struct
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite.exceptions import StubFolderDecodeError
from dropbox.shared.validated_record import Field, ValidatedRecord
from dropbox.trace import TRACE

class StubFolderDetails(ValidatedRecord):
    target_ns = Field.required(int)
    user_id = Field.required(int)
    
    def encode(self = None):
        return self.encode_v2()

    
    def encode_v2(self = None):
        json_blob = json.dumps({
            'target_ns': self.target_ns,
            'user_id': self.user_id }).encode('utf-8')
        return struct.pack('<IQ', 2, self.user_id) + json_blob

    decode = (lambda data = None: try:
(version,) = struct.unpack_from('<I', data)if version == 2:
json_blob = data[12:].decode('utf-8')json_details = json.loads(json_blob)StubFolderDetails(target_ns = json_details['target_ns'], user_id = json_details['user_id'])raise TypeError('Invalid version found!')except Exception:
e = NoneTRACE('Invalid stub folder: %r', data)if isinstance(e, struct.error):
raise StubFolderDecodeError('Could not decode version: %s' % e)if isinstance(e, UnicodeDecodeError):
raise StubFolderDecodeError('Could not decode stub folder data')if isinstance(e, ValueError):
raise StubFolderDecodeError('Could not decode JSON data')if isinstance(e, (KeyError, TypeError)):
raise StubFolderDecodeError('Stub folder is malformed')report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UNKNOWN)raise StubFolderDecodeError('Unexpected error decoding')e = Nonedel e)()

