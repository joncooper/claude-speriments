# Source Generated with Decompyle++
# File: office_coauthoring.pyc (Python 3.11)

from build_number.platform import IS_MAC
from dropbox.harmony.models.types import ApplicationID
from dropbox.pap.events.enums.microsoft_office_app_pb2 import MicrosoftOfficeApp
if IS_MAC:
    from Foundation import NSUserDefaults
    from dropbox.mac.internal import autoreleasepool
MICROSOFT_OFFICE_BUNDLE_ID = 'com.microsoft.Office'

def office_license_supports_coauthoring():
    
    try:
        autoreleasepool()
        defaults = NSUserDefaults.alloc().initWithSuiteName_(MICROSOFT_OFFICE_BUNDLE_ID)
        office_activation_license = defaults.stringForKey_('OfficeActivationLicense')
        supported_office_activation_license = office_activation_license == 'Subscription'
        ocsp_last_user_id = defaults.stringForKey_('OCPS-LastSuccessfulUserId')
        if ocsp_last_user_id is not None:
            user_under_office_cloud_policy = len(ocsp_last_user_id) > 0
            if not supported_office_activation_license:
                
                try:
                    None(None, None)
                    return 
                    with None:
                        if not None, user_under_office_cloud_policy:
                            
                            try:
                                
                                try:
                                    return None
                                except Exception:
                                    return False






def get_microsoft_office_application(application_id = None):
    if application_id == 'com.microsoft.Word':
        return MicrosoftOfficeApp.WORD
    if None == 'com.microsoft.Excel':
        return MicrosoftOfficeApp.EXCEL
    if None == 'com.microsoft.Powerpoint':
        return MicrosoftOfficeApp.POWERPOINT
    return None.UNKNOWN

