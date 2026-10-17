# Source Generated with Decompyle++
# File: content_util.pyc (Python 3.11)

import os
from typing import Dict, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.model.types import NsId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sharing.constants.content import Content, ContentType
from dropbox.sync_engine_boundary.types.local_props import LocalDirectoryProperties, LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import MountProperties, RemoteLocationProperties

def is_folder(local_props = None):
    return isinstance(local_props.file_type, LocalDirectoryProperties)


def is_mount_point(remote_props = None):
    if remote_props is not None:
        pass
    return isinstance(remote_props.file_type, MountProperties)


def is_in_team_shared_folder(remote_props = None):
    if remote_props is not None:
        pass
    return remote_props.is_in_team_folder


def get_mount_ns_id(remote_props = None):
    if not is_mount_point(remote_props):
        return None
# WARNING: Decompyle incomplete


def get_content_type(local_props = None, remote_props = None):
    if is_folder(local_props):
        if is_mount_point(remote_props):
            return ContentType.SHARED_FOLDER
        return None.UNSHARED_FOLDER
    return None.FILE


def get_api_id_from_server_path(server_path = None):
    (ns_id, rel_path) = server_path.ns_rel()
    if not rel_path.startswith('/'):
        rel_path = '/' + rel_path
    return f'''ns:{str(ns_id)}{str(rel_path)}'''


def get_api_id(content_type = None, local_props = None, remote_props = None):
    server_path = local_props.mr_server_path
    (ns_id, rel_path) = server_path.ns_rel()
    if not rel_path.startswith('/'):
        rel_path = '/' + rel_path
    if content_type in (ContentType.FILE, ContentType.UNSHARED_FOLDER):
        return f'''ns:{Text(ns_id)}{Text(rel_path)}'''
    if None == ContentType.SHARED_FOLDER:
        return Text(get_mount_ns_id(remote_props))
    raise AssertionError(f'''Unknown content type: {content_type}''')


def get_link_api_id(content_type = None, local_props = None, remote_props = None):
    server_path = local_props.mr_server_path
    if content_type in (ContentType.FILE, ContentType.UNSHARED_FOLDER):
        (ns_id, rel_path) = server_path.ns_rel()
        if not rel_path.startswith('/'):
            rel_path = '/' + rel_path
        return f'''ns:{Text(ns_id)}{Text(rel_path)}'''
    if None == ContentType.SHARED_FOLDER:
        return f'''ns:{Text(get_mount_ns_id(remote_props))}'''
    raise AssertionError(f'''Unknown content type: {content_type}''')


def get_content(props = None):
    pass
# WARNING: Decompyle incomplete


def make_content_ref(ns_id = None, ns_path = None):
    return {
        '.tag': 'ns_id_ns_path',
        'ns_id': f'''{ns_id:d}''',
        'ns_path': ns_path }


def is_nested_shared_folder(account = None, content = None):
    return content.mount_relative_server_path.ns not in (account.home_ns_id, account.root_ns_id)


def get_parent_folder_name(content = None):
    local_path = Text(content.local_path)
    parent_folder_name = os.path.basename(os.path.dirname(os.path.normpath(local_path.rstrip('/'))))
    return parent_folder_name

