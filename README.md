# Overview

As a young and dedicated software engineer I am excited to present this Inventory Management System. This software is designed to offer a straightforward and interactive interface for managing an inventory. It's written in Python and utilizes a SQL relational database - SQLite3 in our case, storing and manipulating the inventory data.

To use the program, you simply run the Python script in a terminal or command line interface. The system will then present you with a variety of options, including adding an item to the inventory, updating an item's quantity, deleting an item, or retrieving information about one or all items in the inventory.

The purpose of writing this software was to deepen my understanding of Python and SQLite3 and to gain more experience with relational databases and SQL commands.

[Software Demo Video](https://www.youtube.com/watch?v=IqYMLZF-jMs)

# Relational Database

I have utilized SQLite3 for this project - a lightweight, file-based relational database system. SQLite3 offers all the core features of a relational database, which has made it a perfect fit for this inventory management system.

The structure of the relational database I created consists of a single table, named 'items'. This table contains four columns: 'id' (an auto-incrementing primary key), 'name' (the name of the inventory item), 'quantity' (the quantity of the item in stock), and 'last_updated' (the timestamp of the last time the item was added or updated).

# Development Environment

To develop this software, I used Visual Studio Code as the primary text editor due to its ease of use and support for Python and SQLite.

The software is written in Python 3, and I have used the sqlite3 module, which comes out-of-the-box with Python, for interacting with the SQLite database. 

# Useful Websites

Here are a couple websites that I found helpful while working on this project:

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)

# Future Work

This software works well for basic inventory management. However, there are always opportunities for improvement and additional features to consider. Some future enhancements include:

- Adding a feature to sort and display based on filters
- Improving user interface with GUI as well as more error handling
- Enhancing the database model to include more details about the item 
