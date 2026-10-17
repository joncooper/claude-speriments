# Source Generated with Decompyle++
# File: trace_js_bridge.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.gandalf import Gandalf

class JavaScriptBridgeEventTracing:
    _tracing_allowed = False
    _gandalf: 'Optional[Gandalf]' = None
    set_gandalf = (lambda gandalf = None: pass# WARNING: Decompyle incomplete
)()
    _on_gandalf_changed = (lambda : if JavaScriptBridgeEventTracing._gandalf is not None:
passJavaScriptBridgeEventTracing._tracing_allowed = JavaScriptBridgeEventTracing._gandalf.allows_any_account('desktop-server-views-javascript-bridge-logging'))()
    should_trace = (lambda : JavaScriptBridgeEventTracing._tracing_allowed)()


class ElectronIpcEventTracing:
    _ipc_tracing_allowed = False
    _rpc_tracing_allowed = False
    _gandalf: 'Optional[Gandalf]' = None
    set_gandalf = (lambda gandalf = None: pass# WARNING: Decompyle incomplete
)()
    _on_gandalf_changed = (lambda : 