# Mermake

## What?
It [makes] a [Mer]maid diagram given an SQL ddl file.

Given some SQL table definition, it generates a MermaidJS diagram, which you can then embed, export as SVG or PNG or whatever.

> Although an ERD seems like a natural choice for a diagram type, ERD describes _entities_, but DDL describes an implementation in tables. ERD was not designed to capture or represent many-to-many tables that may "connect" two "entities". For that reason, a class diagram was chosen, which can represent fields (columns in this context), and arbitrary lines of dependency (foreign keys in our context)


## Usage

```python
python mermake.py --ddl my_ddl_file.sql
```

## Options

|Option|Description|
|--|--- |
|`--ddl`, `-d`|DDL file path|
|`--dump`|Print out the parsed schema (not the MermaidJS diagram)|





