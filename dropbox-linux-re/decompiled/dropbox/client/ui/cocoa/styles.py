# Source Generated with Decompyle++
# File: styles.pyc (Python 3.11)

import objc
from AppKit import NSCenterTextAlignment, NSColor as AppKitNSColor, NSFont, NSFontAttributeName, NSForegroundColorAttributeName, NSMutableAttributedString, NSMutableParagraphStyle, NSParagraphStyleAttributeName
from Quartz import CGColorCreate, CGColorCreateCopyWithAlpha, CGColorRef, CGColorSpaceCreateWithName, CIColor, kCGColorSpaceSRGB
COLORSPACE_SRGB = CGColorSpaceCreateWithName(kCGColorSpaceSRGB)

def CGColorCreateHex(value):
    return CGColorCreate(COLORSPACE_SRGB, [
        ((value & 16711680) >> 16) / 255,
        ((value & 65280) >> 8) / 255,
        (value & 255) / 255,
        1])

COLOR_NOTIFICATION_BADGE = AppKitNSColor.colorWithCalibratedRed_green_blue_alpha_(1, 0.168627, 0.101961, 1)
COLOR_NOTIFICATION_BADGE_DARK = AppKitNSColor.colorWithCalibratedRed_green_blue_alpha_(0.54902, 0, 0, 1)
COLOR_DROPBOX_BLACK = CGColorCreateHex(2435115)
COLOR_DROPBOX_LIGHT_BLACK = CGColorCreateCopyWithAlpha(COLOR_DROPBOX_BLACK, 0.225)
COLOR_DROPBOX_BLUE = CGColorCreateHex(32485)
COLOR_DROPBOX_SUBTEXT_GRAY = CGColorCreateHex(6316128)
COLOR_DROPBOX_DARK_GRAY = CGColorCreateHex(4015693)
COLOR_DROPBOX_LIGHT_GRAY = CGColorCreateHex(4674141)
COLOR_DROPBOX_LIGHTER_GREY = CGColorCreateHex(8096148)
COLOR_DROPBOX_GREEN = CGColorCreateHex(1687056)
COLOR_DROPBOX_RED = CGColorCreateHex(13959199)
COLOR_DROPBOX_WHITE = CGColorCreateHex(16777215)
COLOR_TRANSPARENT = CGColorCreateCopyWithAlpha(COLOR_DROPBOX_WHITE, 0)
COLOR_HARMONY_GREY = CGColorCreateHex(8096148)
COLOR_HARMONY_RED = CGColorCreateHex(12850959)
COLOR_HARMONY_ORANGE = CGColorCreateHex(15887872)
COLOR_HARMONY_DIVIDER_STROKE_COLOR = CGColorCreateCopyWithAlpha(COLOR_DROPBOX_BLACK, 0.15)
COLOR_SELSYNC_WARNING_YELLOW = CGColorCreateHex(16774604)

def NSColor():
    '''NSColor'''
    colorWithCGColor_ = (lambda cls = None, color = None: NSColor.colorWithCIColor_(CIColor.colorWithCGColor_(color)))()

NSColor = <NODE:27>(NSColor, 'NSColor', objc.Category(AppKitNSColor))
_HELVETICA_FONT = NSFont.fontWithName_size_('Helvetica Neue', 13)

def default_attributed_string(text, color, font, alignment = (None, NSCenterTextAlignment)):
