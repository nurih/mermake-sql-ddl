import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Usage: mermake.py -ddl ddl.sql')
    
    parser.add_argument("-d","--ddl", default='ddl.sql')
    
    return parser.parse_args()
