import requests
import sqlite3

api_key = 'your_encrypt_key_here'

headers = {
    'X-API-KEY': api_key
}


def handle_user_message(message):
    conn = sqlite3.connect('../messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (receiver_id, message, sender_name, send_time) VALUES (?, ?, ?, ?)",
                   (message[0], message[1], message[2], message[3]))
    conn.commit()
    conn.close()

    notify_daemon(message)


def notify_daemon(message):
    response = requests.post('http://localhost:5000/notify', json={'message': message}, headers=headers,
                             proxies={"http": None, "https": None})
    if response.status_code == 200:
        print('Message sent to daemon successfully')
    else:
        print('Failed to send message to daemon')


# 示例调用
message_arr = ['1', 'Hello', 'userA', '2024-06-06 03:06:00']
handle_user_message(message_arr)
