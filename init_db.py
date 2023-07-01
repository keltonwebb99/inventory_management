import sqlite3
from sqlite3 import Error

#This defines a function that creates a connection to the SQLite database
def create_connection():
    conn = None;
    try:

        #creates a database connection to a SQLite database named inventory.db
        conn = sqlite3.connect('inventory.db') 
        return conn
    
    except Error as e:
        print(e)

    return conn

#Defines a function to create a table in the database
def create_table(conn):
    try:
        # Create a table named 'items' in the database with id, name, 
        # quantity, and last_updated fields
        sql = '''CREATE TABLE items(
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    quantity integer,
                    last_updated text
                );'''
        conn.execute(sql)
    except Error as e:
        print(e)

#main function that will create the connection and the table
def main():
    conn = create_connection()

    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
