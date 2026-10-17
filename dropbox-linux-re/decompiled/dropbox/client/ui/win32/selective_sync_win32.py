# Source Generated with Decompyle++
# File: selective_sync_win32.pyc (Python 3.11)

import ctypes
from ctypes import byref, c_int, c_long, c_ssize_t, c_void_p, cast, create_unicode_buffer, POINTER, Structure, windll, WINFUNCTYPE, wintypes
from ctypes.wintypes import ATOM, BOOL, DWORD, HANDLE, HINSTANCE, HWND, INT, LPARAM, LPCWSTR, UINT, WPARAM
from typing import Any, Callable, Dict, List, Optional, Set
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.ui.common.selective_sync_v2 import CheckState, RemoteFolder, SelectiveSyncBase, SelectiveSyncStrings
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from ctypes import c_ssize_t as LONG_PTR, c_ssize_t as LRESULT
    from dropbox.client.main import DropboxApplication
LRESULT = ctypes.c_ssize_t
LONG_PTR = c_ssize_t
windll.user32.SetWindowLongPtrW = getattr(windll.user32, 'SetWindowLongPtrW', windll.user32.SetWindowLongW)
windll.user32.SetWindowLongPtrW.argtypes = [
    HWND,
    c_int,
    LONG_PTR]
windll.user32.SetWindowLongPtrW.restype = LONG_PTR
windll.user32.SendMessageW.argtypes = [
    HWND,
    UINT,
    WPARAM,
    c_void_p]
windll.user32.SendMessageW.restype = LRESULT
windll.user32.CreateWindowExW.argtypes = [
    DWORD,
    LPCWSTR,
    LPCWSTR,
    DWORD,
    c_int,
    c_int,
    c_int,
    c_int,
    HWND,
    HANDLE,
    HINSTANCE,
    c_void_p]
windll.user32.CreateWindowExW.restype = HWND
windll.user32.SetWindowPos.argtypes = [
    HWND,
    HWND,
    c_int,
    c_int,
    c_int,
    c_int,
    UINT]
windll.user32.SetWindowPos.restype = BOOL
windll.user32.EnableWindow.argtypes = [
    HWND,
    BOOL]
windll.user32.EnableWindow.restype = BOOL
windll.user32.DestroyWindow.argtypes = [
    HWND]
windll.user32.DestroyWindow.restype = BOOL
windll.user32.LoadCursorW.argtypes = [
    HINSTANCE,
    c_void_p]
windll.user32.LoadCursorW.restype = HANDLE
windll.user32.GetSysColorBrush.argtypes = [
    c_int]
windll.user32.GetSysColorBrush.restype = HANDLE
windll.user32.GetSystemMetrics.argtypes = [
    c_int]
windll.user32.GetSystemMetrics.restype = c_int
windll.user32.GetWindowRect.argtypes = [
    HWND,
    ctypes.POINTER(wintypes.RECT)]
windll.user32.GetWindowRect.restype = BOOL
windll.user32.GetWindowLongW.argtypes = [
    HWND,
    c_int]
windll.user32.GetWindowLongW.restype = c_long
windll.user32.CallWindowProcW.argtypes = [
    WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM),
    HWND,
    UINT,
    WPARAM,
    LPARAM]
windll.user32.CallWindowProcW.restype = LRESULT
windll.user32.PostQuitMessage.argtypes = [
    c_int]
windll.user32.PostQuitMessage.restype = None
windll.user32.GetSysColor.argtypes = [
    c_int]
windll.user32.GetSysColor.restype = DWORD
windll.user32.GetClientRect.argtypes = [
    HWND,
    ctypes.POINTER(wintypes.RECT)]
windll.user32.GetClientRect.restype = BOOL
windll.user32.FillRect.argtypes = [
    wintypes.HDC,
    ctypes.POINTER(wintypes.RECT),
    HANDLE]
windll.user32.FillRect.restype = c_int
windll.user32.InvalidateRect.argtypes = [
    HWND,
    ctypes.POINTER(wintypes.RECT),
    BOOL]
windll.user32.InvalidateRect.restype = BOOL
windll.user32.UpdateWindow.argtypes = [
    HWND]
windll.user32.UpdateWindow.restype = BOOL
windll.user32.ShowWindow.argtypes = [
    HWND,
    c_int]
windll.user32.ShowWindow.restype = BOOL
windll.user32.GetMessageW.argtypes = [
    ctypes.POINTER(wintypes.MSG),
    HWND,
    UINT,
    UINT]
windll.user32.GetMessageW.restype = BOOL
windll.user32.TranslateMessage.argtypes = [
    ctypes.POINTER(wintypes.MSG)]
windll.user32.TranslateMessage.restype = BOOL
windll.user32.DispatchMessageW.argtypes = [
    ctypes.POINTER(wintypes.MSG)]
windll.user32.DispatchMessageW.restype = LPARAM
windll.gdi32.SetBkColor.argtypes = [
    wintypes.HDC,
    DWORD]
windll.gdi32.SetBkColor.restype = DWORD
SetWindowLongPtr = windll.user32.SetWindowLongPtrW
GWLP_WNDPROC = -4

class WNDCLASS(Structure):
    _fields_ = [
        ('style', UINT),
        ('lpfnWndProc', WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)),
        ('cbClsExtra', c_int),
        ('cbWndExtra', c_int),
        ('hInstance', HINSTANCE),
        ('hIcon', HANDLE),
        ('hCursor', HANDLE),
        ('hbrBackground', HANDLE),
        ('lpszMenuName', LPCWSTR),
        ('lpszClassName', LPCWSTR)]

windll.user32.RegisterClassW.argtypes = [
    ctypes.POINTER(WNDCLASS)]
windll.user32.RegisterClassW.restype = ATOM
WS_OVERLAPPEDWINDOW = 13565952
WS_VISIBLE = 268435456
WS_CHILD = 1073741824
WS_TABSTOP = 65536
WS_BORDER = 8388608
WS_VSCROLL = 2097152
WS_HSCROLL = 1048576
WS_EX_CLIENTEDGE = 512
TVS_HASBUTTONS = 1
TVS_HASLINES = 2
TVS_LINESATROOT = 4
TVS_SHOWSELALWAYS = 32
TVS_EX_PARTIALCHECKBOXES = 128
TV_FIRST = 4352
TVM_INSERTITEM = TV_FIRST + 50
TVM_SETITEM = TV_FIRST + 63
TVM_EXPAND = TV_FIRST + 2
TVM_DELETEITEM = TV_FIRST + 1
TVM_GETNEXTITEM = TV_FIRST + 10
TVM_HITTEST = TV_FIRST + 17
TVM_SETEXTENDEDSTYLE = TV_FIRST + 44
TVGN_CARET = 9
TVIF_TEXT = 1
TVIF_IMAGE = 2
TVIF_STATE = 8
TVIF_CHILDREN = 64
TVN_FIRST = 0xFFFFFE70
TVN_ITEMEXPANDING = TVN_FIRST - 5 & 0xFFFFFFFF
TVN_ITEMCHANGED = TVN_FIRST - 19 & 0xFFFFFFFF
TVIS_EXPANDED = 32
TVIS_STATEIMAGEMASK = 61440
TVIS_UNCHECKED = 1
TVIS_CHECKED = 2
TVIS_INDETERMINATE = 3
TVGN_ROOT = 0
TVGN_CHILD = 4
TVGN_NEXT = 1
TVGN_PARENT = 3
TVI_LAST = 0xFFFFFFFF
TVHT_ONITEMSTATEICON = 64
ICC_TREEVIEW_CLASSES = 2
WM_INITDIALOG = 272
WM_COMMAND = 273
WM_CLOSE = 16
WM_DESTROY = 2
WM_NOTIFY = 78
WM_SIZE = 5
WM_GETMINMAXINFO = 36
WM_CTLCOLORSTATIC = 312
WM_CTLCOLORBTN = 309
WM_ERASEBKGND = 20
WM_SETREDRAW = 11
COLOR_BTNFACE = 15
BS_AUTOCHECKBOX = 3
BM_GETCHECK = 240
BM_SETCHECK = 241
BST_UNCHECKED = 0
BST_CHECKED = 1
BST_INDETERMINATE = 2
BST_NOT_INTERACTIVE = 4
IDOK = 1
IDCANCEL = 2
ID_TREE_VIEW = 100
ID_SELECT_ALL = 101
ID_OK = IDOK
ID_CANCEL = IDCANCEL
ID_INFO_LABEL = 102
DEFAULT_CHARSET = 1
DEFAULT_QUALITY = 0
DEFAULT_PITCH = 0
FF_DONTCARE = 0
WM_SETFONT = 48

class INITCOMMONCONTROLSEX(Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwICC', DWORD)]


class TVITEM(Structure):
    _fields_ = [
        ('mask', UINT),
        ('hItem', HANDLE),
        ('state', UINT),
        ('stateMask', UINT),
        ('pszText', POINTER(ctypes.c_wchar)),
        ('cchTextMax', INT),
        ('iImage', INT),
        ('iSelectedImage', INT),
        ('cChildren', INT),
        ('lParam', LPARAM)]


class TVINSERTSTRUCT(Structure):
    _fields_ = [
        ('hParent', HANDLE),
        ('hInsertAfter', HANDLE),
        ('item', TVITEM)]


class NMHDR(Structure):
    _fields_ = [
        ('hwndFrom', HWND),
        ('idFrom', UINT),
        ('code', UINT)]


class NMTREEVIEW(Structure):
    _fields_ = [
        ('hdr', NMHDR),
        ('action', UINT),
        ('itemOld', TVITEM),
        ('itemNew', TVITEM),
        ('ptDrag', wintypes.POINT)]

DLGPROC = WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
TVE_EXPAND = 2
TVE_COLLAPSE = 1

class TVHITTESTINFO(Structure):
    _fields_ = [
        ('pt', wintypes.POINT),
        ('flags', UINT),
        ('hItem', HANDLE)]

TVHT_ONITEMBUTTON = 16
SWP_NOZORDER = 4
SWP_NOACTIVATE = 16
SWP_DRAWFRAME = 32
SWP_NOSIZE = 1
SWP_NOMOVE = 2

class SelectiveSyncWin32(SelectiveSyncBase):
    
    def _create_default_font(self):
        font_name = 'MS Shell Dlg 2'
        font_buf = create_unicode_buffer(font_name)
        height = -11
        return windll.gdi32.CreateFontW(height, 0, 0, 0, 400, 0, 0, 0, DEFAULT_CHARSET, 0, 0, DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE, cast(font_buf, LPCWSTR))

    
    def __init__(self = None, app = None, account = None):
