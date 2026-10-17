# Source Generated with Decompyle++
# File: handler_registries.pyc (Python 3.11)

import traceback
from typing import Any
from dropbox.handler import Handler
_trace_handler: 'Handler[Any]' = Handler(recursive = False, handle_exc = traceback.print_exc)
run_trace_handlers = _trace_handler.run_handlers
add_trace_handler = _trace_handler.add_handler
remove_trace_handler = _trace_handler.remove_handler
_exception_handler: 'Handler[Any]' = Handler(recursive = True, handle_exc = traceback.print_exc)
run_exception_handlers = _exception_handler.run_handlers
add_exception_handler = _exception_handler.add_handler
remove_exception_handler = _exception_handler.remove_handler

def clear_trace_and_exc_handlers():
    _trace_handler.clear()
    _exception_handler.clear()

