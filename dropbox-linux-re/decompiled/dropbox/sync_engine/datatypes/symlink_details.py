# Source Generated with Decompyle++
# File: symlink_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
from typing import Any, Dict, Text
from dropbox.exception.exception_decorators import handle_exceptions_ex_2
from dropbox.functions import EitherStr, make_unicode
from dropbox.shared.validated_record import Field, ValidatedRecord

class SymlinkDetails(ValidatedRecord):
    target = Field.required(Text)
    target_root_relative_path = Field.optional(Text)
    
    def validate(self = None):
        pass

    from_dict = (lambda cls = None, symlink_details_dict = None: SymlinkDetails(target = symlink_details_dict['target'], target_root_relative_path = symlink_details_dict['target_root_relative_path']))()
    
    def to_dict(self = None):
        symlink_details_dict = {
            'target': self.target,
            'target_root_relative_path': self.target_root_relative_path }
        return symlink_details_dict

    
    def marshal(self = None):
        as_dict = self.to_dict()
        return json.dumps(as_dict)

    unmarshal = (lambda cls = None, buf = None: as_dict = json.loads(make_unicode(buf))cls.from_dict(as_dict))()
    __conform__ = (lambda self = None, protocol = None: self.marshal())()

