# Source Generated with Decompyle++
# File: installer_tag.pyc (Python 3.11)

from __future__ import absolute_import
import base64
import json
import zlib
from typing import Optional, Text
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.client.util.win.registry import get_registry_dealcode
legacy_from_websafe = bytes.maketrans(b'-_~', b'+/=')

def deserialize_tag_data(data = None):
    return zlib.decompress(base64.decodebytes(data.translate(legacy_from_websafe)))


class InstallerTag(object):
    DELIMS = {
        'id_marker': '@',
        'separator': '::',
        'preauth_info': 'DBPREAUTH',
        'dealcode': 'DBDEALCODE',
        'partner': 'DBPARTNER',
        'deals_source': 'DBDEALSSOURCE' }
    
    def __init__(self, tag_string):
        self._original_tag_str = tag_string
        self._browser = None
        self._command_line_dealcode = None
        self._partner = None
        self._deals_source = None
        self._registry_dealcode = None
        self._installer_id = None
        self._session_id = None
        self._plan_type = None
        self._tk_value = None
        self._encoded_data = ''
        if IS_WINDOWS:
            self._registry_dealcode = get_registry_dealcode()
        if not tag_string:
            return None
        (tag_string, sep, installer_id) = tag_string.partition(InstallerTag.DELIMS['id_marker'])
        if installer_id:
            self._installer_id = installer_id
        components = tag_string.split(InstallerTag.DELIMS['separator'])
        if InstallerTag.DELIMS['preauth_info'] in components:
            idx = components.index(InstallerTag.DELIMS['preauth_info'])
            components.pop(idx)
            if len(components) >= idx + 2:
                self._browser = components.pop(idx)
                self._encoded_data = components.pop(idx)
        if InstallerTag.DELIMS['dealcode'] in components:
            idx = components.index(InstallerTag.DELIMS['dealcode'])
            components.pop(idx)
            self._command_line_dealcode = components.pop(idx)
        if InstallerTag.DELIMS['partner'] in components:
            idx = components.index(InstallerTag.DELIMS['partner'])
            components.pop(idx)
            self._partner = components.pop(idx)
        if InstallerTag.DELIMS['deals_source'] in components:
            idx = components.index(InstallerTag.DELIMS['deals_source'])
            components.pop(idx)
            if len(components) > idx:
                self._deals_source = components.pop(idx)
        if not len(components) > 0 and self._encoded_data:
            self._encoded_data = components[-1]
    # WARNING: Decompyle incomplete

    browser = (lambda self: self._browser)()
    dealcode = (lambda self: 