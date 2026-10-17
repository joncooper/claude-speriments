# Source Generated with Decompyle++
# File: bubbler_strings.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Text, Type, Union
from dropbox.client.ui.common.strings import AccountString, UI, UIStrings
from dropbox.i18n import ungettext

class SyncEngineStrings(UIStrings):
    added = AccountString('"%(filename)s" was added to your <personal> Dropbox.')
    shared_folder_added = AccountString("Take a look at what's in this shared folder.")
    infinite_shared_folder_added = AccountString('This shared folder is online-only.')
    success = AccountString('<Personal> Dropbox synced')
    app_folder_added = AccountString('The app folder "%(folder_name)s" was created in your <personal> Dropbox.')
    removed = AccountString('"%(filename)s" was removed from your <personal> Dropbox.')
    shared_folder_removed = AccountString('The shared folder "%(folder_name)s" was removed from your <personal> Dropbox.')
    app_folder_removed = AccountString('The app folder "%(folder_name)s" was removed from your <personal> Dropbox.')
    cdm_shared_folder_added = UI('You can find this shared folder in your member folder.')
    cdm_infinite_shared_folder_added = UI('This shared folder is online-only. You can find it in your member folder.')
    title_file_added = UI('%(name)s added')
    title_files_added = (lambda num_changes = None: ungettext('%(num)s file added', '%(num)s files added', num_changes))()
    title_file_deleted = UI('%(name)s deleted')
    title_files_deleted = (lambda num_changes = None: ungettext('%(num)s file deleted', '%(num)s files deleted', num_changes))()
    title_file_changed = UI('%(name)s changed')
    title_files_changed = (lambda num_changes = None: ungettext('%(num)s file changed', '%(num)s files changed', num_changes))()


class SyncEngineMessageAddedShortStrings(UIStrings):
    you = UI('You added %(filename)s')
    you_others = UI('You and others added %(filename)s')
    other = UI('%(user)s added %(filename)s')
    others = UI('%(user)s and others added %(filename)s')
    plural_you = (lambda num = None: ungettext('You added %(num)s file', 'You added %(num)s files', num))()
    plural_you_others = (lambda num = None: ungettext('You and others added %(num)s file', 'You and others added %(num)s files', num))()
    plural_other = (lambda num = None: ungettext('%(user)s added %(num)s file', '%(user)s added %(num)s files', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others added %(num)s file', '%(user)s and others added %(num)s files', num))()


class SyncEngineMessageDeletedShortStrings(UIStrings):
    you = UI('You deleted %(filename)s')
    you_others = UI('You and others deleted %(filename)s')
    other = UI('%(user)s deleted %(filename)s')
    others = UI('%(user)s and others deleted %(filename)s')
    plural_you = (lambda num = None: ungettext('You deleted %(num)s file', 'You deleted %(num)s files', num))()
    plural_you_others = (lambda num = None: ungettext('You and others deleted %(num)s file', 'You and others deleted %(num)s files', num))()
    plural_other = (lambda num = None: ungettext('%(user)s deleted %(num)s file', '%(user)s deleted %(num)s files', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others deleted %(num)s file', '%(user)s and others deleted %(num)s files', num))()


class SyncEngineMessageChangedShortStrings(UIStrings):
    you = UI('You changed %(filename)s')
    you_others = UI('You and others changed %(filename)s')
    other = UI('%(user)s changed %(filename)s')
    others = UI('%(user)s and others changed %(filename)s')
    plural_you = (lambda num = None: ungettext('You changed %(num)s file', 'You changed %(num)s files', num))()
    plural_you_others = (lambda num = None: ungettext('You and others changed %(num)s file', 'You and others changed %(num)s files', num))()
    plural_other = (lambda num = None: ungettext('%(user)s changed %(num)s file', '%(user)s changed %(num)s files', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others changed %(num)s file', '%(user)s and others changed %(num)s files', num))()


class SyncEngineMessageAddedStrings(UIStrings):
    you = UI('You added %(filename)s to your Dropbox.')
    you_others = UI('You and others added %(filename)s to your Dropbox.')
    other = UI('%(user)s added %(filename)s to your Dropbox.')
    others = UI('%(user)s and others added %(filename)s to your Dropbox.')
    plural_you = (lambda num = None: ungettext('You added %(num)s file to your Dropbox.', 'You added %(num)s files to your Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others added %(num)s file to your Dropbox.', 'You and others added %(num)s files to your Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s added %(num)s file to your Dropbox.', '%(user)s added %(num)s files to your Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others added %(num)s file to your Dropbox.', '%(user)s and others added %(num)s files to your Dropbox.', num))()


class SyncEngineMessageDeletedStrings(UIStrings):
    you = UI('You deleted %(filename)s from your Dropbox.')
    you_others = UI('You and others deleted %(filename)s from your Dropbox.')
    other = UI('%(user)s deleted %(filename)s from your Dropbox.')
    others = UI('%(user)s and others deleted %(filename)s from your Dropbox.')
    plural_you = (lambda num = None: ungettext('You deleted %(num)s file from your Dropbox.', 'You deleted %(num)s files from your Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others deleted %(num)s file from your Dropbox.', 'You and others deleted %(num)s files from your Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s deleted %(num)s file from your Dropbox.', '%(user)s deleted %(num)s files from your Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others deleted %(num)s file from your Dropbox.', '%(user)s and others deleted %(num)s files from your Dropbox.', num))()


class SyncEngineMessageChangedStrings(UIStrings):
    you = UI('You changed %(filename)s in your Dropbox.')
    you_others = UI('You and others changed %(filename)s in your Dropbox.')
    other = UI('%(user)s changed %(filename)s in your Dropbox.')
    others = UI('%(user)s and others changed %(filename)s in your Dropbox.')
    plural_you = (lambda num = None: ungettext('You changed %(num)s file in your Dropbox.', 'You changed %(num)s files in your Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others changed %(num)s file in your Dropbox.', 'You and others changed %(num)s files in your Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s changed %(num)s file in your Dropbox.', '%(user)s changed %(num)s files in your Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others changed %(num)s file in your Dropbox.', '%(user)s and others changed %(num)s files in your Dropbox.', num))()


class SyncEngineMessagePersonalAddedStrings(UIStrings):
    you = UI('You added %(filename)s to your personal Dropbox.')
    you_others = UI('You and others added %(filename)s to your personal Dropbox.')
    other = UI('%(user)s added %(filename)s to your personal Dropbox.')
    others = UI('%(user)s and others added %(filename)s to your personal Dropbox.')
    plural_you = (lambda num = None: ungettext('You added %(num)s file to your personal Dropbox.', 'You added %(num)s files to your personal Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others added %(num)s file to your personal Dropbox.', 'You and others added %(num)s files to your personal Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s added %(num)s file to your personal Dropbox.', '%(user)s added %(num)s files to your personal Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others added %(num)s file to your personal Dropbox.', '%(user)s and others added %(num)s files to your personal Dropbox.', num))()


class SyncEngineMessagePersonalDeletedStrings(UIStrings):
    you = UI('You deleted %(filename)s from your personal Dropbox.')
    you_others = UI('You and others deleted %(filename)s from your personal Dropbox.')
    other = UI('%(user)s deleted %(filename)s from your personal Dropbox.')
    others = UI('%(user)s and others deleted %(filename)s from your personal Dropbox.')
    plural_you = (lambda num = None: ungettext('You deleted %(num)s file from your personal Dropbox.', 'You deleted %(num)s files from your personal Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others deleted %(num)s file from your personal Dropbox.', 'You and others deleted %(num)s files from your personal Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s deleted %(num)s file from your personal Dropbox.', '%(user)s deleted %(num)s files from your personal Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others deleted %(num)s file from your personal Dropbox.', '%(user)s and others deleted %(num)s files from your personal Dropbox.', num))()


class SyncEngineMessagePersonalChangedStrings(UIStrings):
    you = UI('You changed %(filename)s in your personal Dropbox.')
    you_others = UI('You and others changed %(filename)s in your personal Dropbox.')
    other = UI('%(user)s changed %(filename)s in your personal Dropbox.')
    others = UI('%(user)s and others changed %(filename)s in your personal Dropbox.')
    plural_you = (lambda num = None: ungettext('You changed %(num)s file in your personal Dropbox.', 'You changed %(num)s files in your personal Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others changed %(num)s file in your personal Dropbox.', 'You and others changed %(num)s files in your personal Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s changed %(num)s file in your personal Dropbox.', '%(user)s changed %(num)s files in your personal Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others changed %(num)s file in your personal Dropbox.', '%(user)s and others changed %(num)s files in your personal Dropbox.', num))()


class SyncEngineMessageBusinessAddedStrings(UIStrings):
    you = UI('You added %(filename)s to your business Dropbox.')
    you_others = UI('You and others added %(filename)s to your business Dropbox.')
    other = UI('%(user)s added %(filename)s to your business Dropbox.')
    others = UI('%(user)s and others added %(filename)s to your business Dropbox.')
    plural_you = (lambda num = None: ungettext('You added %(num)s file to your business Dropbox.', 'You added %(num)s files to your business Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others added %(num)s file to your business Dropbox.', 'You and others added %(num)s files to your business Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s added %(num)s file to your business Dropbox.', '%(user)s added %(num)s files to your business Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others added %(num)s file to your business Dropbox.', '%(user)s and others added %(num)s files to your business Dropbox.', num))()


class SyncEngineMessageBusinessDeletedStrings(UIStrings):
    you = UI('You deleted %(filename)s from your business Dropbox.')
    you_others = UI('You and others deleted %(filename)s from your business Dropbox.')
    other = UI('%(user)s deleted %(filename)s from your business Dropbox.')
    others = UI('%(user)s and others deleted %(filename)s from your business Dropbox.')
    plural_you = (lambda num = None: ungettext('You deleted %(num)s file from your business Dropbox.', 'You deleted %(num)s files from your business Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others deleted %(num)s file from your business Dropbox.', 'You and others deleted %(num)s files from your business Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s deleted %(num)s file from your business Dropbox.', '%(user)s deleted %(num)s files from your business Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others deleted %(num)s file from your business Dropbox.', '%(user)s and others deleted %(num)s files from your business Dropbox.', num))()


class SyncEngineMessageBusinessChangedStrings(UIStrings):
    you = UI('You changed %(filename)s in your business Dropbox.')
    you_others = UI('You and others changed %(filename)s in your business Dropbox.')
    other = UI('%(user)s changed %(filename)s in your business Dropbox.')
    others = UI('%(user)s and others changed %(filename)s in your business Dropbox.')
    plural_you = (lambda num = None: ungettext('You changed %(num)s file in your business Dropbox.', 'You changed %(num)s files in your business Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others changed %(num)s file in your business Dropbox.', 'You and others changed %(num)s files in your business Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s changed %(num)s file in your business Dropbox.', '%(user)s changed %(num)s files in your business Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others changed %(num)s file in your business Dropbox.', '%(user)s and others changed %(num)s files in your business Dropbox.', num))()


class SyncEngineMessageTeamAddedStrings(UIStrings):
    you = UI('You added %(filename)s to your %(team_name)s Dropbox.')
    you_others = UI('You and others added %(filename)s to your %(team_name)s Dropbox.')
    other = UI('%(user)s added %(filename)s to your %(team_name)s Dropbox.')
    others = UI('%(user)s and others added %(filename)s to your %(team_name)s Dropbox.')
    plural_you = (lambda num = None: ungettext('You added %(num)s file to your %(team_name)s Dropbox.', 'You added %(num)s files to your %(team_name)s Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others added %(num)s file to your %(team_name)s Dropbox.', 'You and others added %(num)s files to your %(team_name)s Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s added %(num)s file to your %(team_name)s Dropbox.', '%(user)s added %(num)s files to your %(team_name)s Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others added %(num)s file to your %(team_name)s Dropbox.', '%(user)s and others added %(num)s files to your %(team_name)s Dropbox.', num))()


class SyncEngineMessageTeamDeletedStrings(UIStrings):
    you = UI('You deleted %(filename)s from your %(team_name)s Dropbox.')
    you_others = UI('You and others deleted %(filename)s from your %(team_name)s Dropbox.')
    other = UI('%(user)s deleted %(filename)s from your %(team_name)s Dropbox.')
    others = UI('%(user)s and others deleted %(filename)s from your %(team_name)s Dropbox.')
    plural_you = (lambda num = None: ungettext('You deleted %(num)s file from your %(team_name)s Dropbox.', 'You deleted %(num)s files from your %(team_name)s Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others deleted %(num)s file from your %(team_name)s Dropbox.', 'You and others deleted %(num)s files from your %(team_name)s Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s deleted %(num)s file from your %(team_name)s Dropbox.', '%(user)s deleted %(num)s files from your %(team_name)s Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others deleted %(num)s file from your %(team_name)s Dropbox.', '%(user)s and others deleted %(num)s files from your %(team_name)s Dropbox.', num))()


class SyncEngineMessageTeamChangedStrings(UIStrings):
    you = UI('You changed %(filename)s in your %(team_name)s Dropbox.')
    you_others = UI('You and others changed %(filename)s in your %(team_name)s Dropbox.')
    other = UI('%(user)s changed %(filename)s in your %(team_name)s Dropbox.')
    others = UI('%(user)s and others changed %(filename)s in your %(team_name)s Dropbox.')
    plural_you = (lambda num = None: ungettext('You changed %(num)s file in your %(team_name)s Dropbox.', 'You changed %(num)s files in your %(team_name)s Dropbox.', num))()
    plural_you_others = (lambda num = None: ungettext('You and others changed %(num)s file in your %(team_name)s Dropbox.', 'You and others changed %(num)s files in your %(team_name)s Dropbox.', num))()
    plural_other = (lambda num = None: ungettext('%(user)s changed %(num)s file in your %(team_name)s Dropbox.', '%(user)s changed %(num)s files in your %(team_name)s Dropbox.', num))()
    plural_others = (lambda num = None: ungettext('%(user)s and others changed %(num)s file in your %(team_name)s Dropbox.', '%(user)s and others changed %(num)s files in your %(team_name)s Dropbox.', num))()

MYPY = False
if MYPY:
    SyncEngineMessageStringsType = Union[(Type[SyncEngineMessageAddedStrings], Type[SyncEngineMessageAddedShortStrings], Type[SyncEngineMessageDeletedStrings], Type[SyncEngineMessageDeletedShortStrings], Type[SyncEngineMessageChangedStrings], Type[SyncEngineMessageChangedShortStrings], Type[SyncEngineMessagePersonalAddedStrings], Type[SyncEngineMessagePersonalDeletedStrings], Type[SyncEngineMessagePersonalChangedStrings], Type[SyncEngineMessageTeamAddedStrings], Type[SyncEngineMessageTeamDeletedStrings], Type[SyncEngineMessageTeamChangedStrings], Type[SyncEngineMessageBusinessAddedStrings], Type[SyncEngineMessageBusinessDeletedStrings], Type[SyncEngineMessageBusinessChangedStrings])]
    return None
