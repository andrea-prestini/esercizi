from flask import Flask, render_template
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

    welcome_message = rows
    return render_template('index.html', todos = rows)


@app.route('/hello')
def hello():
    return "Ciao mondo infame!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
