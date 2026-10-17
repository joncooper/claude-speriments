# Source Generated with Decompyle++
# File: engine_waits.pyc (Python 3.11)

import json
from typing import Dict, NamedTuple, NewType
from dropbox.proto.engine_wait_tracker.engine_waits_pb2 import EngineWaitEntry, GetActiveEngineWaitsReply
WaitKind = NewType('WaitKind', str)

class EngineWait(NamedTuple):
    duration_in_secs: 'int' = 'EngineWait'
    from_proto = (lambda proto = None: kind = WaitKind(EngineWaitEntry.WaitKind.Name(proto.kind))duration = proto.durationEngineWait(kind, duration))()
    
    def __str__(self = None):
        return json.dumps({
            self.kind: self.duration_in_secs })



def ActiveEngineWaits():
    '''ActiveEngineWaits'''
    from_proto = (lambda proto = None: engine_waits = proto.active_waits()(lambda .0: pass# WARNING: Decompyle incomplete
)(engine_waits())
)()

ActiveEngineWaits = <NODE:27>(ActiveEngineWaits, 'ActiveEngineWaits', Dict[(WaitKind, int)])
