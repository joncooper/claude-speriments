# Source Generated with Decompyle++
# File: setup_wizard_constants.pyc (Python 3.11)

from enum import Enum
DEVICE_LIMIT_EXCEEDED = 'DEVICE_LIMIT_EXCEEDED'
CONFIG_KEY_FRESH_LINK_IN_PROGRESS = 'fresh_link_in_progress'
CONFIG_KEY_FIRST_LINK_TS = 'first_link_ts'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR = 'mev_wizard_has_error'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR_SECONDARY = 'mev_wizard_has_error_secondary'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR_VERSION = 'mev_wizard_has_error_version'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR_COUNT = 'mev_wizard_has_error_count'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR_SECONDARY_VERSION = 'mev_wizard_has_error_secondary_version'
CONFIG_KEY_MEV_WIZARD_HAS_ERROR_SECONDARY_COUNT = 'mev_wizard_has_error_secondary_count'
CONFIG_KEY_HAS_LINKED_DESKTOP_PREVIOUSLY = 'has_linked_desktop_previously'
MAX_MEV_SPAWNS = 2
TK_EXPERIMENT_VALUE = 'e2e_device_onboarding'
MIN_FREE_SPACE = 524288000
MIN_FREE_FRACTION = 0.1
LARGE_DROPBOX_THRESHOLD = 0x280000000
DESKTOP_WELCOME_FLOW_TABLE_NAME = 'desktop_welcome_flow'
DESKTOP_WELCOME_FLOW_EXTRA_REASON = 'reason'
NCCT_PLUS_TRIALS = 'ncct_plus_trials'
PLATFORM_PLUS_TRIALS_30D = 'platform_plus_trials_30d'

class WelcomeFlowViewMevEdgeCase(Enum):
    INFINITE_EXPOSED = 0
    ERRORED_PREVIOUSLY = 1
    STORMCROW_DISABLED = 2
    KILLSWITCH_ENABLED = 3
    PAIRED_INELIGIBLE = 4
    VALID_DEALCODE = 5
    GATING_EXCEPTION = 7
    MAX_ERRORED_PREVIOUSLY = 8
    MEV_DISABLED = 9


class WelcomeFlowViewMevEligibilityEvent(Enum):
    ELIGIBLE = 0
    NOT_ELIGIBLE = 1


class ContentMitigationType(Enum):
    SCALE_MITIGATION = 0
    LOW_DISK_SPACE = 1
    LARGE_DROPBOX = 2

DESKTOP_MEV_SETUP_WIZARD_EXPERIMENT = 'desktop-mev-setup-wizard-experiment'
DESKTOP_MEV_DEVICE_LIMIT_PREAUTH = 'desktop-mev-device-limit-preauth'
DESKTOP_PARTNER_BRANDING_SUPPORT_STORMCROW = 'desktop-partner-branding-support'
DESKTOP_DORA_DEAL_CODE_STORMCROW = 'desktop-dora-deal-code'
DESKTOP_DORA_M5_5_STORMCROW = 'desktop-dora-m5-5'
DESKTOP_DORA_UPSELL_STORMCROW = 'desktop-dora-upsell'
DESKTOP_CONTEXT_ONBOARDING_STORMCROW = 'desktop-context-onboarding'
DESKTOP_DORA_UPSELL_STORMCROW = 'desktop-dora-upsell'
DESKTOP_CONTEXT_ONBOARDING_EDGE_CASES_STORMCROW = 'desktop-context-onboarding-edge-cases'
DESKTOP_MEV_DISABLED = 'desktop-mev-disabled'
DESKTOP_SHOW_DEVICE_LIMIT_EXCEEDED_LANDING_SCREEN = 'desktop-show-device-limit-exceeded-landing-screen'
