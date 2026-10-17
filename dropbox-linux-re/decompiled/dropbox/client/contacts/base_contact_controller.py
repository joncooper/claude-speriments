# Source Generated with Decompyle++
# File: base_contact_controller.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import re
from collections import defaultdict
from typing import Dict, Optional, Text, Tuple
from dropbox.client.background_worker import on_background_thread
from dropbox.client_api.exceptions import DropboxResponseClientError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
FB_PREFIX = '@fb:'
GROUP_PREFIX = 'g:'
SIMPLIFIED_EMAIL_REGEX = re.compile('[^@]+@[^@]+\\.[^@]+')

def is_valid_email(email):
    return bool(SIMPLIFIED_EMAIL_REGEX.match(email))


class BaseContactsController(object):
    REFRESH_INTERVAL = 10800
    
    def __init__(self = None, dropbox_app = None, get_dbids = None):
        self.dropbox_app = dropbox_app
        self._get_dbids = get_dbids
        self.last_server_retrieval = None
        self.is_done_loading = False
        self.contacts = []
        self.hidden_contacts = { }
        self.group_info = { }
        self.sources = []
        self.prev_string = None
        self.prev_exclude_list = []
        self.filtered_contacts = []
        self.display_name_count_dict = defaultdict(int)
        self._has_initiated_network_request_for_contact = False
        self.db_id_and_photo_url_by_contact_value_dict = { }

    has_dbids = (lambda self: self._get_dbids)()
    
    def get_imported_sources(self, results, has_fb_ids):
        for source in results.get('third_party_sources', []):
            if source == 'google':
                self.sources.append('Gmail')
                continue
            if source == 'yahoo':
                self.sources.append('Yahoo')
            if has_fb_ids:
                self.sources.append('Facebook')

    
    def preprocess_duplicates(self):
        self.display_name_count_dict = defaultdict(int)
        for contact in self.contacts:
            display_name = contact[0]
            return None

    
    def has_duplicates(self, display_name):
        return self.display_name_count_dict[display_name.lower()] >= 2

    
    def get_matches(self, string, exclude_list, exclude_fb = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_contact_by_dropbox_id(self, dropbox_id):
        pass
    # WARNING: Decompyle incomplete

    
    def get_exact_match(self, string, account):
