import sqlite3
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit, disconnect
from flask_cors import CORS
import os
import threading
from engineio.async_drivers import gevent
import ssl
import sys
import warnings
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from qt_ui import pyqt_ui2
import json

# Flask section
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

API_KEY = '' 
connected_clients = []

# To record each IP's total number of connections
connections = {}
MAX_CONNECTIONS_PER_IP = 2000
CONFIG_FILE = "socket_config.json"
socketrun = False

ICON_PATH = "../img/favicon.ico"
TITLE = "Websocket Service Console"



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
        print(f"Client connected: {request.sid} Client IP: {client_ip} (Total: {connections[client_ip]})")
        socketio.emit('error', {'data': 'Too many connections from this IP!'})
        disconnect(request.sid)
    else:
        print(f"Client connected: {request.sid} Client IP: {client_ip} (Total: {connections[client_ip]})")


@socketio.on('disconnect')
def handle_disconnect():
    client_ip = request.remote_addr
    if client_ip in connections:
        connections[client_ip] -= 1
        if connections[client_ip] <= 0:
            del connections[client_ip]

    print(f"Client disconnected: {request.sid} Client IP: {client_ip} (Remaining: {connections.get(client_ip, 0)})")
    connected_clients.remove(request.sid)


def run_flask_app():
    global certfile, keyfile, socketrun, http

    if http == 'https':
        if os.path.exists(certfile) and os.path.exists(keyfile):
            socketio.run(app, host='0.0.0.0', port=int(socketport), certfile=certfile, keyfile=keyfile)
        print("The client is using HTTPS! Requires permission files!")
    else:
        socketio.run(app, host='0.0.0.0', port=int(socketport))


# PyQt Section
class MainWindowNew(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = pyqt_ui2.Ui_MainWindow()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QIcon(ICON_PATH))
        ui.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", TITLE))
        ui.pushButton_9.clicked.connect(self.import_certificate)
        ui.pushButton_10.clicked.connect(self.import_key)
        ui.lineEdit_13.setText(_translate("MainWindow", socketport))
        ui.pushButton.clicked.connect(lambda: self.save_socketport(ui))
        if http == "":
            self.ask_http()

        ui.pushButton_11.clicked.connect(self.ask_http)

    def import_certificate(self):
        # Open file dialog
        global certfile
        certfile, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if certfile:
            config["certpath"] = certfile
            save_config(config)
            print(f'File imported: {certfile}')

    def import_key(self):
        # Open File Dialogue
        global keyfile
        keyfile, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if keyfile:
            config["keypath"] = keyfile
            save_config(config)
            print(f'File imported: {keyfile}')

    def ask_http(self):
        global http
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Network protocol')
        msg_box.setText("What network protocol are you using?")
        http_button = msg_box.addButton("HTTP", QMessageBox.NoRole)
        https_button = msg_box.addButton("HTTPS", QMessageBox.YesRole)

        result = msg_box.exec_()

        if msg_box.clickedButton() == http_button:
            http = "http"
            self.show_success_message("Changed successfully, restart the program to apply changes!")
        elif msg_box.clickedButton() == https_button:
            http = "https"
            self.show_success_message("Changed successfully, restart the program to apply changes!")
        elif result == QMessageBox.Rejected:  # The "X" button
            http = config["http"]

        config["http"] = http
        save_config(config)

    def save_socketport(self, ui):
        # Open file dialogue
        global socketport, socketio
        socketport = ui.lineEdit_13.text()
        config["socketport"] = socketport
        save_config(config)

        # display sucessful customization message
        self.show_success_message("Saved successfully, restart the program to apply changes!")

    def show_success_message(self, message):
        self.msg_label = QtWidgets.QLabel(message, self)
        self.msg_label.setStyleSheet("""
            QLabel {
                background-color: #5cb85c;
                color: white;
                border: 1px solid #4cae4c;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setFixedSize(200, 50)
        # calculate centre poin
        center_x = (self.width() - self.msg_label.width()) // 2
        center_y = (self.height() - self.msg_label.height()) // 2
        self.msg_label.move(center_x, center_y)
        self.msg_label.show()

        # use timer to close success message
        QtCore.QTimer.singleShot(3000, self.msg_label.close)  # closes in 3 seconds

    def closeEvent(self, event):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Reminder')
        msg_box.setText("Minimize to tray?")
        yes_button = msg_box.addButton("Yes", QMessageBox.NoRole)
        no_button = msg_box.addButton("N", QMessageBox.YesRole)

        result = msg_box.exec_()

        if msg_box.clickedButton() == yes_button:
            event.ignore()
            self.hide()
        elif msg_box.clickedButton() == no_button:
            QApplication.quit()
        elif result == QMessageBox.Rejected:  # The "X" button
            msg_box.hide()
            self.show()

    def make_window_stay_on_top(self):
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()  # Required to re-show the window with the new flag set


class SystemTray(QSystemTrayIcon):
    def __init__(self, parent):
        super().__init__(parent)
        self.setIcon(QIcon(ICON_PATH))
        self.show()
        self.main_win = parent
        self.clickend = 1

        self.activated.connect(self.onTrayIconActivated)

        self.new_window = MainWindowNew()  # Only one instance

        self.menu = QMenu()
        quit_action = QAction("Quit application", self.parent())
        quit_action.triggered.connect(self.quit_app)
        self.menu.addAction(quit_action)

    def onTrayIconActivated(self, reason):
        if self.clickend == 1:
            self.clickend = 0
            if reason == QSystemTrayIcon.Trigger:
                if not self.new_window.isVisible():
                    self.new_window.make_window_stay_on_top()
                else:
                    self.new_window.hide()
            elif reason == QSystemTrayIcon.Context:
                self.showContextMenu()
            self.clickend = 1

    def showContextMenu(self):
        self.menu.popup(QCursor.pos())

    def open_window(self):
        self.main_win.show()
        self.new_window.hide()

    def quit_app(self):
        QApplication.quit()


if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    win = MainWindowNew()  # Use the new main window directly
    tray = SystemTray(win)  # Pass the new window as parent to the tray

    # Start Flask server thread
    flask_thread = threading.Thread(target=run_flask_app, daemon=True)
    flask_thread.start()

    win.show()
    sys.exit(qt_app.exec_())
