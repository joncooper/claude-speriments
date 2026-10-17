# Source Generated with Decompyle++
# File: infinite_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
from enum import IntEnum
from typing import Any, Dict
from dropbox.exception.exception_decorators import handle_exceptions_ex_2
from dropbox.functions import EitherStr, make_unicode
from dropbox.shared.validated_record import Field, ValidatedRecord

class PlaceholderKind(IntEnum):
    ERRONEOUS = 0
    MAC_APFS_SPARSE_FILE = 1
    MAC_COMPRESSION_TYPE_3 = 3
    MAC_COMPRESSION_TYPE_5 = 5


class InfiniteDetails(ValidatedRecord):
    ns = Field.required(int)
    sjid = Field.optional(int)
    kind = Field.optional(PlaceholderKind)
    
    def validate(self = None):
        if self.ns <= 0:
            raise TypeError('Invalid ns: %d' % self.ns)
    # WARNING: Decompyle incomplete

    from_dict = (lambda cls = None, infinite_details_dict = None: creation_dict = { }creation_dict['ns'] = infinite_details_dict.get('ns')creation_dict['sjid'] = infinite_details_dict.get('sjid')creation_dict['kind'] = infinite_details_dict.get('kind')# WARNING: Decompyle incomplete
)()
    
    def to_dict(self = None):
        infinite_details_dict = { }
        infinite_details_dict['ns'] = self.ns
        infinite_details_dict['sjid'] = self.sjid
        infinite_details_dict['kind'] = self.kind
        return infinite_details_dict

    
    def marshal(self = None):
        as_dict = self.to_dict()
        return json.dumps(as_dict)

    unmarshal = (lambda cls = None, buf = None: as_dict = json.loads(make_unicode(buf))cls.from_dict(as_dict))()
    __conform__ = (lambda self = None, protocol = None: self.marshal())()
    
    def has_same_contents_as(self = None, other_details = None):
