import sqlite3

DB_PATH = 'my_app/products.db'

def get_DBconnection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()  

create_table()
