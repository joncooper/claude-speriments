# Source Generated with Decompyle++
# File: strings.pyc (Python 3.11)

from dropbox.client.ui.common.strings import UI, UIStrings

class EncryptedFolderStrings(UIStrings):
    fingerprint_verification_dialog_caption = UI('Verify security codes to register your device')
    fingerprint_verification_dialog_message = UI('Work directly with your admin to:<br /><br />1. Verify this team code matches that of your admin:<br />%(team_key_fingerprint)s<br /><br />2. If the team code matches, share your device code:<br />%(client_key_fingerprint)s<br /><br />If the team code matches, select Verified team code. The team code is then stored on your device for future reference.')
    fingerprint_verification_dialog_approve = UI('Verified team code')
    fingerprint_mismatch_error_dialog_caption = UI('This device lost access to encrypted folders')
    fingerprint_mismatch_error_dialog_message = UI('The team code stored locally on this device is no longer valid and must be replaced to access encrypted folders. Work with your admin to verify the new team code and replace the invalid one. This will register your device again.')
    fingerprint_mismatch_error_dialog_forget_button = UI('Replace team code…')
    forget_fingerprint_warning_dialog_caption = UI('Replace team code')
    forget_fingerprint_warning_dialog_message = UI('Confirm that you would like to replace the team code stored locally on this device. Your team admin should share the new team code with you. You will be logged out of Dropbox. When you log back in, you will receive a notification to verify the new team code.')
    forget_fingerprint_warning_dialog_unlink = UI('Replace team code')
    forget_fingerprint_warning_dialog_cancel = UI('Cancel')
    fingerprint_dialog_close = UI('Close')
    display_fingerprints_dialog_caption = UI('Your security codes')
    display_fingerprints_verification_disabled_message = UI('You do not have any security codes because your admin chose to use automatic device registration for access to encrypted folders.')
    display_fingerprints_verification_enabled_message = UI('Make sure the team code stored on this device matches that of your admin. If it matches, you can share your device code with them.<br /><br />Team code:<br />%(team_key_fingerprint)s<br /><br />Device code:<br />%(client_key_fingerprint)s')

