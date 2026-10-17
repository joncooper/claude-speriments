# Source Generated with Decompyle++
# File: fromfiledevice.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import Any, List
from dropbox.camera import Device
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.trace import TRACE
MAX_READ_SIZE = 4194304

class ReadFromFile(Device):
    
    def delete_files(self = None, fobjs = None):
        TRACE('Deleting %d objects from the camera', len(fobjs))
        for fobj in fobjs:
            os.remove(fobj.srcpath)
            except Exception:
                report_exception(component = DesktopComponent.CAMERA_UPLOAD)
                continue
            return None


