# Source Generated with Decompyle++
# File: system_info.pyc (Python 3.11)

from __future__ import absolute_import
import os
import re
import subprocess
from typing import Dict, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_LINUX, platform
from dropbox.trace import TRACE
if IS_LINUX:
    from lib.linuxffi.gnu.api import get_glibc_version
    from dropbox.client.util.linux import get_loaded_libraries

def report_system_info():
    if IS_LINUX:
        report_linux_system_info()
        return None


def report_linux_system_info():
    info = get_linux_system_info()
# WARNING: Decompyle incomplete


def get_linux_system_info():
    lsb_raw = None
    
    try:
        lsb_raw = subprocess.check_output([
            'lsb_release',
            '-a'], stderr = subprocess.STDOUT).decode('utf8')
    except FileNotFoundError:
        TRACE("Can't get system info, missing lsb_release")
    except Exception:
        report_exception(severity = Severity.DEBUG, component = DesktopComponent.BUILD_SYSTEM)

    
    try:
        inp = open('/proc/version', 'r')
        proc_raw = inp.read()
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except Exception:
                        proc_raw = None

                    
                    try:
                        disp = bool(os.environ['DISPLAY'])
                    except Exception:
                        disp = None

                    lsb_dict = { }
                    if lsb_raw:
                        for line in lsb_raw.split('\n'):
                            res = line.split(':', 1)
                            if len(res) == 2:
                                lsb_dict[res[0].strip()] = res[1].strip()
                            proc_dict = { }
                            if proc_raw:
                                m = re.match('Linux version ([^\\s]*) \\(([^\\s]*)\\) \\((.*)\\) (.*)', proc_raw)
                                if m:
                                    proc_dict = {
                                        'linux_version': m.group(1),
                                        'build_machine': m.group(2),
                                        'gcc_version': m.group(3),
                                        'build_date': m.group(4) }



# WARNING: Decompyle incomplete

