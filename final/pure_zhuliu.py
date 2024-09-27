import sqlite3
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit, disconnect
from flask_cors import CORS
import os
from engineio.async_drivers import gevent
import json

# Flask部分
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

API_KEY = 'lingdang20240617messagekey'  # Replace with your actual API key
connected_clients = []

# 用于记录每个IP地址的连接数
connections = {}
MAX_CONNECTIONS_PER_IP = 2000
CONFIG_FILE = "socket_config.json"
socketrun = False

ICON_PATH = "favicon.ico"


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        return {"certpath": "", "keypath": ""}


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)


config = load_config()
certfile = config["certpath"]
keyfile = config["keypath"]
socketport = config["socketport"]
http = config["http"]


@app.route('/notify', methods=['POST'])
def notify():
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    notify_clients(message)
    return jsonify({'status': 'Message sent'}), 200


def notify_clients(message):
    socketio.emit('message', {'data': message})


@socketio.on('connect')
def handle_connect():
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


def run_flask_app():
    global certfile, keyfile, socketrun, http

    if http == 'https':
        if os.path.exists(certfile) and os.path.exists(keyfile):
            socketio.run(app, host='0.0.0.0', port=int(socketport), certfile=certfile, keyfile=keyfile)
        print("客户正在使用https!!!")
    else:
        socketio.run(app, host='0.0.0.0', port=int(socketport))


if __name__ == '__main__':
    run_flask_app()
