# Source Generated with Decompyle++
# File: avatar.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from functools import partial
from typing import Callable, Optional, Text
from AppKit import NSBezierPath, NSColor, NSFont, NSFontAttributeName, NSForegroundColorAttributeName, NSImage, NSMakeRect, NSMakeSize, NSMutableParagraphStyle, NSParagraphStyleAttributeName, NSSize, NSString, NSTextAlignmentCenter
from dropbox.client.background_worker import on_background_thread
from dropbox.client.ui.cocoa.util import ImageCache
from dropbox.client.ui.common.colors import color_value_for_avatar
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.mac.internal import autoreleasepool
DEFAULT_AVATAR_SIZE = 32
DEFAULT_FONT_SIZE = 13

def get_avatar_image_async(callback, avatar_url = None, initials = None, account_id = None, size = (DEFAULT_AVATAR_SIZE, DEFAULT_FONT_SIZE), font_size = ('callback', 'Callable[[NSImage], None]', 'avatar_url', 'Optional[Text]', 'initials', 'Text', 'account_id', 'Text', 'size', 'int', 'font_size', 'int', 'return', 'None')):
    if avatar_url:
        image_cache = ImageCache.sharedCache()
        image_cache.get(avatar_url, partial(_on_loaded_avatar_web, callback, initials, account_id), size = NSSize(size, size))
        return None
    _generate_initials_image_async(callback, initials, account_id, size, font_size)

_generate_initials_image_async = (lambda callback = None, initials = None, account_id = on_background_thread, size = (DEFAULT_AVATAR_SIZE, DEFAULT_FONT_SIZE), font_size = ('callback', 'Callable[[NSImage], None]', 'initials', 'Text', 'account_id', 'Text', 'size', 'int', 'font_size', 'int', 'return', 'None'): autoreleasepool()rect = NSMakeRect(0, 0, size, size)image = NSImage.alloc().initWithSize_(NSMakeSize(size, size))if not image:
None(None, None)NoneNone.lockFocus()if account_id.startswith('dbid:'):
account_id = account_id[len('dbid:'):](red, green, blue) = color_value_for_avatar(account_id)NSColor.colorWithCalibratedRed_green_blue_alpha_(red / 255, green / 255, blue / 255, 1).setFill()NSBezierPath.bezierPathWithOvalInRect_(rect).fill()paragraph_style = NSMutableParagraphStyle.alloc().init()if not paragraph_style:
None(None, None)NoneNone.setAlignment_(NSTextAlignmentCenter)font = NSFont.systemFontOfSize_(font_size)attributes = {
NSFontAttributeName: font,
NSParagraphStyleAttributeName: paragraph_style,
NSForegroundColorAttributeName: NSColor.whiteColor() }initials_string = NSString.stringWithString_(initials)text_size = initials_string.sizeWithAttributes_(attributes)text_rect = recttext_rect.origin.y = text_rect.origin.y + 0.5 * (text_rect.size.height - text_size.height) + 1text_rect.size.height = text_size.heightinitials_string.drawInRect_withAttributes_(text_rect, attributes)image.unlockFocus()callback(image)None(None, None)Nonewith None:
if not None:
pass)()
_on_loaded_avatar_web = (lambda callback = None, initials = None, account_id = on_ui_thread, image = ('callback', 'Callable', 'initials', 'Text', 'account_id', 'Text', 'image', 'NSImage', 'return', 'None'): if image:
callback(image)None_generate_initials_image_async(callback, initials, account_id))()
