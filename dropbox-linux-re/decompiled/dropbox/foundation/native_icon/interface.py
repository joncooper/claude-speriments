# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from __future__ import absolute_import
from abc import abstractmethod
from enum import Enum
from typing import Optional, Text

class ImageFormat(Enum):
    PNG = 'PNG'
    BMP = 'BMP'


class NativeIconLoaderInterface:
    get_file_icon_by_path = (lambda self = None, local_path = None, size = abstractmethod, scale_factor = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]'): pass)()
    get_file_icon_by_type = (lambda self = None, extension = None, size = abstractmethod, scale_factor = (ImageFormat.PNG,), format = ('extension', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]'): pass)()
    get_default_folder_icon = (lambda self = None, size = None, scale_factor = abstractmethod, format = (ImageFormat.PNG,): pass)()
    get_folder_icon_by_tag = (lambda self = None, tag = None, size = abstractmethod, scale_factor = (ImageFormat.PNG,), format = ('tag', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]'): pass)()
    get_file_thumbnail_by_path = (lambda self = None, local_path = None, size = abstractmethod, dropbox_feature_attribution = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'dropbox_feature_attribution', 'Text', 'format', 'ImageFormat', 'return', 'Optional[bytes]'): pass)()

