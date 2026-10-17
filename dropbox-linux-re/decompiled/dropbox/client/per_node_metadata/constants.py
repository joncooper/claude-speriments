# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from dropbox.base.enum import StrEnum

class SupportedExtension(StrEnum):
    DBX_BACKUP = '.dbx-backup'
    DBX_PASSWORDS = '.dbx-passwords'
    DBX_VAULT = '.dbx-vault'
    
    def __str__(self = None):
        return self.value


