# Source Generated with Decompyle++
# File: navigation_rules.pyc (Python 3.11)

import binascii
import os
from typing import List, NamedTuple, Optional, Text
from dropbox.foundation.html_views.common.features import HtmlViewFeatures as LocalViewFeatures
from dropbox.url_info import dropbox_url_info
LOCAL_VIEW_NATIVE_IMG_PATH_PREFIX = '/native_img'
LOCAL_VIEW_PREVIEWS_PATH_PREFIX = '/previews_asset'
LOCAL_VIEW_STATIC_CONTENT_PATH_PREFIX = '/static'
LOCAL_VIEW_HTML_PREVIEWS_PATH_PREFIX = '/previews_html'
KNOWN_LOCAL_VIEWS_SCHEME_HANDLERS: 'List[Text]' = []
KNOWN_SCHEME_HANDLER_LOCAL = 'dbx-local'
if LocalViewFeatures.is_feature_only_enabled():
    KNOWN_LOCAL_VIEWS_SCHEME_HANDLERS += [
        KNOWN_SCHEME_HANDLER_LOCAL]

def generate_random_domain(length = None):
    return binascii.hexlify(os.urandom(length)).decode('ascii')

LOCAL_VIEW_CONTENT_DOMAIN = generate_random_domain()
NavigationRules = NamedTuple('NavigationRules', [
    ('allowed_protocols', List[Text]),
    ('allowed_hostnames', List[Text]),
    ('allowed_subframe_hostnames', List[Text]),
    ('allowed_paths', Optional[List[Text]]),
    ('allowed_debugging_protocols', Optional[List[Text]])])
LOCAL_VIEW_NAVIGATION_PREFS = NavigationRules(allowed_protocols = KNOWN_LOCAL_VIEWS_SCHEME_HANDLERS, allowed_hostnames = [
    LOCAL_VIEW_CONTENT_DOMAIN], allowed_subframe_hostnames = [], allowed_paths = [
    LOCAL_VIEW_STATIC_CONTENT_PATH_PREFIX,
    LOCAL_VIEW_HTML_PREVIEWS_PATH_PREFIX], allowed_debugging_protocols = None)
LOCAL_VIEW_NAVIGATION_PREFS_DEBUG = LOCAL_VIEW_NAVIGATION_PREFS._replace(allowed_debugging_protocols = [
    'http',
    'https',
    'ws'])

def get_server_view_navigation_prefs(debug = None):
    return NavigationRules(allowed_protocols = [
        'https'], allowed_hostnames = [
        dropbox_url_info.webserver_host,
        dropbox_url_info.api_host,
        dropbox_url_info.paper_host,
        'cf.dropboxpayments.com'], allowed_subframe_hostnames = [
        'www.google.com',
        'dropboxcaptcha.com'], allowed_paths = [], allowed_debugging_protocols = [
        'https'] if debug else None)

