# Source Generated with Decompyle++
# File: pipe_interface.pyc (Python 3.11)

from abc import abstractmethod
from typing import Callable, NamedTuple, Optional, Text
MessageToBrowser = NamedTuple('MessageToBrowser', [
    ('payload', Text),
    ('on_send', Callable[([], None)]),
    ('debug_name', Optional[Text])])

class JavaScriptBridgePipeInterface:
    send_message_to_browser = (lambda self = None, message = None: pass)()
    register_callbacks = (lambda self = None, on_message_from_view = None, on_browser_connection_opened = abstractmethod, on_security_policy_volation = ('on_message_from_view', 'Callable[[Text], None]', 'on_browser_connection_opened', 'Callable[[], None]', 'on_security_policy_volation', 'Callable[[Text, Text, Text, int], None]', 'return', 'None'): pass)()
    cleanup = (lambda self = None: pass)()

