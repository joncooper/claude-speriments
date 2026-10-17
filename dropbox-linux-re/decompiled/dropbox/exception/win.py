# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

import win32api
import win32con
import win32file

class SavedExceptionHandle:
    
    def __init__(self = None, path = None):
        self.handle = win32file.CreateFile(path, win32con.GENERIC_WRITE, win32con.FILE_SHARE_DELETE, None, win32con.CREATE_NEW, win32con.FILE_ATTRIBUTE_NORMAL, None)
        if self.handle == win32file.INVALID_HANDLE_VALUE:
            raise WindowsError(win32api.GetLastError())
        self.path = path

    
    def write(self = None, contents = None):
        win32file.WriteFile(self.handle, contents)

    
    def remove(self = None):
        
        try:
            win32file.DeleteFile(self.path)
            win32file.CloseHandle(self.handle)
            return None
        except:
            win32file.CloseHandle(self.handle)



