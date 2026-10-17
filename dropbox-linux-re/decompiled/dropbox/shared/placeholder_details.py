# Source Generated with Decompyle++
# File: placeholder_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import struct
from typing import Any, Dict, Iterator, Tuple
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.functions import make_bytes, make_unicode
from dropbox.infinite.exceptions import InfinitePlaceholderDecodeError, NucleusPlaceholderError
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord
from dropbox.trace import TRACE

class PlaceholderDetails(ValidatedRecord):
    ns = Field.required(int)
    sjid = Field.required(int)
    user_id = Field.required(int)
    fileid = Field.optional(BaseString)
    fileid_rev = Field.optional(int)
    
    def __eq__(self = None, other = None):
        if type(self) != type(other):
            return False
        return dict(self.__iter_without_fileid()) == dict(other.__iter_without_fileid())

    
    def __hash__(self = None):
        return hash(frozenset(self.__iter_without_fileid()))

    
    def __iter_without_fileid(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def encode(self = None, require_fileid = None):
        return self.encode_v2(require_fileid)

    
    def encode_v2(self = None, require_fileid = None):
        pass
    # WARNING: Decompyle incomplete

    decode = (lambda data = None: pass# WARNING: Decompyle incomplete
)()


class NucleusPlaceholderDetails(ValidatedRecord):
    data = Field.required(bytes)
    
    def __eq__(self = None, other = None):
        if type(self) != type(other):
            return False
        return None.data == other.data

    
    def __hash__(self = None):
        raise NotImplementedError()

    
    def encode(self = None):
        return self.data

    decode = (lambda data = None: try:
(version,) = struct.unpack_from('<I', data)if version == 3:
NucleusPlaceholderDetails(data = data)if None == 2:
raise InfinitePlaceholderDecodeError('Not a Nucleus placeholder!')raise InfinitePlaceholderDecodeError('Invalid version found!')except Exception:
e = NoneTRACE('Invalid infinite placeholder: %r, %r', data, e)if isinstance(e, struct.error):
raise InfinitePlaceholderDecodeError('Could not decode version: %s' % e)if isinstance(e, InfinitePlaceholderDecodeError):
raise report_exception(component = DesktopComponent.UNKNOWN)raise InfinitePlaceholderDecodeError('Unexpected error decoding')e = Nonedel e)()

