import cli
import json
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
    return [format_table(t) for t in ddl if is_table(t)]


def generate_relationships(ddl):
    result = []
    for table in [tbl for tbl in ddl if has_constraints(tbl)]:
        from_table = format_table_name(table)
        for reference in table['constraints'].get('references', []):
            result.append(format_fk_relationship(from_table, reference))

    return result


def format_table_name(entity):
    schema = entity.get('schema')
    return entity['table_name'] if schema is None else f"{schema}_{entity['table_name']}"


def format_table(table):
    result = f'\tclass {format_table_name(table)}'
    if 'columns' in table:
        result += '{\n'
        for column in table.get('columns'):
            result += '\t\t' + format_column(column) + '\n'
        result += '}'

    return result

def format_size(size):
    if isinstance(size,int):
        return str(size)
    else:
        return ','.join([str(i) for i in size])

def is_table(node):
    return node and node.get('table_name') is not None


def has_constraints(node):
    if not is_table(node):
        return False
    return node.get('constraints') is not None


def format_fk_relationship(source_table, reference):
    return f"{source_table} --|> {reference['schema']}_{reference['table']} : {', '.join(reference['columns'])}"


def format_column(column):
    size = column.get('size')
    
    sql_type = f"{column['type']}"
        
    size_spec = '' if size is None else f"#40;{format_size(size)}#41;"

    return f"{column['name']} {sql_type}{size_spec}"


if __name__ == "__main__":
    args = cli.get_args()
    ddl = None

    with open(args.ddl, 'r') as f:
        sql_text = f.read()
        ddl = parse(sql_text)

    if args.dump:
        print(json.dumps(ddl, indent=4, sort_keys=True))
    else:
        generate_class_diagram(ddl)
