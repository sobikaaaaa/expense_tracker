import sqlite3
def init_db():
    conn=sqlite3.connect("transaction.db")
    cursor=conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    type TEXT CHECK (type IN("income","expense"))NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT
    )
    
    ''')
    conn.commit()
    conn.close()
init_db()