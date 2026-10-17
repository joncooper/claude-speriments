# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

VARIANT_OFF = 'OFF'
VARIANT_ON = 'ON'
VARIANT_SHOW = 'SHOW'
VARIANT_TRUE = 'TRUE'
VARIANT_V1 = 'V1'
VARIANT_V2 = 'V2'
VARIANT_V3 = 'V3'
VARIANT_V4 = 'V4'
VARIANT_V5 = 'V5'
CONTROL = 'CONTROL'
VARIANT_EXCEPTION = 'EXCEPTION'
MOBILE_FEATURE_NOT_RECEIVED = 'FEATURE_NOT_RECEIVED'
STORMCROW_CACHE_TTL = 300
STORMCROW_CACHE_MAX_TTL = 2592000
TYPE_JOB_ID_MAP = {
    'user': {
        'dag_id': 'experimentation_platform_hive_based_population',
        'task_id': 'run_edgestore_export_canary2' } }
TYPE_ROLLUP_ID_MAP = {
    'user': 4753 }
MIN_TS = [
    -1,
    -1]
PERMISSION_MAX_LEN = 100
STORMCROW_EDITOR_PERMISSION = 'stormcrow.edit'
STORMCROW_SUPERUSER_PERMISSION = 'stormcrow.superuser'
GO_DATA_FIELDS = [
    'custom_text',
    'user_cdm_state',
    'user_email',
    'user_id',
    'user_age_seconds',
    'user_programmatic_projects_access',
    'user_is_pro',
    'user_is_team',
    'team_id',
    'server_is_dev',
    'identity_is_team',
    'matched_selectors',
    'user.user_or_paired_user.is_team',
    'user.age_in_seconds',
    'user.is_subscription_active',
    'user.is_team',
    'user.is_cdm_member',
    'user.is_dropbox_admin']
GO_POPULATION_TYPES = [
    'random',
    'custom_text',
    'user',
    'team',
    'account_identity']
STORMCROW_DESKTOP_KIEV_PREFIX_LEN = 14
STORMCROW_DESKTOP_KIEV_PREFIX = 'desktop-kiev--'
STORMCROW_FEATURE_REGEX = '^[a-z0-9]+(_[a-z0-9]+)*$'
STORMCROW_FEATURE_DESKTOP_MOBILE_REGEX = '(^desktop_)|(^mobile_)'
STORMCROW_FEATURE_DESKTOP_MOBILE_VARIANT_CHAR_REGEX = '[a-zA-Z0-9,\\.:_\\-]'
STORMCROW_VARIANT_REGEX = '^[A-Z0-9]+(_[A-Z0-9]+)*$'
