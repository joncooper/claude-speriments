# Source Generated with Decompyle++
# File: link_util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Text

def get_link_type_from_url(url = None):
    if '/scl/' in url:
        return 'SHARED_CONTENT_LINK'

