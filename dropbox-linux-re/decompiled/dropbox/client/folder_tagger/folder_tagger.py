# Source Generated with Decompyle++
# File: folder_tagger.pyc (Python 3.11)

from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from folder_tagger_linux import FolderTagger
elif IS_MAC:
    from folder_tagger_mac import FolderTagger
elif IS_WINDOWS:
    from folder_tagger_windows import FolderTagger
# WARNING: Decompyle incomplete
