import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import threading
from engineio.async_drivers import gevent

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


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
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
