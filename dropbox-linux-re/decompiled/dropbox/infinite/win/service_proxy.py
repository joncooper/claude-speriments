# Source Generated with Decompyle++
# File: service_proxy.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import struct
from ctypes import c_ubyte, c_wchar, create_unicode_buffer, memmove, resize, sizeof, Structure, Union
from ctypes.wintypes import DWORD
from enum import IntEnum
from typing import Optional, Text
import pywintypes
import win32con
import win32file
import win32service
import winerror
from dropbox.infinite import InfiniteReleaseChannel, InvalidInfiniteReleaseChannel
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.infinite.win.util import DRIVER_NAME, get_service_config, get_service_status, SERVICE_NAME, trace_recent_service_info
SERVICE_PIPE_NAME = Text('\\\\.\\pipe\\dbxsvc')

class ServiceFailedToConnectError(Exception):
    pass


class CommandType(IntEnum):
    LOAD_DRIVER = 0
    UNLOAD_DRIVER = 1
    IS_DRIVER_LOADED = 2
    KILL_SERVICE = 3
    CHECK_BUGCHECK = 4
    INSTALL_DRIVER = 5
    UNINSTALL_DRIVER = 6


class DriverVersion(IntEnum):
    NO_CHANGE = 0
    STABLE = 1
    CANARY = 2
    DEV = 3


class CheckBugcheckParams(Structure):
    _pack_ = 1
    _fields_ = [
        ('TimeCutoff', DWORD),
        ('LogFolder', c_ubyte * sizeof(c_wchar) * 1)]


class CommandDataInner(Union):
    _fields_ = [
        ('DriverVersion', DWORD),
        ('CheckBugcheckParams', CheckBugcheckParams)]


class Command(Structure):
    _pack_ = 1
    _anonymous_ = [
        '_u']
    _fields_ = [
        ('Type', DWORD),
        ('_u', CommandDataInner)]
    
    def __init__(self = None, command_type = None):
        self.Type = command_type

    
    def send(self = None):
        pipe = None
    # WARNING: Decompyle incomplete



class InfiniteService(object):
    load_driver = (lambda release_channel = None: command = Command(CommandType.LOAD_DRIVER)if release_channel == InfiniteReleaseChannel.DEV:
command.DriverVersion = DriverVersion.DEVelif release_channel == InfiniteReleaseChannel.STABLE or release_channel == InfiniteReleaseChannel.DRT:
command.DriverVersion = DriverVersion.STABLEelif release_channel == InfiniteReleaseChannel.CANARY:
command.DriverVersion = DriverVersion.CANARY# WARNING: Decompyle incomplete
)()
    unload_driver = (lambda : Command(CommandType.UNLOAD_DRIVER).send())()
    is_driver_loaded = (lambda : Command(CommandType.IS_DRIVER_LOADED).send())()
    kill_service = (lambda : Command(CommandType.KILL_SERVICE).send())()
    get_kernel_crashes = (lambda folder_path, timestamp: folder_path_buffer = create_unicode_buffer(folder_path)command = Command(CommandType.CHECK_BUGCHECK)command.CheckBugcheckParams.TimeCutoff = timestampresize(command, sizeof(command) + sizeof(folder_path_buffer))memmove(command.CheckBugcheckParams.LogFolder, folder_path_buffer, sizeof(folder_path_buffer))command.send())()
    is_service_installed = (lambda : get_service_config(SERVICE_NAME) is not None)()
    is_driver_installed = (lambda : get_service_config(DRIVER_NAME) is not None)()
    is_service_running = (lambda : 