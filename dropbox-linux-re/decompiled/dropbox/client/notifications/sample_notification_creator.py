# Source Generated with Decompyle++
# File: sample_notification_creator.pyc (Python 3.11)

import json
import time
from typing import Any, Dict, List, Optional, Text
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.constants import BLUENOTE_NOTIFICATION_ID, BNNotificationType, CURRENT_NOTIFICATIONS_VERSION, GENERIC_TEMPLATE, NEMO_CAMPAIGN_ID
from dropbox.client.notifications.types import UserNotificationSeenState, UserNotificationStatus
from dropbox.exception.reporting import report_bad_assumption
from dropbox.trace import TRACE

class SampleNotificationCreator:
    
    def __init__(self, gandalf = None, nid = None, popup_nid = None, uid = ('return', 'None')):
        self._gandalf = gandalf
        self._nid = nid
        self._popup_nid = popup_nid
        self._uid = uid

    
    def create_notification(self = None, notification_type = None, **kwargs):
        notification = None
        if notification_type == 'quote':
            notification = self.create_bluenote_quote()
        elif notification_type == 'task':
            notification = self.create_bluenote_task()
        elif notification_type == 'thumbnail':
            notification = self.create_bluenote_thumbnail()
        elif notification_type == 'open_folder':
            notification = self.create_bluenote_open_folder(server_path = kwargs.get('server_path', '2:/'), backup_url_path = kwargs.get('backup_url_path', 'home'), object_id = kwargs.get('object_id'), object_name = kwargs.get('object_name'), message = kwargs.get('message'))
        elif notification_type == 'open_file':
            notification = self.create_bluenote_open_file()
        elif notification_type == 'open_preferences':
            notification = self.create_bluenote_open_preferences()
        elif notification_type == 'open_tray':
            notification = self.create_bluenote_open_tray()
        elif notification_type == 'open_url':
            notification = self.create_bluenote_open_url()
        elif notification_type == 'open_standalone_server_view':
            notification = self.create_bluenote_open_standalone_server_view()
        elif notification_type == 'open_sharing_view':
            notification = self.create_bluenote_open_sharing_view(server_path = kwargs.get('server_path', ''), prefill_email = kwargs.get('prefill_email'), backup_url_path = kwargs.get('backup_url_path', ''))
        elif notification_type == 'persistent_loud':
            notification = self.create_bluenote_persistent_loud()
        elif notification_type == 'multiple_actions':
            notification = self.create_bluenote_multiple_actions()
        elif notification_type == 'xml_unfriendly':
            notification = self.create_bluenote_xml_unfriendly()
        elif notification_type == 'avatar':
            notification = self.create_bluenote_avatar()
        elif notification_type == 'sticky':
            notification = self.create_bluenote_sticky()
        else:
            report_bad_assumption('Unsupported notification type for insert_notification' + str(notification_type))
        return notification

    
    def create_bluenote_quote(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'test' } }
        preview = {
            'quote': "This is a test quote and I'm going to say a lot of things about this doc very cool." }
        notification = self._create_bluenote_notification(identifier = 100, surface_action = surface_action, message = 'Angela Gong commented on foo.bar', preview = preview)
        return notification

    
    def create_bluenote_task(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'test' } }
        preview = {
            'tasks': {
                'tasks': [
                    {
                        'id': '',
                        'name': 'Finish all the debug menu items',
                        'is_complete': True }],
                'task_endpoint': '' } }
        notification = self._create_bluenote_notification(identifier = 99, surface_action = surface_action, message = 'Donald Trump completed 1 task in First 100 Days of Presidency', preview = preview)
        return notification

    
    def create_bluenote_thumbnail(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'test' } }
        preview = {
            'show_thumbnail': True,
            'quote': 'Make sure you read through this doc quickly' }
        notification_object = {
            'name': 'test.pdf',
            'url': '',
            'ignore': False,
            'thumbnail_url': '',
            'type': 'dropbox-file',
            'id': '1234' }
        notification = self._create_bluenote_notification(identifier = 98, surface_action = surface_action, message = 'Click to open a folder', preview = preview, notification_object = notification_object)
        return notification

    
    def create_bluenote_open_folder(self, server_path = None, backup_url_path = None, object_id = None, object_name = ('2:/', 'home', None, None, None), message = ('server_path', 'str', 'backup_url_path', 'str', 'object_id', 'Optional[str]', 'object_name', 'Optional[str]', 'message', 'Optional[str]', 'return', 'Dict[str, Any]')):
        if (object_id is None) != (object_name is None):
            raise ValueError('object_id and object_name must be provided together')
        surface_action = {
            'action_name': 'open_folder',
            'params': {
                'server_path': server_path,
                'backup_url_path': backup_url_path } }
    # WARNING: Decompyle incomplete

    
    def create_bluenote_open_file(self = None):
        button_actions = [
            {
                'action_name': 'open_file',
                'label': 'Open File',
                'params': {
                    'server_path': '2:/test.pdf',
                    'backup_url_path': 'home?preview=test.pdf' } }]
        notification = self._create_bluenote_notification(identifier = 6, button_actions = button_actions, message = 'Click to open a file')
        return notification

    
    def create_bluenote_open_preferences(self = None):
        surface_action = {
            'action_name': 'open_preferences',
            'params': {
                'view_name': 'account' } }
        notification = self._create_bluenote_notification(identifier = 10, surface_action = surface_action, message = 'Click to open preferences')
        return notification

    
    def create_bluenote_open_tray(self = None):
        surface_action = {
            'action_name': 'open_tray' }
        notification = self._create_bluenote_notification(identifier = 2, surface_action = surface_action, message = 'Click to open the tray')
        return notification

    
    def create_bluenote_open_url(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'help' } }
        button_actions = [
            {
                'action_name': 'open_url',
                'label': 'Open URL',
                'highlight': True,
                'params': {
                    'url_path': '1' } },
            {
                'action_name': 'open_url',
                'label': 'Another one',
                'params': {
                    'url_path': '2' } }]
        notification = self._create_bluenote_notification(identifier = 1, surface_action = surface_action, button_actions = button_actions, message = 'Click to open a URL')
        return notification

    
    def create_bluenote_open_standalone_server_view(self = None):
        surface_action = {
            'action_name': 'open_standalone_server_view',
            'params': {
                'url_path': '/pro/buy_server_view',
                'backup_url_path': '/pro/buy',
                'stormcrow_rule_name': 'desktop-bluenote-tray-test',
                'width': '840',
                'height': '510' } }
        button_actions = [
            {
                'action_name': 'open_standalone_server_view',
                'label': 'Open Client Onboarding Server View',
                'highlight': True,
                'params': {
                    'url_path': '/growth/client_onboarding_server_view',
                    'backup_url_path': '/register',
                    'stormcrow_rule_name': 'desktop-bluenote-tray-test' } },
            {
                'action_name': 'open_standalone_server_view',
                'label': 'Open 404 Not found server view',
                'params': {
                    'url_path': '/not_found',
                    'backup_url_path': '/not_found',
                    'stormcrow_rule_name': 'desktop-bluenote-tray-test',
                    'height': '510' } }]
        notification = self._create_bluenote_notification(identifier = 96, surface_action = surface_action, button_actions = button_actions, message = 'Click to open a URL in Server View')
        return notification

    
    def create_bluenote_open_sharing_view(self = None, server_path = None, prefill_email = None, backup_url_path = ('server_path', 'str', 'prefill_email', 'Optional[str]', 'backup_url_path', 'str', 'return', 'Dict[str, Any]')):
        params = {
            'server_path': server_path,
            'backup_url_path': backup_url_path }
    # WARNING: Decompyle incomplete

    
    def create_bluenote_persistent_loud(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'help' } }
        button_actions = [
            {
                'action_name': 'open_url',
                'label': 'Open URL',
                'highlight': True,
                'params': {
                    'url_path': 'persistent_button' } }]
        notification = self._create_bluenote_notification(identifier = 4, surface_action = surface_action, button_actions = button_actions, message = 'I have a persistent loud notification!', loud_is_persistent = True)
        return notification

    
    def create_bluenote_multiple_actions(self = None):
        button_actions = [
            {
                'action_name': 'open_url',
                'label': 'First',
                'highlight': True,
                'params': {
                    'url_path': 'first' } },
            {
                'action_name': 'open_url',
                'label': 'Second',
                'params': {
                    'url_path': 'second' } }]
        notification = self._create_bluenote_notification(identifier = 5, button_actions = button_actions, message = 'Hover for multiple actions')
        return notification

    
    def create_bluenote_xml_unfriendly(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'help' } }
        button_actions = [
            {
                'action_name': 'open_url',
                'label': '<>"\'&–',
                'highlight': True,
                'params': {
                    'url_path': 'persistent_button' } }]
        notification = self._create_bluenote_notification(identifier = 11, surface_action = surface_action, button_actions = button_actions, message = '&\'"><', loud_is_persistent = True)
        return notification

    
    def create_bluenote_avatar(self = None):
        surface_action = {
            'action_name': 'open_url',
            'params': {
                'url_path': 'help' } }
        notification = self._create_bluenote_notification(identifier = 12, message = 'AVATAR!!!', image = {
            'type': 'avatar',
            'avatar_account_id': 'dbid:AADAoyyFZ1hqaGptYwtLpGh7c4uBWmfhj0U',
            'avatar_initials': 'ST' }, surface_action = surface_action, loud_is_persistent = True)
        return notification

    
    def create_bluenote_sticky(self = None):
