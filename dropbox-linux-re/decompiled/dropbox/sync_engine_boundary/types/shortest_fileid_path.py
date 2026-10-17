# Source Generated with Decompyle++
# File: shortest_fileid_path.pyc (Python 3.11)

from typing import Iterable, NamedTuple, Text
from dropbox.model.types import FileId
from dropbox.proto.nucleus.common_api_types_pb2 import ShortestFileIdPath as ShortestFileIdPathProto

class ShortestFileIdPath(NamedTuple):
    relative_components: 'Iterable[Text]' = 'ShortestFileIdPath'
    from_proto = (lambda proto = None: ShortestFileIdPath(FileId(proto.base_fileid.id), proto.relative_components))()

