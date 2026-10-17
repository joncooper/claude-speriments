# Source Generated with Decompyle++
# File: files_v2.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id

class HighlightSpan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

HighlightSpan_validator = bv.Struct(HighlightSpan)

class Snippet(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Snippet_validator = bv.Struct(Snippet)
HighlightSpan.highlight_str.validator = bv.String()
HighlightSpan.highlight_str.validator._redact = bv.BlotRedactor(None)
HighlightSpan.is_highlighted.validator = bv.Boolean()
HighlightSpan.is_highlighted.validator._redact = bv.BlotRedactor(None)
HighlightSpan._all_field_names_ = set([
    'highlight_str',
    'is_highlighted'])
HighlightSpan._all_fields_ = [
    ('highlight_str', HighlightSpan.highlight_str.validator),
    ('is_highlighted', HighlightSpan.is_highlighted.validator)]
Snippet.highlight_spans.validator = bv.Nullable(bv.List(HighlightSpan_validator))
Snippet._all_field_names_ = set([
    'highlight_spans'])
Snippet._all_fields_ = [
    ('highlight_spans', Snippet.highlight_spans.validator)]
HighlightSpan.highlight_str.default = ''
HighlightSpan.is_highlighted.default = False
ROUTES = { }
