# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
import ctypes
import socket
from ctypes import c_char_p, c_uint, c_uint8, c_uint16, c_uint32, c_ushort, c_void_p, cast, get_errno, POINTER, Structure, Union
from typing import Dict, Iterator, Optional
IFF_BROADCAST = 2
IFF_POINTTOPOINT = 16
ByteArraySize4Type = c_uint8 * 4
ByteArraySize8Type = c_uint8 * 8
ByteArraySize14Type = c_uint8 * 14
ByteArraySize16Type = c_uint8 * 16

class sockaddr(Structure):
    _fields_ = [
        ('sa_family', c_ushort),
        ('sa_data', ByteArraySize14Type)]


class sockaddr_in(Structure):
    _fields_ = [
        ('sin_family', c_ushort),
        ('sin_port', c_uint16),
        ('sin_addr', ByteArraySize4Type)]


class sockaddr_in6(Structure):
    _fields_ = [
        ('sin6_family', c_ushort),
        ('sin6_port', c_uint16),
        ('sin6_flowinfo', c_uint32),
        ('sin6_addr', ByteArraySize16Type),
        ('sin6_scope_id', c_uint32)]


class ifa_ifu(Union):
    _fields_ = [
        ('ifu_broadaddr', POINTER(sockaddr)),
        ('ifu_dstaddr', POINTER(sockaddr))]


class ifaddrs(Structure):
    pass

ifaddrs._fields_ = [
    ('ifa_next', POINTER(ifaddrs)),
    ('ifa_name', c_char_p),
    ('ifa_flags', c_uint),
    ('ifa_addr', POINTER(sockaddr)),
    ('ifa_netmask', POINTER(sockaddr)),
    ('ifa_ifu', ifa_ifu),
    ('ifa_data', c_void_p)]
libc = ctypes.CDLL('libc.so.6')

def _get_socket_ip(sa = None):
    addr = None
    if sa and sa.contents:
        family = sa.contents.sa_family
        if family == socket.AF_INET:
            sa = cast(sa, POINTER(sockaddr_in)).contents
            addr = socket.inet_ntop(family, sa.sin_addr)
    return addr


def get_interface_data(ifaddr = None):
    addr = _get_socket_ip(ifaddr.contents.ifa_addr)
# WARNING: Decompyle incomplete


def generate_ipaddresses():
    pass
# WARNING: Decompyle incomplete

