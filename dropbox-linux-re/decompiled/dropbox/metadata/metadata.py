# Source Generated with Decompyle++
# File: metadata.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
from typing import Dict, IO, Iterator, List, Set, Text
from six import iteritems
from EXIF import read_exif
EXIF_IMAGE_ORIENTATION = b'Image Orientation'
EXIF_IMAGE_MAKE = b'Image Make'
EXIF_IMAGE_MODEL = b'Image Model'
EXIF_LENGTH = b'EXIF ExifImageLength'
EXIF_WIDTH = b'EXIF ExifImageWidth'
EXIF_THUMBNAIL = b'Thumbnail Compression'
EXIF_THUMBNAIL_OFFSET = b'Thumbnail JPEGInterchangeFormat'
EXIF_THUMBNAIL_ORIENTATION = b'Thumbnail Orientation'
EXIF_JPEG_THUMBNAIL = b'JPEGThumbnail'
EXIF_TIFF_THUMBNAIL = b'TIFFThumbnail'
EXIF_DATETIME = b'EXIF DateTimeOriginal'
EXIF_CUSTOMRENDERED = b'EXIF CustomRendered'
EXIF_HEIFSIG = b'MakerNote Apple HEIF Signature'
PHOTO_EXIF_WHITELIST = {
    EXIF_IMAGE_ORIENTATION,
    EXIF_IMAGE_MAKE,
    EXIF_IMAGE_MODEL,
    EXIF_LENGTH,
    EXIF_WIDTH,
    EXIF_THUMBNAIL,
    EXIF_THUMBNAIL_OFFSET,
    EXIF_THUMBNAIL_ORIENTATION,
    EXIF_JPEG_THUMBNAIL,
    EXIF_TIFF_THUMBNAIL,
    EXIF_DATETIME,
    EXIF_CUSTOMRENDERED,
    EXIF_HEIFSIG}

def get_exif_metadata(file_obj = None, whitelist = None):
    _reset_file_cursor(file_obj)
    file_obj.seek(0, 0)
    None(None, None)
    return 
    with None:
        if not None, _normalize_metadata(read_exif(file_obj, whitelist), whitelist):
            pass

_reset_file_cursor = (lambda fileobj = None: pass# WARNING: Decompyle incomplete
)()

def _normalize_metadata(attrs = None, whitelist = None):
    if not whitelist:
        toret = attrs
# WARNING: Decompyle incomplete


def _to_encoded_dict(in_dict = None):
    pass
# WARNING: Decompyle incomplete

