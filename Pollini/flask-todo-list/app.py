from flask import Flask, redirect, render_template, request, url_for
from markupsafe import escape
import sqlite3 as sq


app = Flask(__name__)


def get_db():
    conn = sq.connect('todo.sqlite3')
    conn.row_factory = sq.Row
    return conn


@app.route('/')
def index():
    # get data from database
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos')
    rows = cur.fetchall()
    conn.close()

    return render_template('index.html', todos=rows)


@app.route('/hello')
def hello():
    return "Ciao mondo infame!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/add', methods=['POST'])
def add_todo():
    # get data from form
    title = request.form.get('title')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos(title, done) VALUES (?, ?)', (title, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    # get data from form
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
