# Source Generated with Decompyle++
# File: opener_utils.pyc (Python 3.11)

from typing import Any, cast, Dict, List, NamedTuple, Optional, Set, Text, Tuple
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from constants import CloudDocsUrlType
OpenInfo = NamedTuple('OpenInfo', [
    ('url_types', Optional[Set[CloudDocsUrlType]])])
CLOUD_ENHANCED_OPEN_INFO = OpenInfo(url_types = {
    CloudDocsUrlType.DROPBOX_CLOUD_DOC,
    CloudDocsUrlType.DROPBOX_DEV_CLOUD_DOC})
EXTENSION_TO_OPEN_INFO: 'Dict[Text, OpenInfo]' = {
    '.paper': OpenInfo(url_types = {
        CloudDocsUrlType.DROPBOX_CLOUD_DOC,
        CloudDocsUrlType.DROPBOX_DEV_CLOUD_DOC}),
    '.papert': OpenInfo(url_types = {
        CloudDocsUrlType.DROPBOX_CLOUD_DOC,
        CloudDocsUrlType.DROPBOX_DEV_CLOUD_DOC}),
    '.binder': OpenInfo(url_types = {
        CloudDocsUrlType.DROPBOX_CLOUD_DOC,
        CloudDocsUrlType.DROPBOX_DEV_CLOUD_DOC}),
    '.web': OpenInfo(url_types = None),
    '.docx': CLOUD_ENHANCED_OPEN_INFO,
    '.doc': CLOUD_ENHANCED_OPEN_INFO,
    '.pptx': CLOUD_ENHANCED_OPEN_INFO,
    '.ppt': CLOUD_ENHANCED_OPEN_INFO,
    '.xlsx': CLOUD_ENHANCED_OPEN_INFO,
    '.xls': CLOUD_ENHANCED_OPEN_INFO }

def extend_query_params(url = None, new_params = None):
    parse_results = urlparse(url)
    query_params = cast(List[Tuple[(Text, Any)]], parse_qsl(parse_results.query))
    query_params.extend(new_params)
    new_parse_results = parse_results._replace(query = urlencode(query_params))
    return urlunparse(new_parse_results)

