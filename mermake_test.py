import pytest
from mermake import format_size, format_table_name, format_fk_relationship, format_table, generate_tables, format_column, is_table, has_constraints

COLUMN_WITHOUT_SIZE = {'name': 'c1', 'type': 'int'}
COLUMN_WITH_SCALAR_SIZE = {'name': 'c2', 'type': 'nvarchar', 'size': 2048}
COLUMN_WITH_PRECISION_SIZE = {'name': 'c3', 'type': 'numeric', 'size': [8, 3]}

TABLE1 = {'table_name': 'tbl1', 'schema': 'schema1'}
TABLE2 = {'table_name': 'tbl2', 'schema': 'schema1'}
TABLE3 = {'table_name': 'tbl3', 'schema': 'schema3', 'columns': [
    COLUMN_WITHOUT_SIZE,
    COLUMN_WITH_SCALAR_SIZE,
    COLUMN_WITH_PRECISION_SIZE
]}




def test_format_table_name():
    actual = format_table_name(TABLE1)
    assert actual == 'schema1_tbl1'


def test_format_table_name_without_schema():
    subject = {'table_name': TABLE1['table_name']}
    actual = format_table_name(subject)
    assert actual == 'tbl1'


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


def test_format_column_without_size():    
    assert format_column(COLUMN_WITHOUT_SIZE) == 'c1 int'

def test_format_column_with_scalar_size():    
    assert format_column(COLUMN_WITH_SCALAR_SIZE) == 'c2 nvarchar#40;2048#41;'

def test_format_column_with_precision_size():    
    assert format_column(COLUMN_WITH_PRECISION_SIZE) == 'c3 numeric#40;8,3#41;'




def test_is_table_true():
    assert True == is_table({'table_name': 'anything'})


def test_is_table_false():
    assert False == is_table({'key': 1})


def test_as_constraints_true():
    assert True == has_constraints({'table_name': 't1', 'constraints': []})


def test_format_size_when_string():
    assert format_size(42) == '42'
