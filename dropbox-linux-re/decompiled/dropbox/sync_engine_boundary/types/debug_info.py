# Source Generated with Decompyle++
# File: debug_info.pyc (Python 3.11)

from typing import List, Optional
from dropbox.proto.nucleus.app_service_pb2 import DebugInfo as DebugInfoProto

class DebugInfo:
    
    def __init__(self, component, description = None, file_path = None, actions = None, children = ('component', 'str', 'description', 'str', 'file_path', 'Optional[str]', 'actions', 'List[str]')):
        self.component = component
        self.description = description
        self.file_path = file_path
        self.actions = actions
        self.children = children

    from_proto = (lambda proto = None: proto.component(component = proto.description, description = None if not proto.file_path else proto.file_path, file_path = list(proto.actions), actions = (lambda .0: [ DebugInfo.from_proto(child) for child in .0 ]), children = proto.children())
)()

