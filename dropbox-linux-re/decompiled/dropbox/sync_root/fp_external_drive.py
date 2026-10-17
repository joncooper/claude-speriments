# Source Generated with Decompyle++
# File: fp_external_drive.pyc (Python 3.11)

import errno
from dataclasses import dataclass
from typing import List, Optional
from dropbox.platform import IS_MAC
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, SEQUOIA
NSFileProviderVolumeUnsupportedReasonNone = 0
NSFileProviderVolumeUnsupportedReasonUnknown = 1
NSFileProviderVolumeUnsupportedReasonNonAPFS = 2
NSFileProviderVolumeUnsupportedReasonNonEncrypted = 4
NSFileProviderVolumeUnsupportedReasonReadOnly = 8
NSFileProviderVolumeUnsupportedReasonNetwork = 16
NSFileProviderVolumeUnsupportedReasonQuarantined = 32
FP_EXTERNAL_DRIVE_STORMCROW = 'desktop-sync-fp-external-drive'

def is_account_fp_external_drive_eligible(variant = None):
    if IS_MAC:
        if MAC_VERSION >= SEQUOIA:
            if variant is not None:
                pass
    return variant.upper().strip() == 'ON'

FPExternalDriveInfo = <NODE:12>()
if IS_MAC and MAC_VERSION >= SEQUOIA:
    import objc
    from Foundation import NSFileManager, NSFileProviderManager, NSPOSIXErrorDomain, NSURL, NSVolumeEnumerationSkipHiddenVolumes
    from dropbox.mac.internal import autoreleasepool, MacError
    objc.registerMetaDataForSelector(b'NSFileProviderManager', b'checkDomainsCanBeStored:onVolumeAtURL:unsupportedReason:error:', dict(arguments = {
        2: dict(type_modifier = 'o', null_accepted = True),
        4: dict(type_modifier = 'o', null_accepted = True),
        5: dict(type_modifier = 'o', null_accepted = True) }))
    
    def _check_fp_external_drive_eligibility(volume_url = None):
        autoreleasepool()
        (_, is_eligible, unsupported_reason, error) = NSFileProviderManager.checkDomainsCanBeStored_onVolumeAtURL_unsupportedReason_error_(None, volume_url, None, None)
        if error:
            if error.domain() == NSPOSIXErrorDomain and error.code() == errno.ENOENT:
                None(None, None)
                return None
            raise MacError(error)
        None(None, None)
        return 
        with None:
            if not None, FPExternalDriveInfo(volume_url.path(), is_eligible, unsupported_reason):
                pass


def check_fp_external_drive_eligibility(volume_path = None):
    if IS_MAC or MAC_VERSION < SEQUOIA:
        raise Exception('File Provider external drives are not supported on this platform')
    info = _check_fp_external_drive_eligibility(NSURL.fileURLWithPath_(volume_path))
# WARNING: Decompyle incomplete


def get_fp_external_drives():
    if IS_MAC or MAC_VERSION < SEQUOIA:
        raise Exception('File Provider external drives are not supported on this platform')
    autoreleasepool()
    volume_urls = NSFileManager.defaultManager().mountedVolumeURLsIncludingResourceValuesForKeys_options_(None, NSVolumeEnumerationSkipHiddenVolumes)
    None(None, None)

