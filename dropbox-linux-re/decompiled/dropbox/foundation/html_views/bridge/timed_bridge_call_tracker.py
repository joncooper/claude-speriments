# Source Generated with Decompyle++
# File: timed_bridge_call_tracker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, List, Text, TypedDict
from dropbox.client.features.debug_bridge_call_profiler.bridge_gen.bridge_call_record import BridgeCallRecord
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.html_views.common.bridge_gen.bridge_call_checkpoint import BridgeCallCheckpoint
from dropbox.foundation.html_views.common.bridge_gen.timed_bridge_call import TimedBridgeCall
_PendingBridgeCall = TypedDict('_PendingBridgeCall', {
    'class_name': Text,
    'method_name': Text,
    'stack': Text,
    'params': Any,
    'checkpoints': Dict[(BridgeCallCheckpoint, float)],
    'message_id': int })

class TimedBridgeCallTracker:
    
    def __init__(self = None):
        self.pending_bridge_calls = { }
        self.completed_calls = []
        self.feature = '<unknown>'

    
    def set_feature(self = None, path = None):
        self.feature = path

    
    def clear_calls(self = None):
        self.pending_bridge_calls.clear()
        self.completed_calls.clear()

    
    def start_call(self, checkpoints, class_name, method_name = None, params = None, stack = None, message_id = ('checkpoints', 'Dict[BridgeCallCheckpoint, float]', 'class_name', 'Text', 'method_name', 'Text', 'params', 'List[Any]', 'stack', 'Text', 'message_id', 'int', 'return', 'None')):
        if message_id in self.pending_bridge_calls:
            report_bad_assumption('bridge message with same id already recorded')
        self.pending_bridge_calls[message_id] = {
            'class_name': class_name,
            'method_name': method_name,
            'stack': stack,
            'params': params,
            'checkpoints': checkpoints,
            'message_id': message_id }

    
    def get_calls(self = None):
        calls = sorted(self.completed_calls, key = (lambda x: x.checkpoints[BridgeCallCheckpoint.CALL_TIME.name]))
        self.completed_calls = []
        return calls

    
    def end_calls(self = None, calls_to_end = None):
        for js_call in calls_to_end:
            if js_call.message_id in self.pending_bridge_calls:
                py_call = self.pending_bridge_calls.pop(js_call.message_id)
                complete_call = complete_bridge_call_from_py_js_calls(py_call, js_call, {
                    'feature': self.feature })
                self.completed_calls.append(complete_call)
                continue
            report_bad_assumption('No corresponding python side call found for a logged js bridge call')
            return None



def bridge_call_checkpoints():
    return list(BridgeCallCheckpoint)


def complete_bridge_call_from_py_js_calls(py_call = None, js_call = None, extra = None):
    pass
# WARNING: Decompyle incomplete

