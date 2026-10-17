# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

from __future__ import absolute_import
import os
import platform
import plistlib
from functools import total_ordering
from typing import Dict, Optional, Tuple
from xml.parsers.expat import ExpatError
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
SYSTEM_VERSION_LOCATION = '/System/Library/CoreServices/SystemVersion.plist'
MacVersion = <NODE:12>()

def _get_version():
    info = platform.mac_ver()[0].split('.', 2)
    (major, minor) = info[:2]
    point_release = info[2] if len(info) >= 3 else '0'
    return MacVersion((int(major), int(minor)), point_release = point_release)


def _get_build_number():
    if os.path.exists(SYSTEM_VERSION_LOCATION):
        
        try:
            version_file = open(SYSTEM_VERSION_LOCATION, 'rb')
            version_plist = plistlib.load(version_file)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            
                            try:
                                build_number = version_plist['ProductBuildVersion']
                                TRACE('!! Current OS Build Number: %r', build_number)
                                return build_number
                            except KeyError:
                                
                                try:
                                    return None
                                    
                                    try:
                                        pass
                                    except ExpatError:
                                        return None
                                        return None








TIGER = MacVersion((10, 4), 'Tiger')
LEOPARD = MacVersion((10, 5), 'Leopard')
SNOW_LEOPARD = MacVersion((10, 6), 'Snow Leopard')
LION = MacVersion((10, 7), 'Lion')
MOUNTAIN_LION = MacVersion((10, 8), 'Mountain Lion')
MAVERICKS = MacVersion((10, 9), 'Mavericks')
YOSEMITE = MacVersion((10, 10), 'Yosemite')
EL_CAPITAN = MacVersion((10, 11), 'El Capitan')
SIERRA = MacVersion((10, 12), 'Sierra')
HIGH_SIERRA = MacVersion((10, 13), 'High Sierra')
MOJAVE = MacVersion((10, 14), 'Mojave')
CATALINA = MacVersion((10, 15), 'Catalina')
BIG_SUR = MacVersion((11, 0), 'Big Sur')
MONTEREY = MacVersion((12, 0), 'Monterey')
MONTEREY_1203 = MacVersion((12, 3), 'Monterey')
MONTEREY_1205 = MacVersion((12, 5), 'Monterey')
VENTURA = MacVersion((13, 0), 'Ventura')
VENTURA_13_2 = MacVersion((13, 2), 'Ventura')
VENTURA_13_3 = MacVersion((13, 3), 'Ventura')
VENTURA_13_4 = MacVersion((13, 4), 'Ventura')
SONOMA_14_0 = MacVersion((14, 0), 'Sonoma')
SONOMA_14_1 = MacVersion((14, 1), 'Sonoma')
SONOMA_14_3 = MacVersion((14, 3), 'Sonoma')
SONOMA_14_4 = MacVersion((14, 4), 'Sonoma')
SEQUOIA = MacVersion((15, 0), 'Sequoia')
TAHOE_16 = MacVersion((16, 0), 'Tahoe')
TAHOE_26_1 = MacVersion((26, 1), 'Tahoe')
GOLDEN_GATE = MacVersion((27, 0), 'Golden Gate')
if IS_MAC:
    MAC_VERSION = _get_version()
    MAC_BUILD = _get_build_number()
    return None
