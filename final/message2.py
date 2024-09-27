import sqlite3
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit, disconnect, join_room, leave_room
from flask_cors import CORS
import os
import threading
from engineio.async_drivers import gevent
import ssl
import warnings
import requests

# Suppress only the InsecureRequestWarning from urllib3
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

API_KEY = 'lingdang20240617messagekey'  # Replace with your actual API key

connected_clients = []

# 用于记录每个IP地址的连接数
connections = {}
user_rooms = {}  # 存储用户所在的账套信息
MAX_CONNECTIONS_PER_IP = 1000


@app.route('/notify', methods=['POST'])
def notify():
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    message = request.json.get('message')
    # if not message or not isinstance(message, list) or len(message) < 8:
    #     return jsonify({'error': 'Invalid message format'}), 400

    user_id = message[0]
    account = message[6]

    notify_clients(message, user_id, account)
    return jsonify({'status': 'Message sent'}), 200


def notify_clients(message, user_id, account):
    room = f'{user_id}_{account}'
    socketio.emit('message', {'data': message}, room=room)


@socketio.on('connect')
def handle_connect():
    client_ip = request.remote_addr
    if client_ip not in connections:
        connections[client_ip] = 0
    connections[client_ip] += 1
    connected_clients.append(request.sid)

    if connections[client_ip] > MAX_CONNECTIONS_PER_IP:
        print(f"客户端连接: {request.sid} 客户端IP: {client_ip} (总数: {connections[client_ip]})")
        socketio.emit('error', {'data': '此IP建立过多连接！'}, to=request.sid)
        disconnect(request.sid)
    else:
        print(f"客户端连接: {request.sid} 客户端IP: {client_ip} (总数: {connections[client_ip]})")


@socketio.on('join')
def on_join(data):
    user_id = data['user_id']
    account = data['account']  # 用户账套信息
    room = f'{user_id}_{account}'
    join_room(room)
    user_rooms[request.sid] = room
    emit('message', {'data': f'Joined room: {room}'})


@socketio.on('leave')
def on_leave(data):
    user_id = data['user_id']
    account = data['account']  # 用户账套信息
    room = f'{user_id}_{account}'
    leave_room(room)
    user_rooms.pop(request.sid, None)
    emit('message', {'data': f'Left room: {room}'})


@socketio.on('disconnect')
def handle_disconnect():
    client_ip = request.remote_addr
    if client_ip in connections:
        connections[client_ip] -= 1
        if connections[client_ip] <= 0:
            del connections[client_ip]

    room = user_rooms.pop(request.sid, None)
    if room:
        leave_room(room)
    print(f"客户端断开: {request.sid}  客户端IP: {client_ip} (剩余: {connections.get(client_ip, 0)})")
    connected_clients.remove(request.sid)


def db_check_and_notify():
    while True:
        conn = sqlite3.connect('../messages.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messages WHERE user_id = 'userA'")
        messages = cursor.fetchall()
        conn.close()
        for message in messages:
            notify_clients(message)


if __name__ == '__main__':
    # threading.Thread(target=db_check_and_notify, daemon=True).start()
    # Determine the scheme dynamically based on the request
    scheme = 'https' if 'HTTPS' in os.environ and os.environ['HTTPS'] == 'on' else 'http'

    # Run the server based on the scheme
    if scheme == 'https':
        certfile = '/usr/local/nginx/conf/ssl_81com/81mis.com_bundle.crt'
        keyfile = '/usr/local/nginx/conf/ssl_81com/81mis.com.key'
        if os.path.exists(certfile) and os.path.exists(keyfile):
            socketio.run(app, host='0.0.0.0', port=5000, certfile=certfile, keyfile=keyfile)
        print("客户正在使用https!!!")
    else:
        socketio.run(app, host='0.0.0.0', port=5000)
