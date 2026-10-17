# Source Generated with Decompyle++
# File: finderinfo.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import struct
from typing import Any, Optional, Text
from AppKit import NSURL, NSURLTagNamesKey
from pymac.constants import kHasCustomIcon
from dropbox.fsutil import fsutil
from dropbox.mac.internal import autoreleasepool
from dropbox.shared.local_path import LocalPath
FileSystem = Any
FINDER_INFO_XATTR_NAME = b'com.apple.FinderInfo'
TAGS_XATTR_NAME = b'com.apple.metadata:_kMDItemUserTags'
ICON_ENABLED_FLAG_BYTE_SIZE = 2
ICON_ENABLED_FLAG_BITMASK = kHasCustomIcon
ICON_ENABLED_FLAG_OFFSET = 8
LABEL_VALUE_FLAG_OFFSET = 9
FINDER_INFO_BLOB_BYTE_SIZE = 32
FINDER_INFO_TAG_TO_LABEL_MAP = {
    None: b'\x00',
    'Gray': b'\x02',
    'Green': b'\x04',
    'Purple': b'\x06',
    'Blue': b'\x08',
    'Yellow': b'\n',
    'Red': b'\x0c',
    'Orange': b'\x0e' }
FINDER_INFO_LABEL_TO_TAG_MAP = FINDER_INFO_TAG_TO_LABEL_MAP.items()()

class MacFinderInfoHelper(object):
    _replace_bytes_at_index = (lambda original = None, replacement = None, replacement_index = staticmethod: beginning = original[:replacement_index]end_index = replacement_index + len(replacement)end = original[end_index:]beginning + replacement + end)()
    load_or_create_finderinfo_xattr = (lambda fs = None, path = None: try:
attr = fsutil.get_attr(fs, path, 'mac', FINDER_INFO_XATTR_NAME)attrexcept IOError:
e = Noneif e.errno != errno.ENOENT:
raise e = Nonedel eexcept:
e = Nonedel ebytes(bytearray(FINDER_INFO_BLOB_BYTE_SIZE)))()
    _extract_finderinfo_xattr_icon_flag = (lambda attr = None: chunk = attr[ICON_ENABLED_FLAG_OFFSET:ICON_ENABLED_FLAG_OFFSET + ICON_ENABLED_FLAG_BYTE_SIZE]struct.unpack('>H', chunk)[0])()
    change_icon_bit_in_xattr = (lambda attr = None, set_on = None: value = MacFinderInfoHelper._extract_finderinfo_xattr_icon_flag(attr)if set_on:
value = ICON_ENABLED_FLAG_BITMASK | valueelse:
value = value & ~ICON_ENABLED_FLAG_BITMASKchunk = struct.pack('>H', value)MacFinderInfoHelper._replace_bytes_at_index(attr, chunk, ICON_ENABLED_FLAG_OFFSET))()
    is_finderinfo_custom_icon_enabled = (lambda attr = None: value = MacFinderInfoHelper._extract_finderinfo_xattr_icon_flag(attr)value & ICON_ENABLED_FLAG_BITMASK == ICON_ENABLED_FLAG_BITMASK)()
    get_finderinfo_label_color = (lambda attr = None: color_value = attr[LABEL_VALUE_FLAG_OFFSET:LABEL_VALUE_FLAG_OFFSET + 1]FINDER_INFO_LABEL_TO_TAG_MAP.get(color_value))()
    set_finderinfo_label_color = (lambda attr = None, color = None: color_value = FINDER_INFO_TAG_TO_LABEL_MAP.get(color, FINDER_INFO_TAG_TO_LABEL_MAP[None])MacFinderInfoHelper._replace_bytes_at_index(attr, color_value, LABEL_VALUE_FLAG_OFFSET))()
    synchronize_finderinfo_label = (lambda fs = None, path = None: if fsutil.exists(fs, path):
autoreleasepool()color = Noneurl = NSURL.fileURLWithPath_(path.to_unicode())res = url.getResourceValue_forKey_error_(None, NSURLTagNamesKey, None)if res and len(res) == 3 and res[1]:
for tag in res[1]:
if tag in FINDER_INFO_TAG_TO_LABEL_MAP:
color = taginfo = MacFinderInfoHelper.load_or_create_finderinfo_xattr(fs, path)label = MacFinderInfoHelper.get_finderinfo_label_color(info)if color != label:
info = MacFinderInfoHelper.set_finderinfo_label_color(info, color)fsutil.set_attr(fs, path, 'mac', FINDER_INFO_XATTR_NAME, info)None(None, None)Nonewith None:
if not None:
passNone)()

