# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division
from AppKit import NSColor
from six import add_metaclass
from dropbox.client.ui.common.constants import colors
__all__ = [
    'Colors',
    'ENTER_KEY',
    'ESCAPE_KEY']
ENTER_KEY = '\r'
ESCAPE_KEY = '\x1b'

class MetaColors(type):
    
    def __getattr__(cls, attr):
        if attr not in colors:
            raise AttributeError("Color '%s' is not defined." % attr)
        (r, g, b, a) = colors[attr]
        return MetaColors.__makecolor(r, g, b, a)

    __makecolor = (lambda cls, r, g, b, a = (0, 0, 0, 0): NSColor.colorWithCalibratedRed_green_blue_alpha_(r / 255, g / 255, b / 255, a / 255))()

Colors = <NODE:12>()
