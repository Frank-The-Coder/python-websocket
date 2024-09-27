import eventlet

eventlet.monkey_patch()
import sqlite3
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import threading
from engineio.async_drivers import gevent
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

    certfile = 'ssl/cert.pem'
    keyfile = 'ssl/key.pem'

    socketio.run(app, host='0.0.0.0', port=5000, certfile=certfile, keyfile=keyfile)
