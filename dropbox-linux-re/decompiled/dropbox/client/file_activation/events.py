# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

import uuid
from dataclasses import dataclass, field
from typing import Text
from dropbox.client.file_activation.constants import FileOpenStage
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin

def _uuid_factory():
    return Text(uuid.uuid4())

FileOpenInfo = <NODE:12>()
