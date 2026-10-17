# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum
CONFIG_KEY_EXTERNAL_CONTEXT_MENU_SHARING_CONSENTED = 'external_context_menu_sharing_consented'

class ExternalContextMenuSharingActions(Enum):
    VARIANT_EXPOSURE = 'variant_exposure'
    VIEW_LAUNCHED = 'view_launched'
    COPY_LINK_CLICKED = 'copy_link_clicked'
    COPY_LINK = 'copy_link'
    COPY_LINK_OPTION_SHOWN = 'copy_link_option_shown'
    SHARE_CLICKED = 'share_clicked'
    SHARE_OPTION_SHOWN = 'share_option_shown'


class ExternalContextMenuSharingStormcrowVariants(Enum):
    _missing_ = (lambda cls, value: cls.UNKNOWN)()
    UNKNOWN = 'UNKNOWN'
    OFF = 'OFF'
    CONTROL = 'CONTROL'
    SHARE = 'SHARE'
    COPY_LINK = 'COPY_LINK'
    COPY_LINK_AND_SHARE = 'COPY_LINK_AND_SHARE'


class ExternalContextMenuSharingSource(Enum):
    CONTEXT_MENU = 'context_menu'


class ExternalContextMenuSharingSurface(Enum):
    CONSENT_SCREEN = 'consent_screen'
    INSUFFICIENT_QUOTA_SCREEN = 'insufficient_quota_screen'
    INSUFFICIENT_STORAGE_SCREEN = 'insufficient_storage_screen'

