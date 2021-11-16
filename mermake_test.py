import pytest
from mermake import format_table_name, format_fk_relationship, format_table, generate_tables, format_column

TABLE1 = {'table_name': 'tbl1', 'schema': 'schema1'}
TABLE2 = {'table_name': 'tbl2', 'schema': 'schema1'}
TABLE3 = {'table_name': 'tbl3', 'schema': 'schema3', 'columns': [
    {'name': 'c1', 'type': 'int32'},
    {'name': 'c2', 'type': 'char', 'size': 128}
]}


def test_format_table_name():
    actual = format_table_name(TABLE1)
    assert actual == 'schema1_tbl1'


def test_format_fk_relationship():
    actual = format_fk_relationship(
        'here', {'schema': 'there', 'table': 'that', 'columns': ['col11', 'col2']})
    assert actual == 'here --|> there_that : col11, col2'


def test_format_table():
    actual = format_table(TABLE1)
    assert actual == '\tclass schema1_tbl1'


def test_generate_tables():
    actual = generate_tables([TABLE1, TABLE2])
    assert len(actual) == 2

def test_format_column():
    actual = format_column(TABLE3.get('columns')[0])
    assert actual == 'c1 int32'

def test_format_column_with_size():
    actual = format_column(TABLE3.get('columns')[1])
    assert actual == 'c2 char#40;128#41;'
