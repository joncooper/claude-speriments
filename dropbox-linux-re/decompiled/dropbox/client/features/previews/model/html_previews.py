# Source Generated with Decompyle++
# File: html_previews.pyc (Python 3.11)

from typing import Text
from dropbox.client.features.previews.helpers import normalize_and_sign_url
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.transitional import make_delayed_network_call

def fetch_html_preview(url = None, user_context = None):
    pass
# WARNING: Decompyle incomplete


def _fetch_html_preview(url = None, user_context = None):
    normalized_url = normalize_and_sign_url(url, user_context.account)
    return user_context.connection.request_with_response(method = 'GET', url = normalized_url, is_json = False, conn_name = 'previews-duc-server', debug_name = 'fetch_html_preview')

