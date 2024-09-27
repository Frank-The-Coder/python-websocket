import eventlet

eventlet.monkey_patch()
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import ssl

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

connected_clients = []


@app.route('/notify', methods=['POST'])
def notify():
    message = request.json.get('message')
    notify_clients(message)
    return jsonify({'status': 'Message sent'}), 200


def notify_clients(message):
    socketio.emit('message', {'data': message}, broadcast=True)


@socketio.on('connect')
def handle_connect():
    print(f"客户端连接: {request.sid}")
    connected_clients.append(request.sid)
    emit('message', {'data': '连接成功'}, room=request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    print(f"客户端断开: {request.sid}")
    connected_clients.remove(request.sid)


@socketio.on('message')
def handle_message(msg):
    print(f"收到消息: {msg}")
    send(f"回声: {msg}", room=request.sid)


@socketio.on('ping')
def handle_ping():
    print("收到ping")
    emit('pong', {'data': 'pong'}, room=request.sid)


if __name__ == '__main__':
    # 配置 SSL
    certfile = 'ssl/cert.pem'
    keyfile = 'ssl/key.pem'

    socketio.run(app, host='0.0.0.0', port=5000, certfile=certfile, keyfile=keyfile)
