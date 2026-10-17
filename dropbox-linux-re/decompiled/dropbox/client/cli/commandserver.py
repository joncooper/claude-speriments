# Source Generated with Decompyle++
# File: commandserver.pyc (Python 3.11)

from __future__ import absolute_import
import asynchat
import asyncore
import itertools
import socket
from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Text
from six import iteritems
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.functions import desanitize, sanitize
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    asyncore_maptype = asyncore._maptype
CommandArgType = Dict[(Text, List[Text])]
CommandRetType = Mapping[(Text, Iterable[Text])]
CommandType = Callable[([
    'CommandServer',
    object,
    CommandArgType], CommandRetType)]

class IllegalArgumentException(Exception):
    pass
# WARNING: Decompyle incomplete


class CommandNotFoundError(Exception):
    pass

ConnectionStateHook = Callable[([
    'CommandServer',
    'ConnectionState'], None)]

class ConnectionState(object):
    
    def __init__(self = None):
        self.on_disconnect_hooks = []

    
    def add_on_disconnect_hook(self = None, hook = None):
        self.on_disconnect_hooks.append(hook)

    
    def remove_on_disconnect_hook(self = None, hook = None):
        self.on_disconnect_hooks.remove(hook)

    
    def call_on_disconnect_hooks(self = None, cs = None):
        for hook in self.on_disconnect_hooks:
            hook(cs, self)
            return None



class CommandServerHandler(asynchat.async_chat):
    
    class State(Enum):
        WAITING_FOR_COMMAND = 0
        GETTING_ARGUMENTS = 1

    numinstances = 0
    
    def __init__(self = None, cs = None, conn = None, addr = (None,), map = ('cs', 'CommandServer', 'conn', 'socket.socket', 'addr', 'object', 'map', 'Optional[Dict[int, Any]]', 'return', 'None')):
        asynchat.async_chat.__init__(self, sock = conn, map = map)
        self.set_terminator(b'\n')
        self.current_line_data = []
        self.state = CommandServerHandler.State.WAITING_FOR_COMMAND
        self.command_name = None
        self.command_arguments = { }
        self.errors = []
        self.connstate = ConnectionState()
        self.cs = cs
        self.closed = False

    
    def collect_incoming_data(self = None, data = None):
        self.current_line_data.append(data)

    
    def close(self = None):
        if self.closed:
            return None
        None.async_chat.close(self)
        
        try:
            self.connstate.call_on_disconnect_hooks(self.cs)
        except Exception:
            report_exception(component = DesktopComponent.PREFERENCES_UI)

        TRACE('Closed connection to command server')
        True = CommandServerHandler, CommandServerHandler.numinstances -= 1, .numinstances

    
    def respond_notok(self = None):
        self.push(b'notok\n')
        for error in self.errors:
            self.push(sanitize(error).encode('utf8'))
            self.push(b'\n')
            self.push(b'done\n')
            return None

    
    def respond_ok(self = None, rets = None):
        result = (lambda .0: pass# WARNING: Decompyle incomplete
)(iteritems(rets)()).encode('utf8')
        self.push(b'ok\n')
        self.push(result)
        self.push(b'done\n')

    
    def handle_error(self = None):
        report_exception(component = DesktopComponent.PREFERENCES_UI)
        
        try:
            self.close()
            return None
        except Exception:
            report_exception(component = DesktopComponent.PREFERENCES_UI)
            return None


    
    def found_terminator(self = None):
        line = b''.join(self.current_line_data).decode('utf8')
        if self.state == CommandServerHandler.State.WAITING_FOR_COMMAND:
            self.errors[:] = []
            self.command_name = desanitize(line)
            self.command_arguments = { }
            self.state = CommandServerHandler.State.GETTING_ARGUMENTS
    # WARNING: Decompyle incomplete



class CommandServer(asyncore.dispatcher):
    
    def __init__(self, app = None, addr = None, sock = None, map = ('app', 'DropboxApplication', 'addr', 'Any', 'sock', 'socket.socket', 'map', 'asyncore_maptype', 'return', 'None')):
        asyncore.dispatcher.__init__(self, sock = sock, map = map)
        self.map = self._map
        self.bind(addr)
        self.listen(5)
        self.command_dict = { }
        self.command_dict_lock = Lock()
        self.app = app
        TRACE('Command Server listening')

    
    def writable(self = None):
        return False

    
    def add_command(self = None, name = None, fn = None):
        self.command_dict_lock
        self.command_dict[name] = fn
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def remove_command(self = None, name = None):
        self.command_dict_lock
        del self.command_dict[name]
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def call_command(self = None, name = None, conn = None, args = ('name', 'Text', 'conn', 'object', 'args', 'CommandArgType', 'return', 'CommandRetType')):
        self.command_dict_lock
        cmd = self.command_dict[name]

    
    def handle_error(self):
        report_exception(component = DesktopComponent.PREFERENCES_UI)

    
    def handle_accept(self):
        (conn, addr) = self.accept()
        if CommandServerHandler.numinstances >= 10:
            TRACE('Declined connection to command server: %s', Text(addr))
            conn.close()
            return None
        TRACE('Connection to command server: %s', Text(addr))
        CommandServerHandler(self, conn, addr, map = self.map)


