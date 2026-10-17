# Source Generated with Decompyle++
# File: wpad_proxy_win.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional, Text
from winffi.winhttp.api import ffi, lib, WINHTTP_NO_PROXY_BYPASS, WINHTTP_NO_PROXY_NAME
from dropbox.client.proxy.wpad_proxy_base import WpadProxyBase
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.trace import TRACE

class WpadProxyWin(WpadProxyBase):
    
    def __init__(self):
        self.wpad_handle = None

    
    def _release_handle(self):
        if self.wpad_handle:
            if not lib.WinHttpCloseHandle(self.wpad_handle):
                TRACE("!! Couldn't close WPAD HTTP handle: %r", lib.GetLastError())
            self.wpad_handle = None
            return None

    
    def __del__(self):
        
        try:
            self._release_handle()
            return None
        except Exception:
            report_exception(component = DesktopComponent.NETWORKING)
            return None


    
    def _string_from_ffi_string(self, cdata):
        if not cdata:
            return None
        ret = ffi.string(cdata)
        lib.GlobalFree(cdata)
        return ret

    parse_proxy_list = (lambda plist = None, url = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_proxy_for_url(self, dest_url, options):
        info = ffi.new('WINHTTP_PROXY_INFO*')
    # WARNING: Decompyle incomplete

    
    def get_address(self, dest_url):
