import sqlite3 as sq

# Create a database from db.sql
conn = sq.connect('todo.sqlite3')

with open('todo.sql', 'r') as f:
    conn.executescript(f.read())

conn.close()
