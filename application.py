import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dewey-is-THe-CuTeST-puppy-D0g-IN-the-wh0l3-3ntir3-w0rld'

def connect_database():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def index():
    connection = connect_database()
    posts = connection.execute(
        'SELECT posts.id, post_created, post_file_location, post_caption, username'
        ' FROM posts JOIN users'
        ' ON posts.post_author = users.id'
        ).fetchall()
    users = connection.execute('SELECT * FROM users').fetchall()
    connection.close()
    return render_template('index.html', posts=posts, users=users)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        post_author = request.form['post_author']
        post_file_location = request.form['post_file_location']
        post_caption = request.form['post_caption']
        
        if not post_author:
            flash('Author is required! Please enter an author.')
        elif not post_caption:
            flash('A caption is required. Please enter a caption.')
        else:
            connection = connect_database()
            connection.execute(
                'INSERT INTO posts (post_author, post_file_location, post_caption)'
                ' VALUES (?, ?, ?)',
                (post_author, post_file_location, post_caption)
            )
            connection.commit()
            connection.close()
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug = True)