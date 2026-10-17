# Source Generated with Decompyle++
# File: folder_icon_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import collections
import os
import sys
from typing import Dict, Optional, Text
from AppKit import NSImage
from build_number import BUILD_KEY, is_frozen
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.util.mac import get_resources_dir
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import cached_property
from dropbox.mac.internal import autoreleasepool
from dropbox.mac.version import BIG_SUR, EL_CAPITAN, MAC_VERSION, MacVersion, YOSEMITE
FolderTagData = collections.namedtuple('FolderTagData', [
    'path',
    'filename'])

class FolderTagIconMappings(object):
    icon_assets_yosemite = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    icon_assets_elcapitan = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    icon_assets_bigsur = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def icon_asset_mapping(self = None, os_version = None):
        if os_version >= BIG_SUR:
            return self.icon_assets_bigsur
        if None >= EL_CAPITAN:
            return self.icon_assets_elcapitan
        return None.icon_assets_yosemite



def _get_local_types_path():
    if is_frozen() or hasattr(sys, 'dropbox_target'):
        return get_resources_dir()
    runfiles = None.environ.get('RUNFILES')
    if runfiles:
        return os.path.join(runfiles, 'desktop', 'images', '07_OS_Integration', 'mac')
    return f'''{BUILD_KEY}.app/Contents/Resources'''


class FolderTagIcon(object):
    LOCAL_TYPES_PATH = _get_local_types_path()
    tag_mapping: 'Optional[FolderTagIconMappings]' = None
    get_image_for_tag = (lambda tag = None, is_selsync = None: icon_path = FolderTagIcon._get_icon_path_for_tag(tag, is_selsync = is_selsync)# WARNING: Decompyle incomplete
)()
    _get_icon_path_for_tag_for_os = (lambda tag = None, os_version = None: pass# WARNING: Decompyle incomplete
)()
    _get_icon_path_for_tag = (lambda tag = None, is_selsync = None: version = MAC_VERSIONif is_selsync and version >= EL_CAPITAN:
if 'read_only' in tag or 'name_only' in tag:
version = YOSEMITEFolderTagIcon._get_icon_path_for_tag_for_os(tag, version))()

