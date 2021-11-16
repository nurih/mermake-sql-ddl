import json
import cli

from simple_ddl_parser import DDLParser


def parse(text):
    return DDLParser(text).run()


def generate_class_diagram(ddl):
    # Header
    print(generate_header())

    # Tables
    print()

    for table in generate_tables(ddl):
        print(table)

    # FK Relationships
    print()

    for fk_constraint in generate_relationships(ddl):
        print(fk_constraint)


def generate_header():
    return 'classDiagram'


def generate_tables(ddl):
    return [format_table(t) for t in ddl]


def generate_relationships(ddl):
    result = []
    for table in [tbl for tbl in ddl if tbl.get('constraints')]:
        from_table = format_table_name(table)
        for reference in table['constraints'].get('references', []):
            result.append(format_fk_relationship(from_table, reference))

    return result


def format_table_name(entity):
    return f"{entity['schema']}_{entity['table_name']}"


def format_table(table):
    result = f'\tclass {format_table_name(table)}'
    if 'columns' in table:
        result += '{\n'
        for column in table.get('columns'):
            result += '\t\t' + format_column(column) + '\n'
        result += '}'

    return result


def format_fk_relationship(source_table, reference):
    return f"{source_table} --|> {reference['schema']}_{reference['table']} : {', '.join(reference['columns'])}"


def format_column(column):
    size = column.get('size')
    sql_type = f"{column['type']}#40;{size}#41;" if size else column['type']
    return f"{column['name']} { sql_type}"


ddl = None


if __name__ == "__main__":
    args = cli.get_args()

    with open(args.ddl, 'r') as f:
        sql_text = f.read()
        ddl = parse(sql_text)

    generate_class_diagram(ddl)
