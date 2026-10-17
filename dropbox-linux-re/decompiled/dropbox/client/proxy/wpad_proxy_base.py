# Source Generated with Decompyle++
# File: wpad_proxy_base.pyc (Python 3.11)

from __future__ import absolute_import
import re
from typing import Optional, Text
from six.moves.urllib import parse as urlparse
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.trace import TRACE

class WpadProxyBase(object):
    
    def get_address(self = None, dest_url = None):
        raise NotImplementedError("Can't run get_address on base class!")

    
    def _sanitize_url(self = None, url = None):
        if '//' not in url:
            return '//' + url

    
    def _should_bypass_proxy(self = None, dest_url = None, bypass_list = None):
        hostname = urlparse.urlparse(self._sanitize_url(dest_url)).hostname
        if not hostname:
            return False
        for bypass_host in None.split(';'):
            if bypass_host == '<local>' and '.' not in hostname:
                TRACE('Bypassing proxy for %r because local hosts are bypassed', dest_url)
                return True
            if None == '*.local' and '.' not in hostname:
                TRACE('Bypassing proxy for %r because local hosts are bypassed', dest_url)
                return True
            bypass_regex = None.replace('.', '\\.').replace('*', '.*').replace('?', '.')
            if re.match(bypass_regex, hostname, re.I):
                TRACE('Bypassing proxy for %r because of rule %r', dest_url, bypass_host)
                return True
            except Exception:
                TRACE("!! Couldn't parse bypass host %r", bypass_host)
                report_exception(component = DesktopComponent.NETWORKING)
                continue
            return False


