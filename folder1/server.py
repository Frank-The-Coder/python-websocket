# server.py
import socket
import sqlite3


def notify_daemon():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    s.sendall(b'1')
    s.close()


def handle_user_message(user_id, message):
    conn = sqlite3.connect('../messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

    notify_daemon()


# 示例调用
handle_user_message('userA', 'Hello, userB!')
