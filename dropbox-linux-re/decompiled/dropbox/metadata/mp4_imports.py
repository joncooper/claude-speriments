# Source Generated with Decompyle++
# File: mp4_imports.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function

class MP4ParserGenericError(Exception):
    pass


class MP4ParserBadAtomSizeError(MP4ParserGenericError):
    pass


class MP4ParserBadMoovAtomSizeError(MP4ParserGenericError):
    pass


class MP4ParserNeedDataError(MP4ParserGenericError):
    pass


class MP4ParserUnexpectedFirstAtomError(MP4ParserGenericError):
    pass


class MP4ParserMoovFoundBeginningTail(MP4ParserGenericError):
    pass


class MP4ParserMissingMdatError(MP4ParserGenericError):
    pass


class MP4ParserUnknownResolutionError(MP4ParserGenericError):
    pass


class MP4ParserPermanentError(Exception):
    pass


class MP4ParserCannotPipeInterleavingTooSparseError(Exception):
    pass


class MP4ParserDuplicateChildAtomError(Exception):
    pass


class MP4ParserMalformedAtomError(Exception):
    pass


class MP4ParserIdenticalByteOffsetsError(Exception):
    pass


class MP4ParserInvalidAtomNameError(Exception):
    pass


class MP4ParserInvalidOffsetRequestError(Exception):
    pass


class MP4ParserUncompressionError(Exception):
    pass


class MP4ParserUnexpectedCompressionLibraryError(Exception):
    pass


class MP4ParserUnexpectedLengthAtomError(Exception):
    pass


class MP4ParserUnexpectedTrackComponentError(Exception):
    pass


class MP4ParserMissingVideoTrackError(MP4ParserPermanentError):
    pass


class MP4ParserInvalidTimeScaleError(MP4ParserPermanentError):
    pass

SEEKABLE_TRAK_ATOMS = [
    b'soun',
    b'vide',
    b'meta']
UNSEEKABLE_TRAK_ATOMS = [
    b'tmcd',
    b'odsm',
    b'sdsm',
    b'hint',
    b'text',
    b'sbtl',
    b'qtvr',
    b'clcp',
    b'pano',
    b'priv',
    b'tc64',
    b'subp',
    b'MPEG',
    b'vivo',
    b'EVET',
    b'strx',
    b'obje',
    b'm1v ',
    b'souf',
    b'data',
    b'MMS ',
    b'DHAV',
    b'gnrc',
    b'sprt',
    b'strm']
