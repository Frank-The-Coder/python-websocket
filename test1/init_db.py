# init_db.py
import sqlite3

conn = sqlite3.connect('messages.db')
cursor = conn.cursor()
cursor.execute('''
DROP TABLE IF EXISTS messages
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receiver_id TEXT NOT NULL,
    message TEXT NOT NULL,
    sender_name TEXT NOT NULL,
    send_time DATETIME
)
''')
conn.commit()
conn.close()
