# Source Generated with Decompyle++
# File: error_tuple.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, NamedTuple, Optional, Text
ErrorUserAction = NamedTuple('ErrorUserAction', [
    ('label', Text),
    ('url', Optional[Text])])
ErrorUserAction.__new__.__defaults__ = ('', None)
ErrorTuple = NamedTuple('ErrorTuple', [
    ('msg', Optional[Text]),
    ('is_msg_generic', Optional[bool]),
    ('is_transient_error', Optional[Text]),
    ('title', Optional[Text]),
    ('icon', Optional[Text]),
    ('actions', Optional[List[ErrorUserAction]])])
ErrorTuple.__new__.__defaults__ = (None,) * len(ErrorTuple._fields)
