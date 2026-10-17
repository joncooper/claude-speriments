# Source Generated with Decompyle++
# File: mp4_parser.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import calendar
import struct
import zlib
from collections import defaultdict
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from dateutil import parser as date_parser
from dropbox.metadata.mp4_imports import MP4ParserDuplicateChildAtomError, MP4ParserInvalidAtomNameError, MP4ParserMalformedAtomError, MP4ParserUncompressionError, MP4ParserUnexpectedCompressionLibraryError, MP4ParserUnexpectedLengthAtomError, MP4ParserUnexpectedTrackComponentError, SEEKABLE_TRAK_ATOMS, UNSEEKABLE_TRAK_ATOMS
from dropbox.trace import TRACE
AtomParserInfo = Dict[(bytes, Callable[([
    bytes], Any)])]
AtomType = Dict[(bytes, Any)]

def validate_atom_names(parent_atom = None, list_atoms = None):
    for atom in list_atoms:
        if atom[b'name'] not in ATOM_PARSER_TREE[parent_atom]:
            raise MP4ParserInvalidAtomNameError(f'''Atom {atom[b'name'].decode('ascii', 'ignore')!s} not allowed as child of {parent_atom.decode('ascii', 'ignore')!s}''')
        return None


def prune_invalid_atoms(parent_atom = None, list_atoms = None):
    pass
# WARNING: Decompyle incomplete


def _parse_int(buffer = None, offset = None):
    ret_val = struct.unpack('>L', buffer[offset:offset + 4])[0]
    return (ret_val, offset + 4)


def _parse_long(buffer = None, offset = None):
    ret_val = struct.unpack('>Q', buffer[offset:offset + 8])[0]
    return (ret_val, offset + 8)


def _parse_bytes(buffer = None, offset = None, num_chars = None):
    ret_val = buffer[offset:offset + num_chars]
    return (ret_val, offset + num_chars)


def validate_atom_header(buffer = None, expected_atom_name = None):
    pass
# WARNING: Decompyle incomplete


def extract_atoms(buffer = None, buffer_size = None):
    pos = 0
    ret_list = []
# WARNING: Decompyle incomplete


def parse_skipped_atom(buffer = None):
    return 'skipped (size %s)' % len(buffer)


def parse_tkhd_atom(buffer = None):
    validate_atom_header(buffer, b'tkhd')
    offset = 12
    (creation_time, offset) = _parse_int(buffer, offset)
    (modification_time, offset) = _parse_int(buffer, offset)
    (track_id, offset) = _parse_int(buffer, offset)
    offset += 4
    (duration, offset) = _parse_int(buffer, offset)
    offset += 52
    (track_width, offset) = _parse_int(buffer, offset)
    (track_height, offset) = _parse_int(buffer, offset)
    if len(buffer) not in (offset, offset + 12):
        raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
    return {
        b'creation_time': creation_time,
        b'modification_time': modification_time,
        b'duration': duration,
        b'track_id': track_id,
        b'track_width': track_width,
        b'track_height': track_height }


def parse_mdhd_atom(buffer = None):
    validate_atom_header(buffer, b'mdhd')
    offset = 12
    (creation_time, offset) = _parse_int(buffer, offset)
    (modification_time, offset) = _parse_int(buffer, offset)
    (time_scale, offset) = _parse_int(buffer, offset)
    (duration, offset) = _parse_int(buffer, offset)
    offset += 4
    if len(buffer) not in (offset, offset + 12):
        raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
    return {
        b'creation_time': creation_time,
        b'modification_time': modification_time,
        b'duration': duration,
        b'time_scale': time_scale }


def parse_hdlr_atom(buffer = None):
    validate_atom_header(buffer, b'hdlr')
    offset = 12
    (component_type, offset) = _parse_bytes(buffer, offset, 4)
    (component_subtype, offset) = _parse_bytes(buffer, offset, 4)
    offset += 12
    component_name = buffer[offset:]
    return {
        b'component_type': component_type,
        b'component_subtype': component_subtype,
        b'component_name': component_name }


def parse_ctts_atom(buffer = None):
    validate_atom_header(buffer, b'ctts')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 8 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 8!s} bytes but only {len(buffer) - offset!s} are available''')
    composition_offset_table = []
    for _ in range(number_of_entries):
        (sample_count, offset) = _parse_int(buffer, offset)
        (composition_offset, offset) = _parse_int(buffer, offset)
        composition_offset_table.append({
            b'sample_count': sample_count,
            b'composition_offset': composition_offset })
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'composition_offset_table': composition_offset_table }


def parse_minf_atom(buffer = None):
    validate_atom_header(buffer, b'minf')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(b'minf', list_atoms)
    atom_info = { }
    for atom in list_atoms:
        ATOM_PARSER_TREE[b'minf'][atom[b'name']] = None
        sub_atom = parser(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']])
# WARNING: Decompyle incomplete


def parse_stts_atom(buffer = None):
    validate_atom_header(buffer, b'stts')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 8 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 8!s} bytes but only {len(buffer) - offset!s} are available''')
    time_to_samples_table = []
    for _ in range(number_of_entries):
        (sample_count, offset) = _parse_int(buffer, offset)
        (sample_duration, offset) = _parse_int(buffer, offset)
        time_to_samples_table.append({
            b'count': sample_count,
            b'duration': sample_duration })
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'time_to_samples_table': time_to_samples_table }


def parse_stss_atom(buffer = None):
    validate_atom_header(buffer, b'stss')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 4 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 4!s} bytes but only {len(buffer) - offset!s} are available''')
    sync_samples_table = []
    for _ in range(number_of_entries):
        (sync_sample, offset) = _parse_int(buffer, offset)
        sync_samples_table.append(sync_sample)
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'sync_samples_table': sync_samples_table }


def parse_stps_atom(buffer = None):
    validate_atom_header(buffer, b'stps')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 4 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 4!s} bytes but only {len(buffer) - offset!s} are available''')
    partial_sync_sample_table = []
    for _ in range(number_of_entries):
        (partial_sync_sample, offset) = _parse_int(buffer, offset)
        partial_sync_sample_table.append(partial_sync_sample)
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'partial_sync_sample_table': partial_sync_sample_table }


def parse_stsc_atom(buffer = None):
    validate_atom_header(buffer, b'stsc')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 12 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 12!s} bytes but only {len(buffer) - offset!s} are available''')
    sample_to_chunk_table = []
    for _ in range(number_of_entries):
        (first_chunk, offset) = _parse_int(buffer, offset)
        (samples_per_chunk, offset) = _parse_int(buffer, offset)
        (sample_description_id, offset) = _parse_int(buffer, offset)
        sample_to_chunk_table.append({
            b'first_chunk': first_chunk,
            b'samples_per_chunk': samples_per_chunk,
            b'sample_description_id': sample_description_id })
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'sample_to_chunk_table': sample_to_chunk_table }


def parse_stsz_atom(buffer = None):
    validate_atom_header(buffer, b'stsz')
    offset = 12
    (overall_sample_size, offset) = _parse_int(buffer, offset)
    (number_of_entries, offset) = _parse_int(buffer, offset)
    remaining_bytes = len(buffer) - offset
    if remaining_bytes and number_of_entries * 4 > remaining_bytes:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 4!s} bytes but only {len(buffer) - offset!s} are available''')
    sample_size_table = []
    if overall_sample_size == 0:
        for _ in range(number_of_entries):
            (sample_size, offset) = _parse_int(buffer, offset)
            sample_size_table.append(sample_size)
            if len(buffer) not in (offset, offset + 12):
                raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
            return {
                b'number_of_entries': number_of_entries,
                b'sample_size_table': sample_size_table }


def parse_stco_atom(buffer = None):
    validate_atom_header(buffer, b'stco')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 4 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 4!s} bytes but only {len(buffer) - offset!s} are available''')
    chunk_offset_table = []
    for _ in range(number_of_entries):
        (chunk_offset, offset) = _parse_int(buffer, offset)
        chunk_offset_table.append(chunk_offset)
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'chunk_offset_table': chunk_offset_table }


def parse_co64_atom(buffer = None):
    validate_atom_header(buffer, b'co64')
    offset = 12
    (number_of_entries, offset) = _parse_int(buffer, offset)
    if number_of_entries * 8 > len(buffer) - offset:
        raise MP4ParserMalformedAtomError(f'''Need to parse {number_of_entries * 8!s} bytes but only {len(buffer) - offset!s} are available''')
    chunk_offset_table = []
    for _ in range(number_of_entries):
        (chunk_offset, offset) = _parse_long(buffer, offset)
        chunk_offset_table.append(chunk_offset)
        if len(buffer) not in (offset, offset + 12):
            raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
        return {
            b'number_of_entries': number_of_entries,
            b'chunk_offset_table': chunk_offset_table }


def parse_stbl_atom(buffer = None):
    validate_atom_header(buffer, b'stbl')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(b'stbl', list_atoms)
    atom_info = { }
    free_atom_num = 1
    sgpd_atom_num = 1
    csgm_atom_num = 1
    for atom in list_atoms:
        ATOM_PARSER_TREE[b'stbl'][atom[b'name']] = None
        sub_atom = parser(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']])
# WARNING: Decompyle incomplete


def parse_mdia_atom(buffer = None):
    validate_atom_header(buffer, b'mdia')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(b'mdia', list_atoms)
    atom_info = { }
    for atom in list_atoms:
        ATOM_PARSER_TREE[b'mdia'][atom[b'name']] = None
        sub_atom = parser(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']])
# WARNING: Decompyle incomplete


def parse_trak_atom(buffer = None):
    validate_atom_header(buffer, b'trak')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(b'trak', list_atoms)
    atom_info = { }
    for atom in list_atoms:
        ATOM_PARSER_TREE[b'trak'][atom[b'name']] = None
        sub_atom = parser(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']])
# WARNING: Decompyle incomplete


def parse_cmov_atom(buffer = None):
    validate_atom_header(buffer, b'cmov')
    offset = 8
    (_, offset) = _parse_int(buffer, offset)
    (name, offset) = _parse_bytes(buffer, offset, 4)
    if name != b'dcom':
        raise MP4ParserInvalidAtomNameError('Unexpected atom %r as child of cmov' % name)
    (com_library, offset) = _parse_bytes(buffer, offset, 4)
    if com_library != b'zlib':
        raise MP4ParserUnexpectedCompressionLibraryError('Unexpected compression library %r' % com_library)
    (_, offset) = _parse_int(buffer, offset)
    (name, offset) = _parse_bytes(buffer, offset, 4)
    if name != b'cmvd':
        raise MP4ParserInvalidAtomNameError('Unexpected atom %r as child of cmov' % name)
    (_, offset) = _parse_int(buffer, offset)
    compressed_data = buffer[offset:]
    
    try:
        uncompressed_data = zlib.decompress(compressed_data)
    except zlib.error:
        raise MP4ParserUncompressionError('Invalid compressed moov atom')

    return parse_moov_atom(uncompressed_data)


def parse_moov_atom(buffer = None):
    validate_atom_header(buffer, b'moov')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(b'moov', list_atoms)
    atom_info = { }
    childs_that_can_have_multiples = (b'trak_hint', b'trak_soun', b'trak_vide', b'trak_meta', b'trak_stbl', b'trak_text', b'free', b'udta')
    duplicate_child_indexes = defaultdict(int)
# WARNING: Decompyle incomplete


def parse_mvhd_atom(buffer = None):
    validate_atom_header(buffer, b'mvhd')
    offset = 12
    (creation_time, offset) = _parse_int(buffer, offset)
    (modification_time, offset) = _parse_int(buffer, offset)
    (time_scale, offset) = _parse_int(buffer, offset)
    (duration, offset) = _parse_int(buffer, offset)
    offset += 80
    if len(buffer) not in (offset, offset + 12):
        raise MP4ParserUnexpectedLengthAtomError(f'''Parsed only {offset!s} bytes out of {len(buffer)!s}''')
    return {
        b'creation_time': creation_time,
        b'modification_time': modification_time,
        b'time_scale': time_scale,
        b'duration': duration }


def parse_meta_atom(buffer = None):
    atom_info = _parse_atom_recursively(buffer, b'meta')
    meta_keys_we_extract = {
        b'com.apple.quicktime.make': b'make',
        b'com.apple.quicktime.model': b'model',
        b'com.apple.quicktime.software': b'software_version',
        b'com.apple.quicktime.creationdate': b'creationdate',
        b'com.apple.quicktime.location.ISO6709': b'location',
        b'com.apple.photos.originating.signature': b'signature' }
    key_by_index = { }
    for idx, key in enumerate(atom_info.get(b'keys', []), 1):
        if key[b'namespace'] != b'mdta' or key[b'key'] not in meta_keys_we_extract:
            continue
        key_by_index[idx] = meta_keys_we_extract[key[b'key']]
        meta_info = { }
        if not key_by_index:
            return { }
        for item in None.get(b'ilst', []):
            index = item[b'index']
            if index in key_by_index:
                key = key_by_index[index]
                data = item[b'data']
                if key not in meta_info or data[b'locale'] == 0:
                    meta_info[key] = data[b'value']
            return meta_info


def parse_keys_atom(buffer = None):
    validate_atom_header(buffer, b'keys')
    offset = 12
    keys = []
    (num_keys, offset) = _parse_int(buffer, offset)
    for _ in range(num_keys):
        (key_size, offset) = _parse_int(buffer, offset)
        (namespace, offset) = _parse_bytes(buffer, offset, 4)
        (value, offset) = _parse_bytes(buffer, offset, key_size - 8)
        keys.append({
            b'namespace': namespace,
            b'key': value })
        return keys


def parse_ilst_atom(buffer = None):
    validate_atom_header(buffer, b'ilst')
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    values = []
    for atom in list_atoms:
        (index, _) = _parse_int(atom[b'name'], 0)
        value = _parse_atom_recursively(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']], b'ilst', validate_name = False)
        value[b'index'] = index
        values.append(value)
        return values


def parse_data_atom(buffer = None):
    validate_atom_header(buffer, b'data')
    (type_indicator, offset) = _parse_int(buffer, 8)
    (locale_indicator, offset) = _parse_int(buffer, offset)
    return {
        b'type': type_indicator,
        b'locale': locale_indicator,
        b'value': buffer[offset:] }


def _parse_atom_recursively(buffer = None, atom_name = None, validate_name = None):
    if validate_name:
        validate_atom_header(buffer, atom_name)
    list_atoms = extract_atoms(buffer[8:], len(buffer) - 8)
    validate_atom_names(atom_name, list_atoms)
    atom_info = { }
    duplicate_child_indexes = defaultdict(int)
    for atom in list_atoms:
        ATOM_PARSER_TREE[atom_name][atom[b'name']] = None
        sub_atom = parser(buffer[atom[b'pos']:atom[b'pos'] + atom[b'size']])
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
