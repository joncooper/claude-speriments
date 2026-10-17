# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, Text
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.reporting import report_app_framework_event_restricted
_K_PRIMARY_MAPPINGS = [
    ('video/webm', 'webm'),
    ('application/wasm', 'wasm'),
    ('application/x-chrome-extension', 'crx'),
    ('application/xhtml+xml', 'xhtml,xht,xhtm'),
    ('audio/flac', 'flac'),
    ('audio/mp3', 'mp3'),
    ('audio/ogg', 'ogg,oga,opus'),
    ('audio/wav', 'wav'),
    ('audio/webm', 'webm'),
    ('audio/x-m4a', 'm4a'),
    ('image/gif', 'gif'),
    ('image/jpeg', 'jpeg,jpg'),
    ('image/png', 'png'),
    ('image/apng', 'png'),
    ('image/webp', 'webp'),
    ('multipart/related', 'mht,mhtml'),
    ('text/css', 'css'),
    ('text/html', 'html,htm,shtml,shtm'),
    ('text/javascript', 'js,mjs'),
    ('text/xml', 'xml'),
    ('video/mp4', 'mp4,m4v'),
    ('video/ogg', 'ogv,ogm')]
_K_SECONDARY_MAPPINGS = [
    ('image/x-icon', 'ico'),
    ('application/epub+zip', 'epub'),
    ('application/font-woff', 'woff'),
    ('application/gzip', 'gz,tgz'),
    ('application/javascript', 'js'),
    ('application/json', 'json'),
    ('application/octet-stream', 'bin,exe,com'),
    ('application/pdf', 'pdf'),
    ('application/pkcs7-mime', 'p7m,p7c,p7z'),
    ('application/pkcs7-signature', 'p7s'),
    ('application/postscript', 'ps,eps,ai'),
    ('application/rdf+xml', 'rdf'),
    ('application/rss+xml', 'rss'),
    ('application/vnd.android.package-archive', 'apk'),
    ('application/vnd.mozilla.xul+xml', 'xul'),
    ('application/x-gzip', 'gz,tgz'),
    ('application/x-mpegurl', 'm3u8'),
    ('application/x-shockwave-flash', 'swf,swl'),
    ('application/x-tar', 'tar'),
    ('application/zip', 'zip'),
    ('audio/mpeg', 'mp3'),
    ('image/bmp', 'bmp'),
    ('image/jpeg', 'jfif,pjpeg,pjp'),
    ('image/svg+xml', 'svg,svgz'),
    ('image/tiff', 'tiff,tif'),
    ('image/vnd.microsoft.icon', 'ico'),
    ('image/x-png', 'png'),
    ('image/x-xbitmap', 'xbm'),
    ('message/rfc822', 'eml'),
    ('text/calendar', 'ics'),
    ('text/html', 'ehtml'),
    ('text/plain', 'txt,text'),
    ('text/x-sh', 'sh'),
    ('text/xml', 'xsl,xbl,xslt'),
    ('video/mpeg', 'mpeg,mpg')]
_K_PLATFORM_MAPPINGS = [
    ('application/x-font-ttf', 'ttf')]
_HTML_VIEW_MIME_MAP: 'Dict[Text, Text]' = { }
for mime_type, exts in reversed(_K_PRIMARY_MAPPINGS + _K_PLATFORM_MAPPINGS + _K_SECONDARY_MAPPINGS):
    for ext in exts.split(','):
        _HTML_VIEW_MIME_MAP[ext] = mime_type
        
        def get_mime_type_for_ext(file_ext = None):
            if file_ext in _HTML_VIEW_MIME_MAP:
                result = _HTML_VIEW_MIME_MAP[file_ext]
            else:
                report_bad_assumption("Unknown mime type for extension '%s'", file_ext)
                report_app_framework_event_restricted('Unknown mime type for extension', ext = file_ext)
                result = 'application/octet-stream'
            return result

        return None
