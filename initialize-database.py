import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
    ('dewey', 'dog')
    )

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
    ('fitz', 'man')
    )

cursor.execute("INSERT INTO posts (post_author, post_file_location, post_caption) VALUES (?, ?, ?)",
    (1, 'test_file_location_1.jpg', 'This is the first test post.')
    )

cursor.execute("INSERT INTO posts (post_author, post_file_location, post_caption) VALUES (?, ?, ?)",
    (1, 'test_file_location_2.jpg', 'This is the second test post.')
    )

cursor.execute("INSERT INTO posts (post_author, post_file_location, post_caption) VALUES (?, ?, ?)",
    (1, 'test_file_location_3.jpg', 'This is the third test post.')
    )

cursor.execute("INSERT INTO tags (tag_name, tag_description) VALUES (?, ?)",
    ('Tag 1', 'Test tag 1.')
    )

cursor.execute("INSERT INTO tags (tag_name, tag_description) VALUES (?, ?)",
    ('Tag 2', 'Test tag 2.')
    )

connection.commit()
connection.close()