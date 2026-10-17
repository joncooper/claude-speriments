# Source Generated with Decompyle++
# File: blacklist.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, Optional, Sequence, Text
from dropbox.infinite import infinite_stubfolders_enabled
from dropbox.infinite.pager import PageRequest, PageResponse, PagerRequestType
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
FALLBACK_BLACK_LIST_MAC = ('Dropbox', 'quicklookd', 'com.apple.quicklook.ThumbnailsAgent', 'QuickLookUIHelper', 'QuickLookSatellite', 'QuickLookUIService', 'com.apple.WebKit.WebContent', 'ubd')
FALLBACK_PASSTHROUGH_LIST_MAC = ('Finder', 'mv', 'rm', 'ls', 'CoreServicesUIAgent', 'Locum', 'lsd', 'fseventsd', 'dbfseventsd', 'com.apple.appkit.xpc.openAndSavePanelService', 'garcon', 'stat', 'find', 'DesktopServicesHelper', 'mds', 'mdworker', 'mdworker32', 'mdworker_shared')
FALLBACK_BLACK_LIST_WIN = ('svchost.exe', 'vmtoolsd.exe', 'WRSA.exe', 'SavService.exe', 'ekrn.exe')
FALLBACK_PASSTHROUGH_LIST_WIN: 'Sequence[Text]' = ()
FALLBACK_BLACK_LIST_LINUX: 'Sequence[Text]' = ()
FALLBACK_PASSTHROUGH_LIST_LINUX = ('nautilus', 'evince-thumbnai')
FALLBACK_STUBFOLDER_ALLOWED_LIST_MAC = ('Finder',)

class InfiniteModuleBlacklist(object):
    
    def __init__(self = None, black_list = None):
