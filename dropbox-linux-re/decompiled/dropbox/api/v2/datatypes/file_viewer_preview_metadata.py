# Source Generated with Decompyle++
# File: file_viewer_preview_metadata.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class Audio(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Audio_validator = bv.Struct(Audio)

class CloudDoc(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CloudDoc_validator = bv.Struct(CloudDoc)

class ContentMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentMetadata_validator = bv.Struct(ContentMetadata)

class Dimensions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Dimensions_validator = bv.Struct(Dimensions)

class DocPreview(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DocPreview_validator = bv.Struct(DocPreview)

class ExcelPreview(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExcelPreview_validator = bv.Struct(ExcelPreview)

class Image(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Image_validator = bv.Struct(Image)

class Linkfile(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Linkfile_validator = bv.Struct(Linkfile)

class PreviewMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewMetadata_validator = bv.Struct(PreviewMetadata)

class PreviewType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewType_validator = bv.Union(PreviewType)

class RestrictedContentTypes(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestrictedContentTypes_validator = bv.Struct(RestrictedContentTypes)

class RestrictedUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestrictedUnion_validator = bv.Union(RestrictedUnion)

class SharedFile(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFile_validator = bv.Struct(SharedFile)

class TextPreview(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TextPreview_validator = bv.Struct(TextPreview)

class ThreeDimensional(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThreeDimensional_validator = bv.Struct(ThreeDimensional)

class TranscriptPermission(bb.Union):
    pass
# WARNING: Decompyle incomplete

TranscriptPermission_validator = bv.Union(TranscriptPermission)

class Video(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Video_validator = bv.Struct(Video)

class ContentUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContentUnion_validator = bv.Union(ContentUnion)
Audio.container.validator = bv.String()
Audio.container.validator._redact = bv.BlotRedactor(None)
Audio.transcode_url.validator = bv.String()
Audio.transcode_url.validator._redact = bv.BlotRedactor(None)
Audio.waveform_url.validator = bv.String()
Audio.waveform_url.validator._redact = bv.BlotRedactor(None)
Audio.duration.validator = bv.Int64()
Audio.duration.validator._redact = bv.BlotRedactor(None)
Audio.transcript_url.validator = bv.String()
Audio.transcript_url.validator._redact = bv.BlotRedactor(None)
Audio.generated_captions_url.validator = bv.String()
Audio.generated_captions_url.validator._redact = bv.BlotRedactor(None)
Audio.transcript_permission.validator = TranscriptPermission_validator
Audio.transcript_urls_by_lang.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
Audio.caption_urls_by_lang.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
Audio._all_field_names_ = set([
    'container',
    'transcode_url',
    'waveform_url',
    'duration',
    'transcript_url',
    'generated_captions_url',
    'transcript_permission',
    'transcript_urls_by_lang',
    'caption_urls_by_lang'])
Audio._all_fields_ = [
    ('container', Audio.container.validator),
    ('transcode_url', Audio.transcode_url.validator),
    ('waveform_url', Audio.waveform_url.validator),
    ('duration', Audio.duration.validator),
    ('transcript_url', Audio.transcript_url.validator),
    ('generated_captions_url', Audio.generated_captions_url.validator),
    ('transcript_permission', Audio.transcript_permission.validator),
    ('transcript_urls_by_lang', Audio.transcript_urls_by_lang.validator),
    ('caption_urls_by_lang', Audio.caption_urls_by_lang.validator)]
CloudDoc.exit_url.validator = bv.String()
CloudDoc.exit_url.validator._redact = bv.BlotRedactor(None)
CloudDoc.text_url_tmpl.validator = bv.String()
CloudDoc.text_url_tmpl.validator._redact = bv.BlotRedactor(None)
CloudDoc.image_url_tmpl.validator = bv.String()
CloudDoc.image_url_tmpl.validator._redact = bv.BlotRedactor(None)
CloudDoc.refresh_url.validator = bv.String()
CloudDoc.refresh_url.validator._redact = bv.BlotRedactor(None)
CloudDoc.placeholder_image_url.validator = bv.String()
CloudDoc.placeholder_image_url.validator._redact = bv.BlotRedactor(None)
CloudDoc.autoprint_url.validator = bv.String()
CloudDoc.autoprint_url.validator._redact = bv.BlotRedactor(None)
CloudDoc._all_field_names_ = set([
    'exit_url',
    'text_url_tmpl',
    'image_url_tmpl',
    'refresh_url',
    'placeholder_image_url',
    'autoprint_url'])
CloudDoc._all_fields_ = [
    ('exit_url', CloudDoc.exit_url.validator),
    ('text_url_tmpl', CloudDoc.text_url_tmpl.validator),
    ('image_url_tmpl', CloudDoc.image_url_tmpl.validator),
    ('refresh_url', CloudDoc.refresh_url.validator),
    ('placeholder_image_url', CloudDoc.placeholder_image_url.validator),
    ('autoprint_url', CloudDoc.autoprint_url.validator)]
ContentMetadata.content.validator = bv.Nullable(ContentUnion_validator)
ContentMetadata._all_field_names_ = set([
    'content'])
ContentMetadata._all_fields_ = [
    ('content', ContentMetadata.content.validator)]
Dimensions.height.validator = bv.UInt64()
Dimensions.height.validator._redact = bv.BlotRedactor(None)
Dimensions.width.validator = bv.UInt64()
Dimensions.width.validator._redact = bv.BlotRedactor(None)
Dimensions._all_field_names_ = set([
    'height',
    'width'])
Dimensions._all_fields_ = [
    ('height', Dimensions.height.validator),
    ('width', Dimensions.width.validator)]
DocPreview.text_url_tmpl.validator = bv.String()
DocPreview.text_url_tmpl.validator._redact = bv.BlotRedactor(None)
DocPreview.image_url_tmpl.validator = bv.String()
DocPreview.image_url_tmpl.validator._redact = bv.BlotRedactor(None)
DocPreview.refresh_url.validator = bv.String()
DocPreview.refresh_url.validator._redact = bv.BlotRedactor(None)
DocPreview.placeholder_image_url.validator = bv.String()
DocPreview.placeholder_image_url.validator._redact = bv.BlotRedactor(None)
DocPreview.autoprint_url.validator = bv.String()
DocPreview.autoprint_url.validator._redact = bv.BlotRedactor(None)
DocPreview.supported_widths.validator = bv.Nullable(bv.List(bv.Int64()))
DocPreview.supported_widths.validator._redact = bv.BlotRedactor(None)
DocPreview.pages.validator = bv.UInt32()
DocPreview.pages.validator._redact = bv.BlotRedactor(None)
DocPreview._all_field_names_ = set([
    'text_url_tmpl',
    'image_url_tmpl',
    'refresh_url',
    'placeholder_image_url',
    'autoprint_url',
    'supported_widths',
    'pages'])
DocPreview._all_fields_ = [
    ('text_url_tmpl', DocPreview.text_url_tmpl.validator),
    ('image_url_tmpl', DocPreview.image_url_tmpl.validator),
    ('refresh_url', DocPreview.refresh_url.validator),
    ('placeholder_image_url', DocPreview.placeholder_image_url.validator),
    ('autoprint_url', DocPreview.autoprint_url.validator),
    ('supported_widths', DocPreview.supported_widths.validator),
    ('pages', DocPreview.pages.validator)]
ExcelPreview.workbook_data_url_tmpl.validator = bv.String()
ExcelPreview.workbook_data_url_tmpl.validator._redact = bv.BlotRedactor(None)
ExcelPreview.sheet_data_url_tmpl.validator = bv.String()
ExcelPreview.sheet_data_url_tmpl.validator._redact = bv.BlotRedactor(None)
ExcelPreview.tile_url_tmpl.validator = bv.String()
ExcelPreview.tile_url_tmpl.validator._redact = bv.BlotRedactor(None)
ExcelPreview._all_field_names_ = set([
    'workbook_data_url_tmpl',
    'sheet_data_url_tmpl',
    'tile_url_tmpl'])
ExcelPreview._all_fields_ = [
    ('workbook_data_url_tmpl', ExcelPreview.workbook_data_url_tmpl.validator),
    ('sheet_data_url_tmpl', ExcelPreview.sheet_data_url_tmpl.validator),
    ('tile_url_tmpl', ExcelPreview.tile_url_tmpl.validator)]
Image.thumbnail_url_tmpl.validator = bv.String()
Image.thumbnail_url_tmpl.validator._redact = bv.BlotRedactor(None)
Image.default_src.validator = bv.String()
Image.default_src.validator._redact = bv.BlotRedactor(None)
Image.full_size_src.validator = bv.String()
Image.full_size_src.validator._redact = bv.BlotRedactor(None)
Image.src_set.validator = bv.String()
Image.src_set.validator._redact = bv.BlotRedactor(None)
Image.motion_photo_video_src.validator = bv.String()
Image.motion_photo_video_src.validator._redact = bv.BlotRedactor(None)
Image._all_field_names_ = set([
    'thumbnail_url_tmpl',
    'default_src',
    'full_size_src',
    'src_set',
    'motion_photo_video_src'])
Image._all_fields_ = [
    ('thumbnail_url_tmpl', Image.thumbnail_url_tmpl.validator),
    ('default_src', Image.default_src.validator),
    ('full_size_src', Image.full_size_src.validator),
    ('src_set', Image.src_set.validator),
    ('motion_photo_video_src', Image.motion_photo_video_src.validator)]
Linkfile.url.validator = bv.String()
Linkfile.url.validator._redact = bv.BlotRedactor(None)
Linkfile.authenticated.validator = bv.Boolean()
Linkfile.authenticated.validator._redact = bv.BlotRedactor(None)
Linkfile._all_field_names_ = set([
    'url',
    'authenticated'])
Linkfile._all_fields_ = [
    ('url', Linkfile.url.validator),
    ('authenticated', Linkfile.authenticated.validator)]
PreviewMetadata.content.validator = bv.Nullable(ContentMetadata_validator)
PreviewMetadata.preview_url.validator = bv.String()
PreviewMetadata.preview_url.validator._redact = bv.BlotRedactor(None)
PreviewMetadata.dimensions.validator = bv.Nullable(Dimensions_validator)
PreviewMetadata.file_type_extension.validator = bv.String()
PreviewMetadata.file_type_extension.validator._redact = bv.BlotRedactor(None)
PreviewMetadata._all_field_names_ = set([
    'content',
    'preview_url',
    'dimensions',
    'file_type_extension'])
PreviewMetadata._all_fields_ = [
    ('content', PreviewMetadata.content.validator),
    ('preview_url', PreviewMetadata.preview_url.validator),
    ('dimensions', PreviewMetadata.dimensions.validator),
    ('file_type_extension', PreviewMetadata.file_type_extension.validator)]
PreviewType._unknown_validator = bv.Void()
PreviewType._archive_validator = bv.Void()
PreviewType._audio_validator = bv.Void()
PreviewType._cloud_doc_validator = bv.Void()
PreviewType._excel_validator = bv.Void()
PreviewType._html_validator = bv.Void()
PreviewType._image_validator = bv.Void()
PreviewType._linkfile_validator = bv.Void()
PreviewType._other_type_validator = bv.Void()
PreviewType._ssr_doc_validator = bv.Void()
PreviewType._raw_html_validator = bv.Void()
PreviewType._restricted_validator = bv.Void()
PreviewType._video_validator = bv.Void()
PreviewType._other_validator = bv.Void()
PreviewType._tagmap = {
    'unknown': PreviewType._unknown_validator,
    'archive': PreviewType._archive_validator,
    'audio': PreviewType._audio_validator,
    'cloud_doc': PreviewType._cloud_doc_validator,
    'excel': PreviewType._excel_validator,
    'html': PreviewType._html_validator,
    'image': PreviewType._image_validator,
    'linkfile': PreviewType._linkfile_validator,
    'other_type': PreviewType._other_type_validator,
    'ssr_doc': PreviewType._ssr_doc_validator,
    'raw_html': PreviewType._raw_html_validator,
    'restricted': PreviewType._restricted_validator,
    'video': PreviewType._video_validator,
    'other': PreviewType._other_validator }
PreviewType.unknown = PreviewType('unknown')
PreviewType.archive = PreviewType('archive')
PreviewType.audio = PreviewType('audio')
PreviewType.cloud_doc = PreviewType('cloud_doc')
PreviewType.excel = PreviewType('excel')
PreviewType.html = PreviewType('html')
PreviewType.image = PreviewType('image')
PreviewType.linkfile = PreviewType('linkfile')
PreviewType.other_type = PreviewType('other_type')
PreviewType.ssr_doc = PreviewType('ssr_doc')
PreviewType.raw_html = PreviewType('raw_html')
PreviewType.restricted = PreviewType('restricted')
PreviewType.video = PreviewType('video')
PreviewType.other = PreviewType('other')
RestrictedContentTypes.restricted.validator = bv.Nullable(RestrictedUnion_validator)
RestrictedContentTypes._all_field_names_ = set([
    'Restricted'])
RestrictedContentTypes._all_fields_ = [
    ('restricted', RestrictedContentTypes.restricted.validator)]
RestrictedUnion._video_validator = bv.Boolean()
RestrictedUnion._video_validator._redact = bv.BlotRedactor(None)
RestrictedUnion._ssr_doc_validator = bv.Boolean()
RestrictedUnion._ssr_doc_validator._redact = bv.BlotRedactor(None)
RestrictedUnion._image_validator = bv.Boolean()
RestrictedUnion._image_validator._redact = bv.BlotRedactor(None)
RestrictedUnion._other_validator = bv.Void()
RestrictedUnion._tagmap = {
    'video': RestrictedUnion._video_validator,
    'ssr_doc': RestrictedUnion._ssr_doc_validator,
    'image': RestrictedUnion._image_validator,
    'other': RestrictedUnion._other_validator }
RestrictedUnion.other = RestrictedUnion('other')
SharedFile.is_dir.validator = bv.Boolean()
SharedFile.is_dir.validator._redact = bv.BlotRedactor(None)
SharedFile.is_symlink.validator = bv.Boolean()
SharedFile.is_symlink.validator._redact = bv.BlotRedactor(None)
SharedFile.bytes.validator = bv.UInt64()
SharedFile.bytes.validator._redact = bv.BlotRedactor(None)
SharedFile.filename.validator = bv.String()
SharedFile.filename.validator._redact = bv.BlotRedactor(None)
SharedFile.sort_key.validator = bv.String()
SharedFile.sort_key.validator._redact = bv.BlotRedactor(None)
SharedFile.href.validator = bv.String()
SharedFile.href.validator._redact = bv.BlotRedactor(None)
SharedFile.preview_type.validator = PreviewType_validator
SharedFile.preview_metadata.validator = bv.Nullable(PreviewMetadata_validator)
SharedFile.ts.validator = bv.Int64()
SharedFile.ts.validator._redact = bv.BlotRedactor(None)
SharedFile.ns_id.validator = bv.UInt64()
SharedFile.ns_id.validator._redact = bv.BlotRedactor(None)
SharedFile.sjid.validator = bv.UInt64()
SharedFile.sjid.validator._redact = bv.BlotRedactor(None)
SharedFile.file_id.validator = bv.String()
SharedFile.file_id.validator._redact = bv.BlotRedactor(None)
SharedFile.direct_block_server.validator = bv.String()
SharedFile.direct_block_server.validator._redact = bv.BlotRedactor(None)
SharedFile.preview_url.validator = bv.String()
SharedFile.preview_url.validator._redact = bv.BlotRedactor(None)
SharedFile.thumbnail_url_tmpl.validator = bv.String()
SharedFile.thumbnail_url_tmpl.validator._redact = bv.BlotRedactor(None)
SharedFile.revision_id.validator = bv.String()
SharedFile.revision_id.validator._redact = bv.BlotRedactor(None)
SharedFile.icon.validator = bv.String()
SharedFile.icon.validator._redact = bv.BlotRedactor(None)
SharedFile.is_cloud_doc.validator = bv.Boolean()
SharedFile.is_cloud_doc.validator._redact = bv.BlotRedactor(None)
SharedFile._all_field_names_ = set([
    'is_dir',
    'is_symlink',
    'bytes',
    'filename',
    'sort_key',
    'href',
    'preview_type',
    'preview_metadata',
    'ts',
    'ns_id',
    'sjid',
    'file_id',
    'direct_block_server',
    'preview_url',
    'thumbnail_url_tmpl',
    'revision_id',
    'icon',
    'is_cloud_doc'])
SharedFile._all_fields_ = [
    ('is_dir', SharedFile.is_dir.validator),
    ('is_symlink', SharedFile.is_symlink.validator),
    ('bytes', SharedFile.bytes.validator),
    ('filename', SharedFile.filename.validator),
    ('sort_key', SharedFile.sort_key.validator),
    ('href', SharedFile.href.validator),
    ('preview_type', SharedFile.preview_type.validator),
    ('preview_metadata', SharedFile.preview_metadata.validator),
    ('ts', SharedFile.ts.validator),
    ('ns_id', SharedFile.ns_id.validator),
    ('sjid', SharedFile.sjid.validator),
    ('file_id', SharedFile.file_id.validator),
    ('direct_block_server', SharedFile.direct_block_server.validator),
    ('preview_url', SharedFile.preview_url.validator),
    ('thumbnail_url_tmpl', SharedFile.thumbnail_url_tmpl.validator),
    ('revision_id', SharedFile.revision_id.validator),
    ('icon', SharedFile.icon.validator),
    ('is_cloud_doc', SharedFile.is_cloud_doc.validator)]
TextPreview.extracted_text.validator = bv.String()
TextPreview.extracted_text.validator._redact = bv.BlotRedactor(None)
TextPreview._all_field_names_ = set([
    'extracted_text'])
TextPreview._all_fields_ = [
    ('extracted_text', TextPreview.extracted_text.validator)]
ThreeDimensional.model_url.validator = bv.String()
ThreeDimensional.model_url.validator._redact = bv.BlotRedactor(None)
ThreeDimensional._all_field_names_ = set([
    'model_url'])
ThreeDimensional._all_fields_ = [
    ('model_url', ThreeDimensional.model_url.validator)]
TranscriptPermission._ineligible_validator = bv.Void()
TranscriptPermission._opted_in_validator = bv.Void()
TranscriptPermission._other_validator = bv.Void()
TranscriptPermission._tagmap = {
    'ineligible': TranscriptPermission._ineligible_validator,
    'opted_in': TranscriptPermission._opted_in_validator,
    'other': TranscriptPermission._other_validator }
TranscriptPermission.ineligible = TranscriptPermission('ineligible')
TranscriptPermission.opted_in = TranscriptPermission('opted_in')
TranscriptPermission.other = TranscriptPermission('other')
Video.transcode_url.validator = bv.String()
Video.transcode_url.validator._redact = bv.BlotRedactor(None)
Video.transcode_urls_separate_resolutions.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
Video.container.validator = bv.String()
Video.container.validator._redact = bv.BlotRedactor(None)
Video.thumb_scrubber_vtt_url.validator = bv.String()
Video.thumb_scrubber_vtt_url.validator._redact = bv.BlotRedactor(None)
Video.poster_url_tmpl.validator = bv.String()
Video.poster_url_tmpl.validator._redact = bv.BlotRedactor(None)
Video.metadata_url.validator = bv.String()
Video.metadata_url.validator._redact = bv.BlotRedactor(None)
Video.transcript_url.validator = bv.String()
Video.transcript_url.validator._redact = bv.BlotRedactor(None)
Video.transcript_permission.validator = TranscriptPermission_validator
Video.generated_captions_url.validator = bv.String()
Video.generated_captions_url.validator._redact = bv.BlotRedactor(None)
Video.duration.validator = bv.Int64()
Video.duration.validator._redact = bv.BlotRedactor(None)
Video.transcript_urls_by_lang.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
Video.caption_urls_by_lang.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
Video.initial_video_bandwidth.validator = bv.String()
Video.initial_video_bandwidth.validator._redact = bv.BlotRedactor(None)
Video.mux_player_name.validator = bv.String()
Video.mux_player_name.validator._redact = bv.BlotRedactor(None)
Video._all_field_names_ = set([
    'transcode_url',
    'transcode_urls_separate_resolutions',
    'container',
    'thumb_scrubber_vtt_url',
    'poster_url_tmpl',
    'metadata_url',
    'transcript_url',
    'transcript_permission',
    'generated_captions_url',
    'duration',
    'transcript_urls_by_lang',
    'caption_urls_by_lang',
    'initial_video_bandwidth',
    'mux_player_name'])
Video._all_fields_ = [
    ('transcode_url', Video.transcode_url.validator),
    ('transcode_urls_separate_resolutions', Video.transcode_urls_separate_resolutions.validator),
    ('container', Video.container.validator),
    ('thumb_scrubber_vtt_url', Video.thumb_scrubber_vtt_url.validator),
    ('poster_url_tmpl', Video.poster_url_tmpl.validator),
    ('metadata_url', Video.metadata_url.validator),
    ('transcript_url', Video.transcript_url.validator),
    ('transcript_permission', Video.transcript_permission.validator),
    ('generated_captions_url', Video.generated_captions_url.validator),
    ('duration', Video.duration.validator),
    ('transcript_urls_by_lang', Video.transcript_urls_by_lang.validator),
    ('caption_urls_by_lang', Video.caption_urls_by_lang.validator),
    ('initial_video_bandwidth', Video.initial_video_bandwidth.validator),
    ('mux_player_name', Video.mux_player_name.validator)]
ContentUnion._archive_validator = bv.Boolean()
ContentUnion._archive_validator._redact = bv.BlotRedactor(None)
ContentUnion._raw_html_validator = bv.Boolean()
ContentUnion._raw_html_validator._redact = bv.BlotRedactor(None)
ContentUnion._restricted_validator = RestrictedContentTypes_validator
ContentUnion._excel_validator = ExcelPreview_validator
ContentUnion._video_validator = Video_validator
ContentUnion._audio_validator = Audio_validator
ContentUnion._linkfile_validator = Linkfile_validator
ContentUnion._ssr_doc_validator = DocPreview_validator
ContentUnion._image_validator = Image_validator
ContentUnion._cloud_doc_validator = CloudDoc_validator
ContentUnion._text_validator = TextPreview_validator
ContentUnion._three_dimensional_validator = ThreeDimensional_validator
ContentUnion._other_validator = bv.Void()
ContentUnion._tagmap = {
    'archive': ContentUnion._archive_validator,
    'raw_html': ContentUnion._raw_html_validator,
    'restricted': ContentUnion._restricted_validator,
    'excel': ContentUnion._excel_validator,
    'video': ContentUnion._video_validator,
    'audio': ContentUnion._audio_validator,
    'linkfile': ContentUnion._linkfile_validator,
    'ssr_doc': ContentUnion._ssr_doc_validator,
    'image': ContentUnion._image_validator,
    'cloud_doc': ContentUnion._cloud_doc_validator,
    'text': ContentUnion._text_validator,
    'three_dimensional': ContentUnion._three_dimensional_validator,
    'other': ContentUnion._other_validator }
ContentUnion.other = ContentUnion('other')
Audio.waveform_url.default = ''
Audio.duration.default = 0
Audio.transcript_url.default = ''
Audio.generated_captions_url.default = ''
Audio.transcript_permission.default = TranscriptPermission.ineligible
CloudDoc.exit_url.default = ''
CloudDoc.text_url_tmpl.default = ''
CloudDoc.image_url_tmpl.default = ''
CloudDoc.refresh_url.default = ''
CloudDoc.placeholder_image_url.default = ''
CloudDoc.autoprint_url.default = ''
Dimensions.height.default = 0
Dimensions.width.default = 0
DocPreview.refresh_url.default = ''
DocPreview.placeholder_image_url.default = ''
DocPreview.autoprint_url.default = ''
DocPreview.pages.default = 0
Image.default_src.default = ''
Image.full_size_src.default = ''
Image.src_set.default = ''
Image.motion_photo_video_src.default = ''
Linkfile.authenticated.default = False
PreviewMetadata.preview_url.default = ''
PreviewMetadata.file_type_extension.default = ''
SharedFile.is_dir.default = False
SharedFile.sort_key.default = ''
SharedFile.preview_type.default = PreviewType.unknown
SharedFile.direct_block_server.default = ''
SharedFile.preview_url.default = ''
SharedFile.thumbnail_url_tmpl.default = ''
SharedFile.icon.default = ''
SharedFile.is_cloud_doc.default = False
ThreeDimensional.model_url.default = ''
Video.thumb_scrubber_vtt_url.default = ''
Video.poster_url_tmpl.default = ''
Video.metadata_url.default = ''
Video.transcript_url.default = ''
Video.transcript_permission.default = TranscriptPermission.ineligible
Video.generated_captions_url.default = ''
Video.duration.default = 0
Video.initial_video_bandwidth.default = ''
Video.mux_player_name.default = ''
ROUTES = { }
