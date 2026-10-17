# Source Generated with Decompyle++
# File: office_coauthoring.pyc (Python 3.11)

from build_number.platform import IS_WINDOWS
from dropbox.harmony.models.types import ApplicationID
from dropbox.pap.events.enums.microsoft_office_app_pb2 import MicrosoftOfficeApp
if IS_WINDOWS:
    from pynt.constants import HKEY_CURRENT_USER, KEY_READ, KEY_WOW64_64KEY
    from pynt.helpers.registry import registry_key, safe_read_registry_value
SUPPORTED_PRODUCT_IDS = [
    'o365proplusretail',
    'o365businessretail',
    'o365propluseeanoteamsretail']

def office_license_supports_coauthoring():
    
    def inner():
        
        try:
            hkey = registry_key(HKEY_CURRENT_USER, 'Software\\Microsoft\\Office\\16.0\\Common\\Licensing\\LicensingNext', KEY_READ | KEY_WOW64_64KEY)
            for product_id in SUPPORTED_PRODUCT_IDS:
                if safe_read_registry_value(hkey, product_id) > 0:
                    
                    try:
                        None(None, None)
                        return True
                        continue
                        
                        try:
                            None(None, None)
                            return False
                            with None:
                                if not None:
                                    
                                    try:
                                        
                                        try:
                                            return None
                                        except Exception:
                                            return False






    if not hasattr(office_license_supports_coauthoring, '_cache'):
        setattr(office_license_supports_coauthoring, '_cache', inner())
    return getattr(office_license_supports_coauthoring, '_cache')


def get_microsoft_office_application(application_id = None):
    if application_id == 'Word.Application':
        return MicrosoftOfficeApp.WORD
    if None == 'Excel.Application':
        return MicrosoftOfficeApp.EXCEL
    if None == 'Powerpoint.Application':
        return MicrosoftOfficeApp.POWERPOINT
    return None.UNKNOWN

