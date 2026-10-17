# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import pathlib
import re
from enum import auto, Enum
from typing import Optional
from dropbox.client.features.backup_common.constants import DEFAULT_IGNORED_GLOBS
from dropbox.platform import IS_WINDOWS
SPECIAL_GLOB_CHARS = '{}[]?*#'
escaped_special_glob_chars = re.escape(SPECIAL_GLOB_CHARS)
special_glob_char_regex = re.compile(f'''([{escaped_special_glob_chars}])''')

def path_to_glob(path = None):
    if IS_WINDOWS:
        win_path = pathlib.PureWindowsPath(path)
        posix_path = win_path.as_posix()
    else:
        posix_path = path
    return special_glob_char_regex.sub('[\\1]', posix_path).replace('\\', '\\\\')

special_glob_char_escaped_regex = re.compile(f'''(?:\\[([{escaped_special_glob_chars}])\\]|\\\\([{escaped_special_glob_chars}])|\\\\(\\\\))''')

def glob_to_path(glob = None):
    glob_without_escaped_chars = special_glob_char_escaped_regex.sub('', glob)
# WARNING: Decompyle incomplete

DEFAULT_IGNORED_GLOBS_V123 = ('.volumeicon.icns', '.fseventsd', '.spotlight-v100', '.temporaryitems', '.trashes', 'system volume information', '$recycle.bin')()
case_insensitive_character_class_regex = '\\[('(f'''{(lambda .0: [ f'''{c.lower()}{c.upper()}''' for c in .0 ])('abcdefghijklmnopqrstuvwxyz'())})\\]''')

def unescape_v123_glob(glob = (lambda .0: [ ''.join(map((lambda ch: f'''[{ch.lower()}{ch.upper()}]''' if ch.isalpha() else ch), glob)) for glob in .0 ]
)):
    return case_insensitive_character_class_regex.sub((lambda m: m.group(1)[0]), glob)


def convert_dbx_ignore_line_to_path(glob = None):
    if len(glob) == 0:
        return None
    if None in DEFAULT_IGNORED_GLOBS:
        return None
    return glob_to_path(glob)

invalid_exclamation_character_class_regex = re.compile('\\[!\\](?:$|[^\\[\\]]*(?:$|\\[))')

class _Status(Enum):
    WAITING_FOR_START = auto()
    READY_TO_START = auto()
    STARTING = auto()
    READY = auto()
    UPDATING = auto()
    
    def valid_transition(self = None, next_status = None):
        allowed_transitions = [
            (_Status.WAITING_FOR_START, _Status.READY_TO_START),
            (_Status.READY_TO_START, _Status.STARTING),
            (_Status.STARTING, _Status.READY),
            (_Status.READY, _Status.UPDATING),
            (_Status.UPDATING, _Status.READY)]
        return (self, next_status) in allowed_transitions


