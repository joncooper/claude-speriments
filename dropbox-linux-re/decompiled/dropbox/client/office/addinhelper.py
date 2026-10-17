# Source Generated with Decompyle++
# File: addinhelper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.office.base import BaseOfficeAddInHelper, BaseOfficeAddInHelperFactory
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from dropbox.client.office.win.addinhelper import WinOfficeAddInHelper, WinOfficeAddInHelperFactory
    OfficeAddInHelper = WinOfficeAddInHelper
    OfficeAddInHelperFactory = WinOfficeAddInHelperFactory
    return None
OfficeAddInHelper = None
OfficeAddInHelperFactory = BaseOfficeAddInHelperFactory
