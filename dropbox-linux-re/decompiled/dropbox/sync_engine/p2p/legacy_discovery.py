# Source Generated with Decompyle++
# File: legacy_discovery.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import json
import select
import socket
import time
from json import JSONDecodeError
from typing import Any, Dict, Optional
from build_number import is_test
from six import integer_types
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report_aggregate_event
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import bytesafe_json_dumps, make_bytes, make_str
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.network import generate_ipaddresses, is_in_local_network
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MSG_MAX_SEND_SIZE = 512
MSG_MAX_RECV_SIZE = 65536
SIX_HOURS = 21600

class DiscoveryEngine(object):
    announcement_interval = 30
    HANDLED_ERROR_CODES = set([
        errno.EPERM,
        errno.EDESTADDRREQ,
        errno.EHOSTUNREACH,
        errno.ENETDOWN,
        errno.ENETUNREACH,
        errno.EADDRNOTAVAIL,
        errno.EHOSTDOWN])
    
    def __init__(self, version):
        self._version = version
        self._bind_addr = ('', dropbox_url_info.discovery_port)
        self._socket = self._init_socket(self._bind_addr)
        self._announcement_data = None
        self._next_announcement_time = 0
        self._subscribers = set()

    
    def set_announcement_data(self, version, port, host_int, namespaces_callback):
        pass
    # WARNING: Decompyle incomplete

    
    def subscribe(self, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def pulse(self, force_broadcast = (False,)):
        self._handle_incoming_announcements()
        now = get_monotonic_time_seconds()
        if force_broadcast or now >= self._next_announcement_time:
            self._next_announcement_time = now + self.announcement_interval
            self._announce()
            return None

    
    def _announce(self):
        namespaces = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._namespaces_callback()())
        if not namespaces:
            return None
        self._announcement_data['namespaces'] = list
        raw_msgs = self._encode_announcement(self._announcement_data)
        for raw_msg in raw_msgs:
            self._do_broadcast(raw_msg, dropbox_url_info.discovery_port)
            self._last_announcement_monotonic_time = get_monotonic_time_seconds()
            return None

    
    def _do_broadcast(self, raw_msg, port):
        report_aggregate_event('p2p-broadcast-made', {
            'num-broadcasts': 1 }, approx_timeout = SIX_HOURS)
        
        try:
            self._socket.sendto(raw_msg, 0, ('<broadcast>', port))
        except OSError:
            e = None
            report_aggregate_event('p2p-broadcast-error', {
                e.errno: 1 }, approx_timeout = SIX_HOURS)
            if e.errno in self.HANDLED_ERROR_CODES:
                TRACE('failed to broadcast send to port %d (%s)', port, errno.errorcode[e.errno])
            else:
                TRACE('failed to broadcast send to port %d (%r)', port, e)
                report_exception(component = DesktopComponent.LAN_SYNC)
            e = None
            del e
        except Exception:
            e = None
            TRACE('failed to broadcast send to port %d (%r)', port, e)
            report_exception(component = DesktopComponent.LAN_SYNC)
            e = None
            del e
        except:
            e = None
            del e

        
        try:
            for addrdata in generate_ipaddresses():
                baddr = addrdata.get('broadcast')
                if not baddr:
                    continue
                if is_test():
                    TRACE('DiscoveryEngine: Broadcasting to %r: %r', (baddr, port), raw_msg)
                self._socket.sendto(raw_msg, 0, (baddr, port))
                
                try:
                    continue
                    except OSError:
                        e = None
                        report_aggregate_event('p2p-broadcast-baddr-error', {
                            e.errno: 1 }, approx_timeout = SIX_HOURS)
                        if e.errno in self.HANDLED_ERROR_CODES:
                            TRACE('failed to send to baddr %s port %d (%s)', baddr, port, errno.errorcode[e.errno])
                        else:
                            TRACE('failed to send to baddr %s port %d (%r)', baddr, port, e)
                            report_exception(component = DesktopComponent.LAN_SYNC)
                            
                            try:
                                e = None
                                del e
                                continue
                                e = None
                                del e
                                except Exception:
                                    e = None
                                    TRACE('failed to send to baddr %s port %d (%r)', baddr, port, e)
                                    report_exception(component = DesktopComponent.LAN_SYNC)
                                    
                                    try:
                                        e = None
                                        del e
                                        continue
                                        e = None
                                        del e
                                        
                                        try:
                                            return None
                                        except Exception:
                                            report_exception(component = DesktopComponent.LAN_SYNC)
                                            return None






    
    def _handle_incoming_announcements(self):
        rlist = select.select((self._socket,), (), (), 0)[0]
        if self._socket not in rlist:
            return None
        
        try:
            (raw_msg, remote_addr) = self._socket.recvfrom(MSG_MAX_RECV_SIZE)
        except Exception:
            e = None
            if e.errno != 10054 and e.errno != 10052:
                report_exception(severity = Severity.DEBUG, component = DesktopComponent.LAN_SYNC)
            self._socket.close()
        except Exception:
            if e.errno != 10054 and e.errno != 10052:
                report_exception(severity = Severity.DEBUG, component = DesktopComponent.LAN_SYNC)

        self._socket = self._init_socket(self._bind_addr)
        e = None
        del e
        return None
        e = None
        del e
        if not raw_msg:
            continue
        ips = list(generate_ipaddresses())
    # WARNING: Decompyle incomplete

    
    def _parse_announcement(self = None, raw_msg = None):
        
        try:
            data = json.loads(raw_msg)
        except Exception:
            e = None
            TRACE('[P2P] Could not decode announcement message (%r)', e)
            e = None
            del e
            return None
            e = None
            del e

        if not isinstance(data, dict):
            raise TypeError('cannot parse: not a dict')
        msg = { }
        if 'version' in data:
            version = (lambda .0: pass# WARNING: Decompyle incomplete
)(data['version']())
            if version != self._version:
                return None
            msg['version'] = tuple
        else:
            return None
        if None in data:
            msg['host_int'] = int(data['host_int'])
        if 'port' in data:
            msg['port'] = int(data['port'])
        if 'namespaces' in data:
            msg['namespaces'] = (lambda .0: pass# WARNING: Decompyle incomplete
)(data['namespaces']())
        return msg

    _encode_announcement = (lambda out: pass# WARNING: Decompyle incomplete
)()
    
    def _init_socket(self, bind_addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception:
            pass

        
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except Exception:
            pass

        
        try:
            s.bind(bind_addr)
        except Exception:
            report_exception(component = DesktopComponent.LAN_SYNC)
            report_bad_assumption('P2P UDP bind() failed.  please notify dlitz')

        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        return s


