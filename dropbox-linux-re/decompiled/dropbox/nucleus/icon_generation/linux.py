# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List
from six import iteritems
from util import ICON_TYPE_MAP
from dropbox.proto.database.icons_pb2 import DBXIcon

def generate_icon_paths():
    return iteritems(ICON_TYPE_MAP)()

