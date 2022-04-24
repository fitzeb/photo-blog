import sqlite3

# Define connection and cursor

connection = sqlite3.connect('app_database.db')
print("Created the Connection!")

cursor = connection.cursor()
print("Created the Cursor!")

with open('schema.sql') as f:
    connection.executescript(f.read())
    print("Opened the Schema!")

connection.commit()
connection.close()