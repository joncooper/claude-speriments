# Source Generated with Decompyle++
# File: fileids.pyc (Python 3.11)

from __future__ import absolute_import
import base64
import os
from typing import Dict, Optional, Text, Union
from dropbox.functions import make_unicode
from dropbox.model.types import FileId
from dropbox.shared.validated_record import BaseString
FILE_ID_PLAT = 'dropbox_fileid_local'
FILE_ID_MACHINE_ATTR = 'machineid_attr'

def new_fileid_xattr():
    return base64.b64encode(os.urandom(16))


def extra_attrs_from_fileid_xattr(attr = None):
    return {
        FILE_ID_PLAT: {
            FILE_ID_MACHINE_ATTR: {
                'data': make_unicode(attr) } } }


def map_fileid_to_ascii(fileid = None):
    pass
# WARNING: Decompyle incomplete

