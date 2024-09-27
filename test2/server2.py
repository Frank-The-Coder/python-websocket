import requests
import sqlite3


def handle_user_message(user_id, message):
    conn = sqlite3.connect('../messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

    notify_daemon(message)


def notify_daemon(message):
    response = requests.post('http://localhost:5000/notify', json={'message': message})
    if response.status_code == 200:
        print('Message sent to daemon successfully')
    else:
        print('Failed to send message to daemon')


# 示例调用
handle_user_message('userA', 'Hello, userB!')

