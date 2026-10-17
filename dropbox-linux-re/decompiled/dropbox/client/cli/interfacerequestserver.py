# Source Generated with Decompyle++
# File: interfacerequestserver.pyc (Python 3.11)

from __future__ import absolute_import
import asyncore
from contextlib import suppress

queue
from six import iteritems
import six.moves.queue, moves
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.functions import sanitize
from dropbox.threading import Lock
from dropbox.trace import TRACE

class InterfaceRequestServerHandler(asyncore.dispatcher):
    
    def __init__(self, conn, addr, *n, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def writable(self):
        if not self._pending_message is not None:
            pass
        return not self.output_queue.empty()

    
    def readable(self):
        return True

    
    def handle_expt(self):
        pass

    
    def handle_read(self):
        self.recv(4096)

    
    def handle_close(self):
        self.close()

    
    def handle_error(self):
        report_exception(component = DesktopComponent.PREFERENCES_UI)
        self.close()

    
    def handle_write(self):
        suppress(Queue.Empty)
    # WARNING: Decompyle incomplete

    
    def close(self):
        TRACE('closed connection to interface request server')
        asyncore.dispatcher.close(self)
    # WARNING: Decompyle incomplete



class InterfaceRequestServer(asyncore.dispatcher):
    
    def __init__(self, app, addr, *n, **kw):
        self.app = app
    # WARNING: Decompyle incomplete

    
    def writable(self):
        return False

    
    def handle_error(self):
        report_exception(component = DesktopComponent.PREFERENCES_UI)

    
    def ifaces_request(self, command_name, args):
        if not self._anyonelistening():
            return False
        lines = None
        lines.append(sanitize(command_name))
        for k, vals in iteritems(args):
            '\t'.join([
                sanitize(k)]((lambda .0: [ sanitize(val) for val in .0 ]) + vals()))
            lines.append('done')
            rawmsg = (lambda .0: pass# WARNING: Decompyle incomplete
)(lines()).encode('utf-8')
            self._push_rawmsg_to_ifaces(rawmsg)
            return True

    
    def _push_rawmsg_to_ifaces(self, data):
        self.ifaces_list_lock
        for iface_conn in self.ifaces_list:
            iface_conn.output_queue.put(data)
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def _anyonelistening(self):
        self.ifaces_list_lock
        None(None, None)
        return 
        with None:
            if not None, len(self.ifaces_list) > 0:
                pass

    
    def _handle_iface_conn_closed(self, iface_conn):
        self.ifaces_list_lock
        self.ifaces_list.remove(iface_conn)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def handle_accept(self):
        pass
    # WARNING: Decompyle incomplete


