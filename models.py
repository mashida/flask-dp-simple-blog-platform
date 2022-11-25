import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    """
    function that creates post.
    """
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    """f
    unction that gets all available posts
    """
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    con.close()
    return posts
