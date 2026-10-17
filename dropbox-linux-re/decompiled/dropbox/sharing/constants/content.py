# Source Generated with Decompyle++
# File: content.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, NamedTuple, Optional, Text
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
_Content = NamedTuple('_Content', [
    ('mount_relative_server_path', Optional[MRCasedServerPath]),
    ('root_relative_server_path', Optional[RRCasedServerPath]),
    ('local_path', Optional[LocalPath]),
    ('api_id', Optional[Text]),
    ('link_api_id', Optional[Text]),
    ('type', Optional[Text]),
    ('content_name', Optional[Text]),
    ('is_in_team_folder', Optional[bool]),
    ('is_cloud_doc', Optional[bool])])
_Content.__new__.__defaults__ = (None,) * len(_Content._fields)

class Content(_Content):
    
    def __eq__(self = None, other = None):
