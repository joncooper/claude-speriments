# Source Generated with Decompyle++
# File: sqlite3_definitions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sqlite3
from enum import Enum, IntEnum, StrEnum, unique as unique_enum
from sqlite3 import Cursor
from typing import Any, Callable, cast, Dict, Generic, Iterable, List, Mapping, Optional, Text, Tuple, Type, TypeVar, Union
from dropbox.shared.server_path import RRCasedServerPath, RRLowerServerPath, ServerPath
from dropbox.shared.validated_record import Field, ValidatedRecord
from dropbox.sqlite3_helpers import from_db_type, to_db_type
SQLType = <NODE:12>()
AnyPythonSQLiteType = Union[(Dict[(Text, Any)], Text, int, float)]
T = TypeVar('T', bound = ValidatedRecord)
MYPY = False

def validate_row(record_type = None, row = None):
    pass
# WARNING: Decompyle incomplete


def validate_rows(record_type = None, rows = None):
    result = []
    for row in rows:
        validated = validate_row(record_type, row)
        if validated:
            result.append(validated)
        return result


def SQLiteValidatedTable():
    '''SQLiteValidatedTable'''
    
    def __init__(self = None, name = None, record_type = None):
        self._name = name
        self._record_type = record_type

    name = (lambda self = None: self._name)()
    count_sql = (lambda self = None: 'SELECT count(*) FROM %s' % self._name)()
    count_sql_not_null_clientvars = (lambda self = None: f'''SELECT count(*) FROM {self._name!s} WHERE {'clientvars'!s} IS NOT NULL''')()
    creation_sql = (lambda self = None: columns = self._record_type.schema_iter()()cols_sql = columns()pri_key_constraints = self._primary_key_constraint(columns)if pri_key_constraints:
cols_sql.append(pri_key_constraints)f'''CREATE TABLE {self._name!s} ({', '.join(cols_sql)!s})''')()
    generic_drop_sql = (lambda table_name = None: 'DROP TABLE %s' % table_name)()
    drop_sql = (lambda self = None: 'DROP TABLE %s' % self._name)()
    
    def _primary_key_constraint(self = None, columns = None):
        pri_key_fields = columns()
        return 'PRIMARY KEY (%s)' % ','.join(pri_key_fields) if pri_key_fields else ''

    
    def count(self = None, cursor = None):
        return cursor.execute(self.count_sql).fetchone()[0]

    
    def count_with_notnull_clientvars(self = None, cursor = None):
        return cursor.execute(self.count_sql_not_null_clientvars).fetchone()[0]

    
    def validate_row(self = None, row = None):
        r = validate_row(self._record_type, row)
        return r

    
    def validate_rows(self = None, rows = None):
        return validate_rows(self._record_type, rows)


SQLiteValidatedTable = <NODE:27>(SQLiteValidatedTable, 'SQLiteValidatedTable', Generic[T])

def insert_values_for_record_sqlite_columns(record = None):
    res = insert_values_for_records_sqlite_columns([
        record])
# WARNING: Decompyle incomplete


def insert_values_for_records_sqlite_columns(records = None):
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(records()):
        return None
    schema_record = next(iter(records))
# WARNING: Decompyle incomplete

R = TypeVar('R')
SpecificPythonSQLiteType = TypeVar('SpecificPythonSQLiteType', Dict, Text, int, float, covariant = True)

def SQLiteValidatedColumn():
    '''SQLiteValidatedColumn'''
    pass
# WARNING: Decompyle incomplete

SQLiteValidatedColumn = <NODE:27>(SQLiteValidatedColumn, 'SQLiteValidatedColumn', Field, Generic[(R, SpecificPythonSQLiteType)])

def marshal_validated_record(record = None):
    return record.to_json_dict()

S = TypeVar('S', bound = ServerPath)

def coerce_to_serverpath(path_class = None, server_path = None):
    if isinstance(server_path, Text):
        return path_class(server_path)


def make_coerce_to_serverpath(path_class = None):
    pass
# WARNING: Decompyle incomplete


def serverpath_to_sqlite(server_path = None):
    return Text(server_path)


def ServerPathColumn(name = None, path_class = None, nullable = None, unique = (False, False, False), primary = ('name', 'Text', 'path_class', 'Type[S]', 'nullable', 'Optional[bool]', 'unique', 'Optional[bool]', 'primary', 'Optional[bool]', 'return', 'SQLiteValidatedColumn[S, Text]')):
    return SQLiteValidatedColumn(name, field_type = path_class, data_type = SQLType.TEXT, marshal = serverpath_to_sqlite, coerce = make_coerce_to_serverpath(path_class), nullable = nullable, unique = unique, primary = primary)


def RRLowerServerPathColumn(name = None, nullable = None, unique = None, primary = (False, False, False)):
    return ServerPathColumn(name, RRLowerServerPath, nullable, unique, primary)


def RRCasedServerPathColumn(name = None, nullable = None, unique = None, primary = (False, False, False)):
    return ServerPathColumn(name, RRCasedServerPath, nullable, unique, primary)

