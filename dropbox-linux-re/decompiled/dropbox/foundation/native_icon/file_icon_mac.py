# Source Generated with Decompyle++
# File: file_icon_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from AppKit import NSBitmapImageRep, NSData, NSImage, NSMakeRect, NSPNGFileType, NSWorkspace
from macffi.QuickLook import get_file_thumbnail
from pymac.constants import kUTTypeFolder, kUTTypePNG
from dropbox.client.folder_tagger.folder_icon_mac import FolderTagIcon
from dropbox.foundation.native_icon.interface import ImageFormat, NativeIconLoaderInterface
from dropbox.mac.internal import autoreleasepool

def resize_nsimage(image = None, size = None):
    resized = NSImage.alloc().initWithSize_((size, size))
    resized.lockFocus()
    image.drawInRect_(NSMakeRect(0, 0, size, size))
    resized.unlockFocus()
    return resized


def _nsimage_to_nsdata(image = None):
    data = image.TIFFRepresentation()
    if not data:
        return None
    bitmap = NSBitmapImageRep.alloc().initWithData_(data)
    if not bitmap:
        return None
    png_data = None.representationUsingType_properties_(NSPNGFileType, None)
    return png_data


def _get_file_icon_by_path_as_png_data(local_path = None, size = None):
    icon = NSWorkspace.sharedWorkspace().iconForFile_(local_path)
    if not icon:
        return None
    icon = resize_nsimage(icon, size)
    return _nsimage_to_nsdata(icon)


def _get_file_icon_by_type_as_png_data(extension = None, size = None):
    icon = NSWorkspace.sharedWorkspace().iconForFileType_(extension)
    if not icon:
        return None
    icon = resize_nsimage(icon, size)
    return _nsimage_to_nsdata(icon)


def _get_default_folder_icon_as_png_data(size = None):
    icon = NSWorkspace.sharedWorkspace().iconForFileType_(kUTTypeFolder)
    if not icon:
        return None
    icon = resize_nsimage(icon, size)
    return _nsimage_to_nsdata(icon)


def _get_file_thumbnail_as_png_data_bytes(local_path = None, size = None):
    thumbnail_data = get_file_thumbnail(local_path, size, True, kUTTypePNG)
    if thumbnail_data or len(thumbnail_data) == 0:
        return None


class NativeIconLoaderMac(NativeIconLoaderInterface):
    
    def _check_supported_format(self = None, format = None):
        if format != ImageFormat.PNG:
            raise ValueError('Image format %r is not supported.' % format)

    
    def get_file_icon_by_path(self = None, local_path = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        self._check_supported_format(format)
        autoreleasepool()
        icon = _get_file_icon_by_path_as_png_data(local_path, size)
        if not icon:
            None(None, None)
            return None
        None(None, None)
        return 
        with None:
            if not None, bytes(icon.bytes()):
                pass

    
    def get_file_icon_by_type(self = None, extension = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('extension', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        self._check_supported_format(format)
        autoreleasepool()
        icon = _get_file_icon_by_type_as_png_data(extension, size)
        if not icon:
            None(None, None)
            return None
        None(None, None)
        return 
        with None:
            if not None, bytes(icon.bytes()):
                pass

    
    def get_default_folder_icon(self = None, size = None, scale_factor = None, format = (ImageFormat.PNG,)):
        self._check_supported_format(format)
        autoreleasepool()
        icon = _get_default_folder_icon_as_png_data(size)
        if not icon:
            None(None, None)
            return None
        None(None, None)
        return 
        with None:
            if not None, bytes(icon.bytes()):
                pass

    
    def get_folder_icon_by_tag(self = None, tag = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('tag', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        self._check_supported_format(format)
        autoreleasepool()
        nsimage = FolderTagIcon.get_image_for_tag(tag, is_selsync = True)
        if not nsimage:
            None(None, None)
            return None
        nsimage = resize_nsimage(nsimage, size)
        None(None, None)
        return 
        with None:
            if not None, _nsimage_to_nsdata(nsimage):
                pass

    
    def get_file_thumbnail_by_path(self = None, local_path = None, size = None, dropbox_feature_attribution = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'dropbox_feature_attribution', 'Text', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        self._check_supported_format(format)
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, _get_file_thumbnail_as_png_data_bytes(local_path, size):
                pass


