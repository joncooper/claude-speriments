# Source Generated with Decompyle++
# File: extension_whitelist.pyc (Python 3.11)

from enum import Enum
from typing import NamedTuple, Text
from dropbox.client.cloud_docs.extension_constants import LOGGING_WHITELISTED_EXTS

class ExtensionType(Enum):
    NO_EXTENSION = 0
    EXTENSION_IN_WHITELIST = 1
    EXTENSION_NOT_IN_WHITELIST = 2

ExtensionData = NamedTuple('ExtensionData', [
    ('whitelisted_extension', Text),
    ('extension_type', ExtensionType)])

def get_whitelisted_extension(filename = None):
    filename_parts = filename.split('.')
# WARNING: Decompyle incomplete

