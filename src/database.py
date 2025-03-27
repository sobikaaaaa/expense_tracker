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
def add_transaction(date,t_type,amount,category,description):
   

    conn=sqlite3.connect("transaction.db")
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO transactions (date,type,amount,category,description)
    VALUES(?,?,?,?,?)
    ''',(date,t_type,amount,category,description))
    
    conn.commit()
    conn.close()
def get_transactions():
    conn=sqlite3.connect("transaction.db")
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM transactions
    ''')    
    transactions=cursor.fetchall()
    conn.close()
    return transactions
        
init_db()
add_transaction("2025-03-27","income","15000","Grocery"," ")
all_transaction=get_transactions()
print(all_transaction)
