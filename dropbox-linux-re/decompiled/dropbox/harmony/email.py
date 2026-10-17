# Source Generated with Decompyle++
# File: email.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import List, Optional, Text
from six.moves.urllib.parse import quote
from dropbox.platform import IS_MAC, IS_WINDOWS

def _open_mailto_win(mailto_string = None):
    
    try:
        os.startfile(mailto_string)
        return True
    except WindowsError:
        return False



def _open_mailto_mac(mailto_string = None):
    NSWorkspace = NSWorkspace
    import AppKit
    NSURL = NSURL
    import Foundation
    autoreleasepool = autoreleasepool
    import dropbox.mac.internal
    autoreleasepool()
    url = NSURL.URLWithString_(mailto_string)
    None(None, None)
    return 
    with None:
        if not None, NSWorkspace.sharedWorkspace().openURL_(url):
            pass


def _format_mailto(address = None, **kwargs):
    parts = []
    for headername in ('subject', 'body', 'attach'):
        if headername in kwargs:
            headervalue = kwargs[headername]
            if not headervalue:
                continue
            parts.append(f'''{headername!s}={quote(headervalue.encode('utf-8'), safe = '')!s}''')
        mailto_string = 'mailto:%s' % quote(address, safe = '')
        if parts:
            mailto_string += '?' + '&'.join(parts)
    return mailto_string


def open_email(address = None, subject = None, body = None, attach = (None, None, None)):
    mailto_string = _format_mailto(address, subject = subject, body = body, attach = attach)
    success = False
    if IS_WINDOWS:
        success = _open_mailto_win(mailto_string)
    elif IS_MAC:
        success = _open_mailto_mac(mailto_string)
    return success

