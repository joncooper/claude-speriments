# Source Generated with Decompyle++
# File: url_info.pyc (Python 3.11)

import multiprocessing
import os
import webbrowser
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Union
from webbrowser import BackgroundBrowser, BaseBrowser, register
from six.moves import urllib
from six.moves.urllib.request import pathname2url
from build_number import is_frozen, is_prod
from build_number.features import feature_enabled
from build_number.language_data import SYSTEM_LANG_CODE
from dropbox.callbacks import Handler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import BROWSER_LAUNCHER
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import is_integration_tests
from dropbox.i18n import get_current_code, get_requested_code
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS, platform
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE, WARNING
if IS_LINUX:
    from dropbox.client.util.linux import using_old_ld_library_path
browser_launcher_open = webbrowser.open
browser_launcher_open_new: 'Callable[[str], bool]' = webbrowser.open_new
ProtocolHostPort = NamedTuple('ProtocolHostPort', [
    ('protocol', str),
    ('host', str),
    ('port', int)])
HostPort = NamedTuple('HostPort', [
    ('host', str),
    ('port', int)])

def to_protocol_host_port(url = None):
    (prot, port) = ('https', '443')
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
        (prot, port) = ('http', '80')
    if url.find(':') != -1:
        (url, port) = url.split(':')
        if (int(port) == 80 or is_prod()) and int(port) == 2000 and 'dev.corp.dropbox.com' in url:
            prot = 'http'
    return ProtocolHostPort(prot, str(url), int(port))


def to_host_port(url = None):
    (_, host, port) = to_protocol_host_port(url)
    return HostPort(host, port)


def _get_displayable_url_hostname(url = None):
    (protocol, host, port) = to_protocol_host_port(url)
    if port not in (None, 80, 443):
        return '%s://%s:%d' % (protocol, host, port)
    return f'''{None!s}://{host!s}'''

if IS_WINDOWS:
    import subprocess
    from ctypes import byref, create_unicode_buffer, HRESULT
    from ctypes.wintypes import DWORD, LPCWSTR, LPWSTR, UINT
    from comtypes import COMMETHOD, IUnknown, POINTER
    from comtypes.client import CreateObject
    from comtypes.GUID import GUID
    from pynt.constants import HKEY_CLASSES_ROOT, S_FALSE
    from pynt.dlls.shlwapi import shlwapi
    from pynt.helpers.registry import read_registry_value, registry_key
    from pynt.types import ASSOCIATIONLEVEL, ASSOCIATIONTYPE
    from winffi.shell32.api import shell_execute_ex
    from winffi.shlwapi.api import url_create_from_path
    from winshell.api import command_line_to_list
    from dropbox.win32.version import WIN81, WINDOWS_VERSION
    ASSOCIATION_LEVEL_NAMES = {
        ASSOCIATIONLEVEL.AL_USER: 'user',
        ASSOCIATIONLEVEL.AL_MACHINE: 'machine',
        ASSOCIATIONLEVEL.AL_EFFECTIVE: 'effective' }
    PROGID_UNDECIDED = 'Undecided'
    
    class IApplicationAssociationRegistration(IUnknown):
        CLSID_APPLICATIONASSOCIATIONREGISTRATION = '{591209c7-767b-42b2-9fba-44ee4615f2c7}'
        _iid_ = GUID('{4E530B0A-E611-4C77-A3AC-9031D022281B}')
        _idlflags_: 'List[Any]' = []
        _methods_ = [
            COMMETHOD([], HRESULT, 'QueryCurrentDefault', ([
                'in'], LPCWSTR, 'pszQuery'), ([
                'in'], UINT, 'atQueryType'), ([
                'in'], UINT, 'alQueryLevel'), ([
                'out'], POINTER(LPWSTR), 'ppszAssociation'))]

    
    def open_url(full_url = None):
        initialized_com = initialized_com
        import dropbox.win32.com_helper
        initialized_com('open_url')
        if WINDOWS_VERSION.version_number() >= WIN81.version_number():
            prog_id = check_application_association()
            if is_microsoft_edge(prog_id):
                TRACE('Browser appears to be Microsoft Edge')
                None(None, None)
                return 
        else:
            get_command_from_assoc_name('http') = get_command_from_assoc_name(prog_id)
        TRACE('Got browser command "%r"', command)
        None(None, None)
        return 
        with None:
            if not None, open_url_with_command(full_url, command):
                pass

    
    def _open(url = None, new = None, autoraise = None):
        return open_url(url)

    
    def is_microsoft_edge(prog_id = None):
        if 'AppX' not in prog_id:
            TRACE('AppX is not in the progID for the browser, so it cannot be Edge')
            return False
        edge_identifier = None
        prog_application = os.path.join(prog_id, 'Application')
        hkey = registry_key(HKEY_CLASSES_ROOT, prog_application)
        reg_val = read_registry_value(hkey, 'ApplicationName')
        TRACE('Found ApplicationName of %r in reg_key for prog_id %r, comparing to %s', reg_val, prog_id, edge_identifier)
        if edge_identifier in reg_val:
            None(None, None)
            return True
        None(None, None)

    
    def check_application_association():
        
        try:
            app_reg = CreateObject(IApplicationAssociationRegistration.CLSID_APPLICATIONASSOCIATIONREGISTRATION, interface = IApplicationAssociationRegistration)
            associations = [
                ('http', ASSOCIATIONTYPE.AT_URLPROTOCOL, ASSOCIATIONLEVEL.AL_EFFECTIVE),
                ('https', ASSOCIATIONTYPE.AT_URLPROTOCOL, ASSOCIATIONLEVEL.AL_EFFECTIVE),
                ('.html', ASSOCIATIONTYPE.AT_FILEEXTENSION, ASSOCIATIONLEVEL.AL_EFFECTIVE),
                ('.htm', ASSOCIATIONTYPE.AT_FILEEXTENSION, ASSOCIATIONLEVEL.AL_EFFECTIVE),
                ('http', ASSOCIATIONTYPE.AT_URLPROTOCOL, ASSOCIATIONLEVEL.AL_MACHINE),
                ('https', ASSOCIATIONTYPE.AT_URLPROTOCOL, ASSOCIATIONLEVEL.AL_MACHINE),
                ('.html', ASSOCIATIONTYPE.AT_FILEEXTENSION, ASSOCIATIONLEVEL.AL_MACHINE),
                ('.htm', ASSOCIATIONTYPE.AT_FILEEXTENSION, ASSOCIATIONLEVEL.AL_MACHINE)]
            for assoc_name, assoc_type, assoc_level in associations:
                prog_id = app_reg.QueryCurrentDefault(LPCWSTR(assoc_name), assoc_type, assoc_level)
                if prog_id != PROGID_UNDECIDED:
                    TRACE('Url_info: Found progID %r from association %r level %r', prog_id, assoc_name, ASSOCIATION_LEVEL_NAMES[assoc_level])
                
                if prog_id == PROGID_UNDECIDED:
                    TRACE('Url_info: Multiple programs registered as default for http/.html files')
            return prog_id
        except Exception:
            report_exception(component = DesktopComponent.AUTH)
            TRACE('Failed to get default http application with IApplicationAssociationRegistration')
            raise 


    
    def get_command_from_assoc_name(assoc_name = None):
        if '.exe' in assoc_name.lower():
            return assoc_name
        outsize = DWORD(0)
        
        try:
            shlwapi.AssocQueryStringW(0, 1, LPCWSTR(assoc_name), None, None, byref(outsize))
        except WindowsError:
            e = None
            if e.winerror != S_FALSE:
                raise 
            e = None
            del e
        except:
            e = None
            del e

        outval = create_unicode_buffer(outsize.value)
        shlwapi.AssocQueryStringW(0, 1, LPCWSTR(assoc_name), None, outval, byref(outsize))
        return outval.value

    
    def shellexecute_open_url(reg_class = None, full_url = None):
        
        try:
            TRACE('Opening %s with %s using ShellExecuteEx', full_url, reg_class)
            shell_execute_ex(reg_class, full_url)
            return True
        except Exception:
            report_exception(component = DesktopComponent.AUTH)
            TRACE('Launching browser did not work with ProgID %s', reg_class)
            return False


    
    def open_url_with_command(full_url = None, command = None):
        if not full_url:
            return False
        full_url = None.strip()
        place_holder = '%1'
        command_list = []
        raw_command_list = command_line_to_list(command)
        if not raw_command_list:
            return False
        None.append(raw_command_list[0])
        found_place_holder = False
        if len(raw_command_list) > 1:
            for segment in raw_command_list[1:]:
                if place_holder in segment:
                    segment = segment.replace(place_holder, full_url)
                    found_place_holder = True
                command_list.append(segment)
                if not found_place_holder:
                    command_list.append(full_url)
        TRACE('Executing %r', Text(command_list))
        subprocess.Popen(command_list)
        return True

    
    def execute_browser_launcher_command(command = None):
        TRACE('Executing %r', command)
        
        try:
            subprocess.Popen(command)
        except Exception:
            report_exception(component = DesktopComponent.AUTH)
            TRACE('Failed to launch url, command: %r', command)
            return False

        return True

    
    class PathBrowserLauncher(BaseBrowser):
        
        def __init__(self = None, path = None):
            self.path = path

        
        def open(self = None, full_url = None, new = None, autoraise = (0, True)):
            command = f'''{self.path!s} {full_url!s}'''
            return execute_browser_launcher_command(command)


    
    class EdgeBrowserLauncher(BaseBrowser):
        escape_uri = (lambda cls = None, uri = None: pass# WARNING: Decompyle incomplete
)()
        
        def open(self = None, full_url = None, new = None, autoraise = (0, True)):
            command = None
            
            try:
                safe_url = EdgeBrowserLauncher.escape_uri(full_url)
                command = 'microsoft-edge:%s' % safe_url
                os.startfile(command, 'open')
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.AUTH)
                TRACE('Failed to launch url using Edge, command: %r', command)
                return False

            return True


    allowed_path_launcher_browsers = [
        'chrome',
        'firefox',
        'mozilla',
        'msie']
    exe_name = { }
    exe_name['chrome'] = [
        'chrome.exe']
    exe_name['firefox'] = [
        'firefox.exe']
    exe_name['msie'] = [
        'IEXPLORE.EXE',
        'iexplore.exe']
    exe_name['mozilla'] = exe_name['firefox']
    
    def find_browser_path_from_registry(browser = None):
        path = None
        CloseKey = CloseKey
        EnumValue = EnumValue
        HKEY_LOCAL_MACHINE = HKEY_LOCAL_MACHINE
        OpenKey = OpenKey
        import six.moves.winreg
        for exe in exe_name[browser]:
            key = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\%s' % exe)
            path = EnumValue(key, 0)[1]
            CloseKey(key)
        except EnvironmentError:
            path = None
        if path and os.path.isfile(path):
            TRACE('Found path %s for browser %s from registry', path, browser)
            
            return None, path

    
    def find_browser_path_in_program_files(browser = None):
        rel_paths = { }
        rel_paths['chrome'] = [
            'Google\\Chrome\\Application\\chrome.exe']
        rel_paths['firefox'] = [
            'Mozilla Firefox\\firefox.exe']
        rel_paths['msie'] = [
            'Internet Explorer\\IEXPLORE.EXE',
            'Internet Explorer\\iexplore.exe']
        program_files_path = os.environ.get('PROGRAMFILES', 'C:\\Program Files')
        for rel_path in rel_paths[browser]:
            path = os.path.join(program_files_path, rel_path)
            if os.path.isfile(path):
                TRACE('Found path %s for browser %s from default location', path, browser)
                
                return None, path
            return None

    
    def _find_browser_path(browser = None):
        if browser not in allowed_path_launcher_browsers:
            return None
        path = find_browser_path_from_registry(browser)
        if not path:
            path = find_browser_path_in_program_files(browser)
        return path

    
    def _get_browser_launcher(browser = None):
        path = _find_browser_path(browser)
        if path:
            path_browser_launcher = PathBrowserLauncher(path)
            if not path_browser_launcher:
                report(BROWSER_LAUNCHER, browser = browser, event_name = 'path_failed')
            return path_browser_launcher
        if None == 'edge':
            edge_browser_launcher = EdgeBrowserLauncher()
            if not edge_browser_launcher:
                report(BROWSER_LAUNCHER, browser = browser, event_name = 'edge_failed')
            return edge_browser_launcher
        browser_launcher = webbrowser.get(browser)
        if not browser_launcher:
            report(BROWSER_LAUNCHER, browser = browser, event_name = 'webbrowser_failed')
        return browser_launcher

    register('chrome', None, BackgroundBrowser('chrome'))
    browser_launcher_open = _open
    browser_launcher_open_new = open_url
elif IS_MAC:
    from platform import machine
    from webbrowser import MacOSXOSAScript
    from AppKit import NSRunningApplication, NSWorkspace
    from Cocoa import NSAppleScript
    from CoreServices.LaunchServices import kLSRolesAll, LSGetApplicationForURL
    from Foundation import NSBundle, NSURL
    from macffi.CoreServices import browser_activate_and_launch_url
    from dropbox.mac.internal import autoreleasepool, MacError
    
    def _fast_mac_open(url = None, new = None, autoraise = None):
        autoreleasepool()
        fake_url = NSURL.URLWithString_('http:')
        browser_url = NSWorkspace.sharedWorkspace().URLForApplicationToOpenURL_(fake_url)
        if browser_url:
            bundle_id = NSBundle.bundleWithURL_(browser_url).bundleIdentifier()
            opened = _fast_mac_open_with_browser(bundle_id, url)
            if opened:
                None(None, None)
                return True
            TRACE('!! Failed to use app %r to open %r', bundle_id, url)
        else:
            TRACE('!! Failed to find application to open URL %r', fake_url)
        None(None, None)

    
    def _fast_mac_open_with_browser(bundle_identifier = None, url = None):
        autoreleasepool()
        if bundle_identifier.lower() != 'com.apple.safari':
            matching_apps = NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle_identifier)
            if len(matching_apps) == 0:
                NSWorkspace.sharedWorkspace().launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(bundle_identifier, 0, None, None)
                matching_apps = NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle_identifier)
            if len(matching_apps) > 0:
                None(None, None)
                return 
            (error_desc, _) = script.executeAndReturnError_(None)
            None(None, None)
            return 
        with None:
            if not None:
                pass

    
    class DefaultMacBrowser(MacOSXOSAScript):
        pass
    # WARNING: Decompyle incomplete

    
    class FastMacBrowserLauncher(BaseBrowser):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_browser_launcher(browser = None):
        bundle_identifier = None
        if browser in ('safari', 'webkit'):
            bundle_identifier = 'com.apple.Safari'
        elif browser == 'chrome':
            bundle_identifier = 'com.google.Chrome'
        elif browser == 'firefox':
            bundle_identifier = 'org.mozilla.firefox'
        elif browser == 'edge':
            bundle_identifier = 'com.microsoft.edgemac'
    # WARNING: Decompyle incomplete

    register('MacOSDefault', None, DefaultMacBrowser(), preferred = True)
    register('chrome', None, MacOSXOSAScript('Google Chrome'))
    register('opera', None, MacOSXOSAScript('opera'))
    register('firefox', None, MacOSXOSAScript('Firefox'))
    
    try:
        register('webkit', None, webbrowser.get('safari'))
    except webbrowser.Error:
        pass

    if machine() != 'arm64':
        browser_launcher_open = _fast_mac_open
    elif IS_LINUX and os.environ.get('DISPLAY'):
        
        def _get_browser_launcher(browser = None):
            res = webbrowser.get(browser)
            if not res:
                report(BROWSER_LAUNCHER, browser = browser, event_name = 'webbrowser_failed')
            return res

        
        try:
            register('chrome', None, webbrowser.get('google-chrome'))
        except webbrowser.Error:
            pass

        
        try:
            register('mozilla', None, webbrowser.get('firefox'))
        except webbrowser.Error:
            pass

        Str = Union[(str, Text)]
        
        def update_query_string(url = None, query_update = None):
            parsed_url = urllib.parse.urlparse(url)
            query_items = urllib.parse.parse_qs(parsed_url.query)
            query_items.update(query_update)
            updated_query = urllib.parse.urlencode(query_items, doseq = True)
            updated_parsed = parsed_url._replace(query = updated_query)
            return urllib.parse.urlunparse(updated_parsed)

        
        class DropboxURLInfo(object):
            __module__ = __name__
            __qualname__ = 'DropboxURLInfo'
            
            def __init__(self = None, overrides = None):
                pass
            # WARNING: Decompyle incomplete

            
            def __repr__(self = None):
                return easy_repr(self, 'webserver_host', 'paper_host', 'previews_dbx_host', 'previews_duc_host', 'sfe_host', 'nsf_host', 'api_hosts', 'discovery_port', 'p2p_port', '_pubserver')

            api_host = (lambda self = None: self.hosts['api_host'])()
            api_hosts = (lambda self = None: [
to_host_port(self.api_host)])()
            unity_flash_host = (lambda self = None: self.hosts['unity_flash_host'])()
            webserver_host = (lambda self = None: self.hosts['www_host'])()
            _block_host = (lambda self = None: self.hosts['block_host'])()
            _ping_http_host = (lambda self = None: self.hosts['ping_http_host'])()
            paper_host = (lambda self = None: self.hosts['paper_host'])()
            previews_dbx_host = (lambda self = None: self.hosts['previews_dbx_host'])()
            previews_duc_host = (lambda self = None: self.hosts['previews_duc_host'])()
            sfe_host = (lambda self = None: self.hosts['sfe_host'])()
            nsf_host = (lambda self = None: self.hosts['nsf_host'])()
            bolt_host = (lambda self = None: self.hosts['boltserver'])()
            replay_host = (lambda self = None: self.hosts['replay_host'])()
            _pubserver = (lambda self = None: self.hosts.get('pubserver'))()
        # WARNING: Decompyle incomplete

        
        def url_from_path(path = None):
            if IS_WINDOWS:
                return url_create_from_path(path)
            return None + pathname2url(path).lstrip('/')

        dropbox_url_info = DropboxURLInfo.init_from_build_info()
        return None
