# Source Generated with Decompyle++
# File: logging_helpers.pyc (Python 3.11)

import uuid
from typing import Any, Dict
from dropbox.client.configuration.interface import LocalConfigurationInterface
DOD_SESSION_ID_CONFIG_KEY = 'dod_session_id_config_key'

def non_pii_extras(extras = None):
    no_pii_extras = { }
    for k, v in extras.items():
        if k.startswith('nopii_'):
            new_key = k[len('nopii_'):]
            no_pii_extras[new_key] = v
        return no_pii_extras


def get_or_create_dod_session_id(local_config = None):
    session_id = local_config.config_dict.get(DOD_SESSION_ID_CONFIG_KEY, uuid.uuid4().hex)
    if DOD_SESSION_ID_CONFIG_KEY not in local_config.config_dict.keys():
        local_config.config_dict[DOD_SESSION_ID_CONFIG_KEY] = session_id
    return session_id

