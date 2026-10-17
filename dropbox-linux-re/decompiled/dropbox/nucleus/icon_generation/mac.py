# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Dict, List, Text
from six import iteritems
from util import ICON_TYPE_MAP
from dropbox.client.folder_tagger.folder_icon_mac import FolderTagData, FolderTagIconMappings
from dropbox.mac.version import MAC_VERSION
from dropbox.proto.database.icons_pb2 import DBXIcon

def generate_icon_paths():
    mappings = FolderTagIconMappings().icon_asset_mapping(MAC_VERSION)
    dbx_icons = []
# WARNING: Decompyle incomplete

