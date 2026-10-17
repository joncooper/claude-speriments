# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import socket
import struct
from typing import Dict, List
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from dropbox.network.win import generate_ipaddresses
elif IS_MAC:
    from pymac.helpers.interfaces import generate_ipaddresses
elif IS_LINUX:
    from dropbox.network.linux import generate_ipaddresses
ONESEVENTWOPARTS = range(16, 32)()

def is_in_local_network(addr = None, interfaces = None):
    targetaddrint = struct.unpack('I', socket.inet_aton(addr))[0]
    local = False
    for netdata in interfaces:
        netmask = netdata.get('netmask')
        if not netmask:
            if addr.startswith('192.168.'):
                netmask = '255.255.0.0'
            if addr.startswith('10.'):
                netmask = '255.0.0.0'
            if addr.startswith('169.254.'):
                netmask = '255.255.0.0'
            if addr.startswith('172.'):
                part = addr[4:6]
                if part in ONESEVENTWOPARTS:
                    netmask = '255.240.0.0'
        if not netmask or netdata.get('addr'):
            continue
        netmaskint = struct.unpack('I', socket.inet_aton(netmask))[0]
        netaddrint = struct.unpack('I', socket.inet_aton(netdata['addr']))[0]
        if netmaskint & netaddrint == netmaskint & targetaddrint:
            local = True
        except Exception:
            report_exception(component = DesktopComponent.NETWORKING)
            continue
        return local

