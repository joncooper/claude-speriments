# Source Generated with Decompyle++
# File: thumbnail_pipe.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
from typing import Optional, Text
import win32event
OpenFileMapping = ctypes.windll.kernel32.OpenFileMappingW
OpenFileMapping.argtypes = [
    ctypes.wintypes.DWORD,
    ctypes.wintypes.BOOL,
    ctypes.wintypes.LPWSTR]
OpenFileMapping.restype = ctypes.wintypes.HANDLE
MapViewOfFile = ctypes.windll.kernel32.MapViewOfFile
MapViewOfFile.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.c_size_t]
MapViewOfFile.restype = ctypes.c_void_p
RtlMoveMemory = ctypes.windll.kernel32.RtlMoveMemory
RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
RtlMoveMemory.restype = None
UnmapViewOfFile = ctypes.windll.kernel32.UnmapViewOfFile
UnmapViewOfFile.argtypes = (ctypes.c_void_p,)
UnmapViewOfFile.restype = ctypes.wintypes.BOOL
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.argtypes = (ctypes.wintypes.HANDLE,)
CloseHandle.restype = ctypes.wintypes.BOOL
FILE_MAP_WRITE = 2

class ThumbnailReply(object):
    
    def __init__(self = None, guid = None):
        self._guid = guid

    
    def send(self = None, buffer = None):
        event = win32event.CreateEvent(None, 1, 0, self._guid + '_event')
        
        try:
            filemap = OpenFileMapping(FILE_MAP_WRITE, False, self._guid)
            mapped_view = MapViewOfFile(filemap, FILE_MAP_WRITE, 0, 0, 0)
            if mapped_view:
                if not buffer:
                    buffer_size = ctypes.c_ulong(len(''))
                    length = ctypes.c_size_t(ctypes.sizeof(buffer_size))
                    RtlMoveMemory(mapped_view, ctypes.pointer(buffer_size), length)
                    if buffer:
                        buffer_address = mapped_view + length.value
                        length = ctypes.c_size_t(len(buffer))
                        RtlMoveMemory(buffer_address, buffer, length)
            win32event.SetEvent(event)
            if mapped_view:
                UnmapViewOfFile(mapped_view)
            if filemap:
                CloseHandle(filemap)
                return None
            return None
        except:
            if mapped_view:
                UnmapViewOfFile(mapped_view)
            if filemap:
                CloseHandle(filemap)



