import requests
import sqlite3
import socket


def handle_user_message(user_id, message):
    conn = sqlite3.connect('../messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

    notify_daemon(message)


def get_server_ip():
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())

    try:
        # 尝试获取外部IP地址
        external_ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        external_ip = 'Unable to get external IP'

    return local_ip, external_ip


def notify_daemon(message):
    local_ip, external_ip = get_server_ip()
    server_ip = external_ip if external_ip != 'Unable to get external IP' else local_ip
    response = requests.post(f'http://{server_ip}:5000/notify', json={'message': message})
    if response.status_code == 200:
        print('Message sent to daemon successfully')
    else:
        print('Failed to send message to daemon')


# 示例调用
handle_user_message('userA', 'Hello, userB!')
