import sqlite3
from flask import g

# This assumes a file named "tododatabase.db" is located in your working directory.
def connection_to_database():
    database_connection = sqlite3.connect("./tododatabase.db")
    database_connection.row_factory = sqlite3.Row
    return database_connection

def get_database():
    if "db" not in g:
        g.db = connection_to_database()    
    return g.db