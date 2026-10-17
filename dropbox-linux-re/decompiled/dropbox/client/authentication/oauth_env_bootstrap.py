# Source Generated with Decompyle++
# File: oauth_env_bootstrap.pyc (Python 3.11)

import json
import os
from typing import NamedTuple, Optional, TYPE_CHECKING
from build_number import BUILDID
from build_number.features import feature_enabled
import dropbox.api.v2.datatypes.client_auth as dropbox
from dropbox.build_common import get_build_number
from dropbox.client.device_info import get_device_info, UNSAFE_get_raw_machine_uuid
from dropbox.client.high_trace import add_redacted_trace_value
from dropbox.client.util import get_platform_info
from dropbox.client_api.apiv2.generated.client_auth import ClientAuth
from dropbox.client_api.connection.interface import OAuthTokenAuth
from dropbox.hostname import get_local_host_display_name
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication
OAUTH_ENV_BOOTSTRAP_FEATURE = 'oauth-env-bootstrap'
OAUTH_ENV_ACCESS_TOKEN = 'DROPBOX_ACCESS_TOKEN'

class OAuthEnvBootstrapResult(NamedTuple):
    host_int: 'Optional[int]' = 'OAuthEnvBootstrapResult'


class OAuthEnvBootstrapError(Exception):
    pass
# WARNING: Decompyle incomplete


def pop_oauth_env_access_token():
    if not oauth_env_bootstrap_enabled():
        return None
    token = None.environ.pop(OAUTH_ENV_ACCESS_TOKEN, None)
    if token:
        add_redacted_trace_value(token, '[oauth env access token]')
    return token


def oauth_env_bootstrap_enabled():
    return feature_enabled(OAUTH_ENV_BOOTSTRAP_FEATURE)


def bootstrap_host_from_oauth_env(dropbox_app = None, access_token = None):
    if not oauth_env_bootstrap_enabled():
        raise OAuthEnvBootstrapError('unsupported_build')
# WARNING: Decompyle incomplete

