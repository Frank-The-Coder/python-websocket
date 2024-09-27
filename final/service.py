import sqlite3
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit, disconnect
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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

API_KEY = 'lingdang20240617messagekey'  # Replace with your actual API key

connected_clients = []

# 用于记录每个IP地址的连接数
connections = {}
MAX_CONNECTIONS_PER_IP = 1000


@app.route('/notify', methods=['POST'])
def notify():
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    message = request.json.get('message')
    notify_clients(message)
    return jsonify({'status': 'Message sent'}), 200


def notify_clients(message):
    socketio.emit('message', {'data': message})


@socketio.on('connect')
def handle_connect():
    # emit('message', {'data': '连接成功'}, room=request.sid)
    client_ip = request.remote_addr
    if client_ip not in connections:
        connections[client_ip] = 0
    connections[client_ip] += 1
    connected_clients.append(request.sid)

    if connections[client_ip] > MAX_CONNECTIONS_PER_IP:
        print(f"客户端连接: {request.sid} 客户端IP: {client_ip} (总数: {connections[client_ip]})")
        socketio.emit('error', {'data': '此IP建立过多连接！'})
        disconnect(request.sid)
    else:
        print(f"客户端连接: {request.sid} 客户端IP: {client_ip} (总数: {connections[client_ip]})")


@socketio.on('disconnect')
def handle_disconnect():
    client_ip = request.remote_addr
    if client_ip in connections:
        connections[client_ip] -= 1
        if connections[client_ip] <= 0:
            del connections[client_ip]

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
    certfile = '/usr/local/nginx/conf/ssl_81com/81mis.com_bundle.crt'
    keyfile = '/usr/local/nginx/conf/ssl_81com/81mis.com.key'
    socketio.run(app, host='0.0.0.0', port=5000, certfile=certfile, keyfile=keyfile)
