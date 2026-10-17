# Source Generated with Decompyle++
# File: premium_kit_assets.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class Asset(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Asset_validator = bv.Struct(Asset)

class Graphic(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Graphic_validator = bv.Struct(Graphic)

class Image(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Image_validator = bv.Struct(Image)

class Video(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Video_validator = bv.Struct(Video)

class ValueUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValueUnion_validator = bv.Union(ValueUnion)
Asset.asset_id.validator = bv.String()
Asset.asset_id.validator._redact = bv.BlotRedactor(None)
Asset.graphic.validator = bv.Nullable(Graphic_validator)
Asset.color_hex.validator = bv.String()
Asset.color_hex.validator._redact = bv.BlotRedactor(None)
Asset._all_field_names_ = set([
    'asset_id',
    'graphic',
    'color_hex'])
Asset._all_fields_ = [
    ('asset_id', Asset.asset_id.validator),
    ('graphic', Asset.graphic.validator),
    ('color_hex', Asset.color_hex.validator)]
Graphic.picker_image.validator = bv.String()
Graphic.picker_image.validator._redact = bv.BlotRedactor(None)
Graphic.fallback_image_url.validator = bv.Nullable(bv.String())
Graphic.fallback_image_url.validator._redact = bv.BlotRedactor(None)
Graphic.value.validator = bv.Nullable(ValueUnion_validator)
Graphic._all_field_names_ = set([
    'picker_image',
    'fallback_image_url',
    'value'])
Graphic._all_fields_ = [
    ('picker_image', Graphic.picker_image.validator),
    ('fallback_image_url', Graphic.fallback_image_url.validator),
    ('value', Graphic.value.validator)]
Image.original_url.validator = bv.String()
Image.original_url.validator._redact = bv.BlotRedactor(None)
Image._all_field_names_ = set([
    'original_url'])
Image._all_fields_ = [
    ('original_url', Image.original_url.validator)]
Video.original_url.validator = bv.String()
Video.original_url.validator._redact = bv.BlotRedactor(None)
Video._all_field_names_ = set([
    'original_url'])
Video._all_fields_ = [
    ('original_url', Video.original_url.validator)]
ValueUnion._image_validator = Image_validator
ValueUnion._video_validator = Video_validator
ValueUnion._other_validator = bv.Void()
ValueUnion._tagmap = {
    'image': ValueUnion._image_validator,
    'video': ValueUnion._video_validator,
    'other': ValueUnion._other_validator }
ValueUnion.other = ValueUnion('other')
Asset.asset_id.default = ''
Asset.color_hex.default = ''
Graphic.picker_image.default = ''
Image.original_url.default = ''
Video.original_url.default = ''
ROUTES = { }
