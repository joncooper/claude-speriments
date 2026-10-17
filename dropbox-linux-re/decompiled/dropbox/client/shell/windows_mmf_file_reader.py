# Source Generated with Decompyle++
# File: windows_mmf_file_reader.pyc (Python 3.11)

import time
import ctypes
from ctypes import wintypes
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import SuppressedExceptionMixin
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE

class SuppressedRuntimeError(SuppressedExceptionMixin, RuntimeError):
    pass


class MemoryMappedFileReader:
    
    def __init__(self, read_callback, identifier, buffer_size = (4194304,)):
        self.BUFFER_SIZE = buffer_size
        self.HEADER_SIZE = 12
        self.MAPPING_NAME = identifier
        self.MUTEX_NAME = identifier + 'Mutex'
        self.EVENT_NAME = identifier + 'Event'
        self.DELAY_CONSUMING_POST_EVENT_SIGNAL = 5
        self.MMF_VERSION = 2
        self.INFINITE = 0xFFFFFFFF
        self.WAIT_ABANDONED = 128
        self.WAIT_OBJECT_0 = 0
        self.WAIT_TIMEOUT = 258
        self.FILE_MAP_ALL_ACCESS = 31
        self.PAGE_READWRITE = 4
        self.hMutex = None
        self.hMapFile = None
        self.hEvent = None
        self.pBuf = None
        self._map_windows_api()
        self._initialize_resources()
        self.read_callback = read_callback
        self.is_interrupted = False

    
    def _map_windows_api(self):
        kernel32 = ctypes.windll.kernel32
        self.CreateEventW = kernel32.CreateEventW
        self.CreateEventW.argtypes = [
            wintypes.LPVOID,
            wintypes.BOOL,
            wintypes.BOOL,
            wintypes.LPCWSTR]
        self.CreateEventW.restype = wintypes.HANDLE
        self.WaitForSingleObject = kernel32.WaitForSingleObject
        self.WaitForSingleObject.argtypes = [
            wintypes.HANDLE,
            wintypes.DWORD]
        self.WaitForSingleObject.restype = wintypes.DWORD
        self.CloseHandle = kernel32.CloseHandle
        self.CloseHandle.argtypes = [
            wintypes.HANDLE]
        self.CloseHandle.restype = wintypes.BOOL
        self.SetEvent = kernel32.SetEvent
        self.SetEvent.argtypes = [
            wintypes.HANDLE]
        self.SetEvent.restype = wintypes.BOOL
        self.ResetEvent = kernel32.ResetEvent
        self.ResetEvent.argtypes = [
            wintypes.HANDLE]
        self.ResetEvent.restype = wintypes.BOOL
        self.CreateMutexW = kernel32.CreateMutexW
        self.CreateMutexW.argtypes = [
            wintypes.LPVOID,
            wintypes.BOOL,
            wintypes.LPCWSTR]
        self.CreateMutexW.restype = wintypes.HANDLE
        self.ReleaseMutex = kernel32.ReleaseMutex
        self.ReleaseMutex.argtypes = [
            wintypes.HANDLE]
        self.ReleaseMutex.restype = wintypes.BOOL
        self.CreateFileMappingW = kernel32.CreateFileMappingW
        self.CreateFileMappingW.argtypes = [
            wintypes.HANDLE,
            wintypes.LPVOID,
            wintypes.DWORD,
            wintypes.DWORD,
            wintypes.DWORD,
            wintypes.LPCWSTR]
        self.CreateFileMappingW.restype = wintypes.HANDLE
        self.MapViewOfFile = kernel32.MapViewOfFile
        self.MapViewOfFile.argtypes = [
            wintypes.HANDLE,
            wintypes.DWORD,
            wintypes.DWORD,
            wintypes.DWORD,
            ctypes.c_size_t]
        self.MapViewOfFile.restype = wintypes.LPVOID
        self.OpenFileMappingW = kernel32.OpenFileMappingW
        self.OpenFileMappingW.argtypes = [
            wintypes.DWORD,
            wintypes.BOOL,
            wintypes.LPCWSTR]
        self.OpenFileMappingW.restype = wintypes.HANDLE
        self.UnmapViewOfFile = kernel32.UnmapViewOfFile
        self.UnmapViewOfFile.argtypes = [
            wintypes.LPVOID]
        self.UnmapViewOfFile.restype = wintypes.BOOL

    
    def _initialize_resources(self):
        
        try:
            self.hMutex = self.CreateMutexW(None, False, self.MUTEX_NAME)
            if not self.hMutex:
                last_error = ctypes.GetLastError()
                if last_error == 5:
                    raise SuppressedRuntimeError(f'''Could not create mutex \'{self.MUTEX_NAME}\'. Error: {last_error}''')
                raise RuntimeError(f'''Could not create mutex \'{self.MUTEX_NAME}\'. Error: {last_error}''')
            preexisting_mmf = True
            self.hMapFile = self.OpenFileMappingW(self.FILE_MAP_ALL_ACCESS, False, self.MAPPING_NAME)
            if not self.hMapFile:
                wait_result = self.WaitForSingleObject(self.hMutex, self.INFINITE)
                if wait_result != self.WAIT_OBJECT_0:
                    raise RuntimeError(f'''Failed to acquire mutex. Wait result: {wait_result}''')
                self.hMapFile = self.CreateFileMappingW(0xFFFFFFFFFFFFFFFF, None, self.PAGE_READWRITE, 0, self.BUFFER_SIZE, self.MAPPING_NAME)
                if not self.hMapFile:
                    raise RuntimeError(f'''Could not create file mapping object \'{self.MAPPING_NAME}\'. Error: {ctypes.GetLastError()}''')
                preexisting_mmf = False
            self.pBuf = self.MapViewOfFile(self.hMapFile, self.FILE_MAP_ALL_ACCESS, 0, 0, self.BUFFER_SIZE)
            if not self.pBuf:
                raise RuntimeError(f'''Could not map view of file. Error: {ctypes.GetLastError()}''')
            if not preexisting_mmf:
                self._initialize_header()
            self.hEvent = self.CreateEventW(None, True, False, self.EVENT_NAME)
            if not self.hEvent:
                raise RuntimeError(f'''Could not create event \'{self.EVENT_NAME}\'. Error: {ctypes.GetLastError()}''')
            
            try:
                pass
            except Exception:
                e = None
                report_exception(severity = Severity.WARN, component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
                self._cleanup_resources()
                raise e
                e = None
                del e

            
            try:
                if self.hMutex:
                    self.ReleaseMutex(self.hMutex)
                    return None
                return None
            except:
                if self.hMutex:
                    self.ReleaseMutex(self.hMutex)



    
    def _cleanup_resources(self):
        if self.pBuf:
            if not self.UnmapViewOfFile(self.pBuf):
                TRACE('!! UnmapViewOfFile failed. Error: %d', ctypes.GetLastError())
            self.pBuf = None
        if self.hMapFile:
            if not self.CloseHandle(self.hMapFile):
                TRACE('!! CloseHandle (file mapping) failed. Error: %d', ctypes.GetLastError())
            self.hMapFile = None
        if self.hMutex:
            if not self.CloseHandle(self.hMutex):
                TRACE('!! CloseHandle (mutex) failed. Error: %d', ctypes.GetLastError())
            self.hMutex = None
        if self.hEvent:
            if not self.CloseHandle(self.hEvent):
                TRACE('!! CloseHandle (event) failed. Error: %d', ctypes.GetLastError())
            self.hEvent = None
            return None

    
    def _initialize_header(self):
        header_size_ptr = ctypes.c_uint32.from_address(self.pBuf)
        header_size_ptr.value = self.HEADER_SIZE
        producer_offset_ptr = ctypes.c_uint32.from_address(self.pBuf + ctypes.sizeof(ctypes.c_uint32))
        producer_offset_ptr.value = 0
        version_ptr = ctypes.c_uint32.from_address(self.pBuf + 2 * ctypes.sizeof(ctypes.c_uint32))
        version_ptr.value = 0

    
    def __del__(self):
        self._cleanup_resources()

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cleanup_resources()

    
    def interrupt(self):
        if not self.hEvent:
            TRACE('!! Event handle is not initialized')
            return None
        
        try:
            self.is_interrupted = True
            result = self.SetEvent(self.hEvent)
            if not result:
                error_code = ctypes.GetLastError()
                TRACE('!! SetEvent failed. Error: %d', error_code)
                return None
            return None
        except Exception:
            e = None
            TRACE('!! Exception occurred while setting event: %s', str(e))
            e = None
            del e
            return None
            e = None
            del e


    
    def read(self):
        if not self.pBuf or self.hMutex:
            TRACE('!! MemoryMappedFileReader not properly initialized')
            return (False, None)
        
        try:
            wait_result = self.WaitForSingleObject(self.hMutex, self.INFINITE)
            if wait_result == self.WAIT_ABANDONED:
                TRACE('!! The producer thread must have crashed while owning the mutex. Data may be corrupted.')
                
                try:
                    self._initialize_header()
                    
                    try:
                        pass
                    except Exception:
                        e = None
                        self._cleanup_resources()
                        self._initialize_resources()
                    except Exception:
                        e2 = None
                        raise IOError('Unaccessible file. Possibly corrupted.'), e2
                        e2 = None
                        del e2
                        
                        try:
                            e = None
                            del e
                        e = None
                        del e
                        try:
                            if not self.ReleaseMutex(self.hMutex):
                                TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                return (False, None)
                            return None
                            
                            try:
                                if wait_result != self.WAIT_OBJECT_0:
                                    TRACE('!! Failed to acquire mutex. Wait result: %d', wait_result)
                                    if not self.ReleaseMutex(self.hMutex):
                                        TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                        return (False, None)
                                    return None
                                header_size = None.c_uint32.from_address(self.pBuf).value
                                producer_offset = ctypes.c_uint32.from_address(self.pBuf + ctypes.sizeof(ctypes.c_uint32)).value
                                version = ctypes.c_uint32.from_address(self.pBuf + 2 * ctypes.sizeof(ctypes.c_uint32)).value
                                if header_size != self.HEADER_SIZE or version != self.MMF_VERSION:
                                    TRACE('!! MMF version mismatch. Expected: %d, Found: %d', self.MMF_VERSION, version)
                                    if not self.ReleaseMutex(self.hMutex):
                                        TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                        return (False, None)
                                    return None
                                if None <= 0:
                                    if not self.ReleaseMutex(self.hMutex):
                                        TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                        return (True, '')
                                    return None
                                if None + producer_offset > self.BUFFER_SIZE:
                                    raise ValueError(f'''Possible data corruption, or the producer wrote past the allocated buffer. Producer Offset: {producer_offset}, Header Size: {header_size}''')
                                payload_len = int(producer_offset / ctypes.sizeof(ctypes.c_wchar))
                                payload = (ctypes.c_wchar * payload_len).from_address(self.pBuf + header_size)
                                trace_payload_for_debugging = False
                                raw_bytes = ctypes.string_at(payload, payload_len * ctypes.sizeof(ctypes.c_wchar))
                                
                                try:
                                    content = raw_bytes.decode('utf-16')
                                    
                                    try:
                                        pass
                                    except UnicodeDecodeError:
                                        trace_payload_for_debugging = True
                                        report_exception(severity = Severity.WARN, component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
                                        content = raw_bytes.decode('utf-16', errors = 'replace')
                                        
                                        try:
                                            pass
                                        try:
                                            if trace_payload_for_debugging:
                                                TRACE('!! Payload with utf-16 encoding errors: %s', content)
                                            if not self.reset_producer_offset():
                                                TRACE('!! Failed to reset producer offset.')
                                            if not self.ReleaseMutex(self.hMutex):
                                                TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                                return (True, content)
                                        except IOError:
                                            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
                                            raise 
                                            except Exception:
                                                e = None
                                                report_exception(severity = Severity.WARN, component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
                                                TRACE('!! Read operation failed with error: %s', str(e))
                                                
                                                try:
                                                    e = None
                                                    del e
                                                    if not self.ReleaseMutex(self.hMutex):
                                                        TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())
                                                        return (False, None)
                                                    return None
                                                    e = None
                                                    del e
                                                    
                                                    try:
                                                        pass
                                                    except:
                                                        if not self.ReleaseMutex(self.hMutex):
                                                            TRACE('!! ReleaseMutex failed. Error: %d', ctypes.GetLastError())











    
    def reset_producer_offset(self):
        
        try:
            producer_offset_ptr = ctypes.c_uint32.from_address(self.pBuf + ctypes.sizeof(ctypes.c_uint32))
            producer_offset_ptr.value = 0
            return True
        except Exception:
            e = None
            TRACE('!! Failed to reset producer offset: %s', str(e))
            e = None
            del e
            return False
            e = None
            del e


    
    def read_and_wait_for_signal(self):
        (success, content) = self.read()
        if not success:
            TRACE('!! Failed to read data')
        else:
            
            try:
                self.read_callback(content)
            except Exception:
                callback_error = None
                TRACE('!! Error in line callback: %s', str(callback_error))
                callback_error = None
                del callback_error
                return None
                callback_error = None
                del callback_error

            wait_result = self.WaitForSingleObject(self.hEvent, self.INFINITE)
            if self.is_interrupted:
                return None
            if None == self.WAIT_OBJECT_0:
                time.sleep(self.DELAY_CONSUMING_POST_EVENT_SIGNAL)
                self.ResetEvent(self.hEvent)
                return None
            TRACE('!! Wait failed with result: %d', wait_result)
            return None


