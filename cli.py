import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Usage: mermake.py -ddl ddl.sql')
    
    parser.add_argument("-d","--ddl", default='ddl.sql', help='Path to SQL file containing the DDL')
    
    parser.add_argument("--dump", action='store_true', help = 'Print out parsing result instead of generating a diagram')
    
    return parser.parse_args()
