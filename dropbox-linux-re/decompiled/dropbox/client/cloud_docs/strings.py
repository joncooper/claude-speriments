# Source Generated with Decompyle++
# File: strings.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, Sequence, Text
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.i18n import trans, ungettext

class CloudDocsUIStrings(UIStrings):
    create_shortcut_caption = UI('Creating shortcut…')
    create_shortcut_message = UI('If many items are syncing, it may take a bit longer to create “%(file_name)s”.')
    copy_url_success_caption = UI('Copied link to “%(url)s”')
    copy_url_success_message = UI('Your link is ready to share.')
    copy_url_error_caption = UI('Couldn’t copy link')
    copy_url_error_message = UI('Something went wrong.')


class CloudDocsErrorStrings(UIStrings):
    confirm_button = UI('OK')
    unknown_reason_caption = UI('Something went wrong.')
    generic_title = (lambda file_names = None: if len(file_names) == 1:
trans('Can’t open “%(file_name)s”') % dict(file_name = file_names[0])num_other_files = len(file_names) - 1ungettext('Can’t open “%(file_name)s” and %(num_other_files)s other file', 'Can’t open “%(file_name)s” and %(num_other_files)s other files', num_other_files) % dict(file_name = file_names[0], num_other_files = num_other_files))()
    no_fileid_title = (lambda file_names = None: if len(file_names) == 1:
trans('Can’t open “%(file_name)s” just yet') % dict(file_name = file_names[0])num_other_files = len(file_names) - 1ungettext('Can’t open “%(file_name)s” and %(num_other_files)s other file just yet', 'Can’t open “%(file_name)s” and %(num_other_files)s other files just yet', num_other_files) % dict(file_name = file_names[0], num_other_files = num_other_files))()
    no_fileid_caption = (lambda file_names = None: ungettext('This file isn’t ready to open just yet. Try again in a few seconds.', 'These files aren’t ready to open just yet. Try opening them again in a few seconds.', len(file_names)))()
    no_permissions_caption = (lambda file_names = None: ungettext('Something’s not quite right with the permissions for this file.', 'Something’s not quite right with the permissions for these files.', len(file_names)))()
    bad_format_caption = (lambda file_names = None: ungettext('Something’s not quite right with the format of this file.', 'Something’s not quite right with the format of these files.', len(file_names)))()
    no_longer_exists_title = (lambda file_names = None: if len(file_names) == 1:
trans('“%(file_name)s” no longer exists') % dict(file_name = file_names[0])num_other_files = len(file_names) - 1ungettext('“%(file_name)s” and %(num_other_files)s other file no longer exist', '“%(file_name)s” and %(num_other_files)s other files no longer exist', num_other_files) % dict(file_name = file_names[0], num_other_files = num_other_files))()
    no_longer_exists_caption = (lambda file_names = None: ungettext('Try checking if someone renamed or deleted this file.', 'Try checking if someone renamed or deleted these files.', len(file_names)))()
    timeout_title = (lambda file_names = None: if len(file_names) == 1:
trans('It’s taking a long time to open “%(file_name)s”') % dict(file_name = file_names[0])num_other_files = len(file_names) - 1ungettext('It’s taking a long time to open “%(file_name)s” and %(num_other_files)s other file', 'It’s taking a long time to open “%(file_name)s” and %(num_other_files)s other files', num_other_files) % dict(file_name = file_names[0], num_other_files = num_other_files))()
    timeout_caption = (lambda file_names = None: ungettext('Try opening it again.', 'Try opening them again.', len(file_names)))()
    invalid_extension_caption = (lambda file_names = None: ungettext('If you want to add this file to Dropbox, try dragging it into the Dropbox folder on your computer.', 'If you want to add these files to Dropbox, try dragging them into the Dropbox folder on your computer.', len(file_names)))()


class CloudDocsFSWarningStrings(UIStrings):
    move_inside_dropbox_caption = (lambda file_names = None: num_files = len(file_names)if num_files == 1:
trans('Web-based file “%(file_name)s” might not work in Dropbox') % dict(file_name = file_names[0])ungettext('“%(file_name)s” and %(num_files)s other web-based file might not work in Dropbox', '“%(file_name)s” and %(num_files)s other web-based files might not work in Dropbox', num_files - 1) % dict(file_name = file_names[0], num_files = num_files - 1))()
    move_inside_dropbox_message = (lambda file_names = None: ungettext('Because this web-based file was created outside Dropbox, it might not work in Dropbox.', 'Because these web-based files were created outside Dropbox, they might not work in Dropbox.', len(file_names)))()
    move_folder_inside_dropbox_caption = (lambda folder_names = None, file_names = None: CloudDocsFSWarningStrings.move_inside_dropbox_caption(file_names))()
    move_folder_inside_dropbox_message = (lambda folder_names = None, file_names = None: CloudDocsFSWarningStrings.move_inside_dropbox_message(file_names))()
    move_outside_dropbox_caption = (lambda file_names = None: num_files = len(file_names)if num_files == 1:
trans('Can’t move web-based file “%(file_name)s” out of Dropbox') % dict(file_name = file_names[0])ungettext('Can’t move “%(file_name)s” and %(num_files)s other web-based file out of Dropbox', 'Can’t move “%(file_name)s” and %(num_files)s other web-based files out of Dropbox', num_files - 1) % dict(file_name = file_names[0], num_files = num_files - 1))()
    move_outside_dropbox_message = (lambda file_names = None: trans('Web-based files will only work in Dropbox.'))()
    move_folder_outside_dropbox_caption = (lambda folder_names = None, file_names = None: num_folders = len(folder_names)if num_folders == 1:
trans('Can’t move “%(folder_name)s” out of Dropbox because it has a web-based file inside') % dict(folder_name = folder_names[0])ungettext('Can’t move “%(folder_name)s” and %(num_folders)s other folder out of Dropbox because they have web-based files inside', 'Can’t move “%(folder_name)s” and %(num_folders)s other folders out of Dropbox because they have web-based files inside', num_folders - 1) % dict(folder_name = folder_names[0], num_folders = num_folders - 1))()
    move_folder_outside_dropbox_message = (lambda folder_names = None, file_names = None: num_files = len(file_names)if num_files == 1:
trans('<b>%(file_name)s</b> is a web-based file and will only work in Dropbox.') % dict(file_name = file_names[0])ungettext('<b>%(file_name)s</b> and %(num_files)s other web-based file will only work in Dropbox.', '<b>%(file_name)s</b> and %(num_files)s other web-based files will only work in Dropbox.', num_files - 1) % dict(file_name = file_names[0], num_files = num_files - 1))()
    move_file_to_trash_caption = (lambda file_names = None: num_files = len(file_names)if num_files == 1:
trans('Delete web-based file “%(file_name)s” from your Dropbox account?') % dict(file_name = file_names[0])ungettext('Delete “%(file_name)s” and %(num_files)s other web-based file from your Dropbox account?', 'Delete “%(file_name)s” and %(num_files)s other web-based files from your Dropbox account?', num_files - 1) % dict(file_name = file_names[0], num_files = num_files - 1))()
    _move_file_to_trash_message = UI('Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.', windows = UI('Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'))
    move_file_to_trash_message = (lambda file_names = None: CloudDocsFSWarningStrings._move_file_to_trash_message)()
    move_folder_to_trash_caption = (lambda folder_names = None, file_names = None: num_folders = len(folder_names)if num_folders == 1:
trans('Delete “%(folder_name)s” from your Dropbox account?') % dict(folder_name = folder_names[0])ungettext('Delete “%(folder_name)s” and %(num_folders)s other folder from your Dropbox account?', 'Delete “%(folder_name)s” and %(num_folders)s other folders from your Dropbox account?', num_folders - 1) % dict(folder_name = folder_names[0], num_folders = num_folders - 1))()
    move_folder_to_trash_message = (lambda folder_names = None, file_names = None: num_files = len(file_names)if num_files == 1:
trans('This folder has web-based file “%(file_name)s” inside.<br><br>%(msg)s') % dict(file_name = file_names[0], msg = CloudDocsFSWarningStrings._move_file_to_trash_message)args = dict(file_name = file_names[0], num_files = num_files - 1, msg = CloudDocsFSWarningStrings._move_file_to_trash_message)num_folders = len(folder_names)if num_folders == 1:
ungettext('This folder has “%(file_name)s” and %(num_files)s other web-based file inside.<br><br>%(msg)s', 'This folder has “%(file_name)s” and %(num_files)s other web-based files inside.<br><br>%(msg)s', num_files - 1) % argsungettext('These folders have “%(file_name)s” and %(num_files)s other web-based file inside.<br><br>%(msg)s', 'These folders have “%(file_name)s” and %(num_files)s other web-based files inside.<br><br>%(msg)s', num_files - 1) % args)()
    move_inside_dropbox_learn_more = UI('Learn more')
    move_outside_dropbox_ok = UI('OK')
    move_to_trash_delete = UI('Delete')
    move_to_trash_cancel = UI('Cancel')

