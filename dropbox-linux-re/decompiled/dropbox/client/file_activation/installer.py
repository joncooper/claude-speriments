# Source Generated with Decompyle++
# File: installer.pyc (Python 3.11)

import itertools
from dataclasses import dataclass
from typing import Iterable, List, Optional, Text, Union
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from build_number import is_full_msix
from dropbox.client.cloud_docs.constants import CloudDocsWindowsInstallationStatus
from dropbox.client.cloud_docs.events import report_windows_installation_status
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.ignore_files.constants import IGNORE_RULE_FILE_EXTENSION
from dropbox.client.features.ignore_files.file_opener import get_default_ignore_rules_file_icon
from dropbox.client.per_node_metadata.constants import SupportedExtension as LinkNodeExtension
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.util.win import get_executable
from dropbox.exception.reporting import report_bad_assumption
from dropbox.trace import TRACE
from dropbox.win32._icon_constants import IDI_DROPBOX_CLOUD_DOCS_BINDER, IDI_DROPBOX_CLOUD_DOCS_PAPER, IDI_DROPBOX_CLOUD_DOCS_PAPER_TEMPLATE, IDI_DROPBOX_CLOUD_DOCS_SHORTCUT, IDI_DROPBOX_DEVICE_ANCHOR, IDI_DROPBOX_FILE_EXTENSIONS_PASSWORDS, IDI_DROPBOX_TAG_METRO_DEVICE_FOLDER_GENERIC
from dropbox.win32.file_click_handlers import install_file_click_handler, uninstall_file_click_handler, validate_file_click_handler_installation

class FileTypeDescriptions(UIStrings):
    paper = UI('Dropbox Paper doc')
    paper_template = UI('Dropbox Paper template')
    binder = UI('Dropbox Binder')
    shortcut = UI('Shortcut')
    passwords = UI('Dropbox feature')
    backup = UI('Dropbox feature')
    device_anchor = UI('Dropbox feature')
    ignore_rules = UI('Dropbox Ignore File')

FileTypeInstallParams = <NODE:12>()
DeprecatedFileTypeAssociation = <NODE:12>()

def _get_icon_location(exe_path = None, resource_id = dataclass):
    return exe_path + ',' + str(-1 * resource_id)


def _get_installation_params(exe_path = None, uninstall = None):
    return [
        FileTypeInstallParams('.paper', 'Paper', FileTypeDescriptions.paper if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_CLOUD_DOCS_PAPER) if exe_path else '', False),
        FileTypeInstallParams('.papert', 'PaperT', FileTypeDescriptions.paper_template if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_CLOUD_DOCS_PAPER_TEMPLATE) if exe_path else '', False),
        FileTypeInstallParams('.binder', 'Binder', FileTypeDescriptions.binder if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_CLOUD_DOCS_BINDER) if exe_path else '', False),
        FileTypeInstallParams('.web', 'Shortcut', FileTypeDescriptions.shortcut if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_CLOUD_DOCS_SHORTCUT) if exe_path else '', True),
        FileTypeInstallParams(LinkNodeExtension.DBX_BACKUP, 'Backup', FileTypeDescriptions.backup if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_TAG_METRO_DEVICE_FOLDER_GENERIC) if exe_path else '', False),
        FileTypeInstallParams(LinkNodeExtension.DBX_PASSWORDS, 'Passwords', FileTypeDescriptions.passwords if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_FILE_EXTENSIONS_PASSWORDS) if exe_path else '', False),
        FileTypeInstallParams(EDB_ANCHOR_EXTENSION, 'ExternalBackupLocation', FileTypeDescriptions.device_anchor if not uninstall else '', _get_icon_location(exe_path, IDI_DROPBOX_DEVICE_ANCHOR) if exe_path else '', False),
        FileTypeInstallParams(IGNORE_RULE_FILE_EXTENSION, 'IgnoreRulesFile', FileTypeDescriptions.ignore_rules if not uninstall else '', get_default_ignore_rules_file_icon() if exe_path else '', False)]


def _get_deprecated_params():
    return [
        DeprecatedFileTypeAssociation(LinkNodeExtension.DBX_VAULT, 'Vault', False),
        DeprecatedFileTypeAssociation('.gdoc', 'Gdoc', is_alternative = True),
        DeprecatedFileTypeAssociation('.gsheet', 'Gsheet', is_alternative = True),
        DeprecatedFileTypeAssociation('.gslides', 'Gslides', is_alternative = True)]


def install_file_type_associations(exe_path = None, hive = None):
    for filetype in _get_installation_params(exe_path = exe_path):
        install_file_click_handler(exe_path, filetype.extension, filetype.handler_name, filetype.description, filetype.icon_path, is_alternative = filetype.is_alternative, hive = hive)
        return None


def _validate_file_type_association_installations(exe_path = None, hive = None):
    for filetype in _get_installation_params(exe_path = exe_path):
        is_valid = validate_file_click_handler_installation(exe_path, filetype.extension, filetype.handler_name, filetype.description, filetype.icon_path, is_alternative = filetype.is_alternative, hive = hive)
        if not is_valid:
            return False
        return True


def uninstall_file_type_associations(hive = None):
    filetypes = itertools.chain(_get_deprecated_params(), _get_installation_params(uninstall = True))
    for filetype in filetypes:
        uninstall_file_click_handler(filetype.extension, filetype.handler_name, is_alternative = filetype.is_alternative, hive = hive)
        return None


def repair_file_type_associations_if_needed():
    if is_full_msix():
        return None
    exe_path = get_executable()
    TRACE('Validating Windows file type associations')
    
    try:
        if _validate_file_type_association_installations(exe_path):
            report_windows_installation_status(CloudDocsWindowsInstallationStatus.INSTALLED)
            TRACE('Windows file type associations validated')
            return None
    except Exception:
        report_windows_installation_status(CloudDocsWindowsInstallationStatus.VALIDATION_FAILED)
        raise 
        TRACE("File type associations weren't installed during installation for local machine. Attempting to install for current user.")
        
        try:
            uninstall_file_type_associations(hive = HKEY_CURRENT_USER)
            install_file_type_associations(exe_path, hive = HKEY_CURRENT_USER)
        except Exception:
            report_windows_installation_status(CloudDocsWindowsInstallationStatus.REPAIR_FAILED)
            raise 

        
        try:
            if _validate_file_type_association_installations(exe_path, HKEY_CURRENT_USER):
                report_windows_installation_status(CloudDocsWindowsInstallationStatus.REPAIRED)
                TRACE('Windows file type association installation for current user succeeded.')
                return None
            report_windows_installation_status(CloudDocsWindowsInstallationStatus.REPAIR_FAILED_SILENTLY)
            report_bad_assumption('Windows file type association installation for current user failed.')
            return None
        except Exception:
            report_windows_installation_status(CloudDocsWindowsInstallationStatus.REPAIR_VALIDATION_FAILED)
            raise 



