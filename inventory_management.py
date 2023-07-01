import sqlite3
from sqlite3 import Error

#Function that will create a connection to the SQLite database that we made
def create_connection():
    conn = None;
    try:
        #Connect to the SQLite database we made
        conn = sqlite3.connect('inventory.db') # Creates an SQLite database file named 'inventory.db'
        return conn
    except Error as e:
        print(e)

    return conn

#Function to insert a new item into the database
def insert_item(conn):
    name = input("Enter the name of the item: ")
    quantity = input("Enter the quantity of the item: ")

    try:
        #SQL query to insert new item into the database
        sql = '''INSERT INTO items(name, quantity, last_updated) VALUES(?,?, datetime('now'))'''
        conn.execute(sql, (name, quantity))
        conn.commit()
        print(f"Item {name} inserted successfully.")
    except Error as e:
        print(e)

#Function to update the quantity of an existing item in the database
def update_item(conn):
    id = input("Enter the id of the item you want to update: ")
    quantity = input("Enter the new quantity of the item: ")

    try:
        #SQL query to update quantity of item in the databae
        sql = '''UPDATE items SET quantity = ?, last_updated = datetime('now') WHERE id = ?'''
        conn.execute(sql, (quantity, id))
        conn.commit()
        print(f"Item {id} updated successfully.")
    except Error as e:
        print(e)

#Function to delete an existing item from the database
def delete_item(conn):
    id = input("Enter the id of the item you want to delete: ")

    try:
        #SQL query to delete item from the database
        sql = '''DELETE FROM items WHERE id = ?'''
        conn.execute(sql, (id,))
        conn.commit()
        print(f"Item {id} deleted successfully.")
    except Error as e:
        print(e)

#Function to fetch and print details of a specific item from the database
def query_item(conn):
    id = input("Enter the id of the item you want to view: ")

    try:
        #SQL query to fetch details of all items in the database
        sql = '''SELECT * FROM items WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

#Function to fetch and print details of all items in the database
def query_all_items(conn):
    try:
        #SQL query to fetch details of all items in the database
        sql = '''SELECT * FROM items'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

#Function to display the main menu of the application
def show_menu():
    print("1. Insert an item")
    print("2. Update an item")
    print("3. Delete an item")
    print("4. Query an item")
    print("5. Query all items")
    print("6. Quit")

#Main function to handle the menu and user input
def main():
    conn = create_connection()

    if conn is None:
        print("Error! cannot create the database connection.")
        return

    while True:
        show_menu()

        choice = input("Select an option: ")

        if choice == "1":
            insert_item(conn)
        elif choice == "2":
            update_item(conn)
        elif choice == "3":
            delete_item(conn)
        elif choice == "4":
            query_item(conn)
        elif choice == "5":
            query_all_items(conn)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

