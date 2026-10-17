# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dataclasses import dataclass
from typing import NamedTuple, Optional, Text

class ContactType(object):
    group = 'group'
    email = 'email'

Contact = NamedTuple('Contact', [
    ('display_name', Text),
    ('contact_value', Text),
    ('contact_type', ContactType),
    ('is_same_team', Optional[bool]),
    ('photo_url', Optional[Text]),
    ('dropbox_id', Optional[Text]),
    ('member_count', Optional[int]),
    ('is_member', Optional[bool]),
    ('sort_key', Text)])
ContactLocalMetadata = <NODE:12>()
Contact.__new__.__defaults__ = (None,) * len(Contact._fields)
