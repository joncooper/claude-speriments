# Source Generated with Decompyle++
# File: tray_menu_options.pyc (Python 3.11)

from dropbox.client.ui.common.strings import UI, UIStrings
TrayOptionID = int

class TrayOption:
    OPTION_OPEN_FOLDER = 0
    OPTION_OPEN_WEBSITE = 1
    OPTION_OPEN_PREFERENCES = 2
    OPTION_PAUSE = 3
    OPTION_RESUME = 4
    OPTION_OPEN_HELP = 5
    OPTION_RECENTLY_CHANGED_PERSONAL = 6
    OPTION_RECENTLY_CHANGED_BUSINESS = 7
    OPTION_OPEN_PERSONAL_FOLDER = 8
    OPTION_OPEN_BUSINESS_FOLDER = 9
    OPTION_OPEN_CAMERA_IMPORT_PROGRESS = 10
    OPTION_OPEN_UPGRADE = 11
    OPTION_RELAUNCH_LINK = 12
    OPTION_DND = 16
    OPTION_VIEW_SYNC_STATUS = 20
    OPTION_OPEN_WEBSITE_MENU = 21
    OPTION_OUT_OF_SPACE = 22
    OPTION_GET_MORE_SPACE = 23
    OPTION_LOCK_VAULT = 24
    OPTION_UNLOCK_VAULT = 25
    OPTION_ADMIN_CONSOLE = 26
    OPTION_OPEN_LOGS = 27
    OPTION_QUIT_DROPBOX = 28
    OPTION_PREFERENCES_SUBMENU = 29
    OPTION_REPORT_BUG_INTERNAL = 101
    OPTION_EVENT_LOGGER_INTERNAL = 103
    OPTION_OVERRIDE_STORMCROW = 104


class TrayOptionStrings(UIStrings):
    open_dropbox = UI('Open Dropbox Folder', windows = UI('Open Dropbox folder'))
    open_personal_dropbox = UI('Open Personal Folder', windows = UI('Open personal folder'))
    launch_website = UI('Launch Dropbox Website', windows = UI('Launch Dropbox website'))
    relaunch_link = UI('Sign in')
    recently_changed = UI('Recently Changed Files', windows = UI('Recently Changed Files'))
    out_of_space = UI('Out of Dropbox space')
    get_more_space = UI('Get More Space', windows = UI('Get more space'))
    preferences_dotdotdot = UI('Preferences...')
    admin_console = UI('Admin Console', windows = UI('Admin console'))
    help_center = UI('Help Center', windows = UI('Help center'))
    open_logs = UI('Export Debug Logs', windows = UI('Export debug logs'))
    pause_syncing = UI('Pause Syncing', windows = UI('Pause syncing'))
    resume_syncing = UI('Resume Syncing', windows = UI('Resume syncing'))
    view_sync_status = UI('View Sync Issues')
    view_photo_import_progress = UI('View Import Progress...', windows = UI('View import progress...'))
    do_not_disturb = UI('Snooze Notifications', windows = UI('Snooze notifications'))
    turn_on_notifications = UI('Turn on notifications')
    snoozing_until = UI('Snoozing notifications until %(time)s', windows = UI('Snoozing notifications until %(time)s'))
    lock_vault = UI('Lock Vault', windows = UI('Lock Vault'))
    unlock_vault = UI('Unlock Vault', windows = UI('Unlock Vault'))

