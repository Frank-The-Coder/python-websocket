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
import pyqt_ui2
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


# PyQt部分
class MainWindowNew(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = pyqt_ui2.Ui_MainWindow()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QIcon(ICON_PATH))
        ui.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", "灵当CRM服务控制台"))
        ui.pushButton_9.clicked.connect(self.import_certificate)
        ui.pushButton_10.clicked.connect(self.import_key)
        ui.lineEdit_13.setText(_translate("MainWindow", socketport))
        ui.pushButton.clicked.connect(lambda: self.save_socketport(ui))
        if http == "":
            self.ask_http()

        ui.pushButton_11.clicked.connect(self.ask_http)

    def import_certificate(self):
        # 打开文件对话框
        global certfile
        certfile, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if certfile:
            config["certpath"] = certfile
            save_config(config)
            print(f'File imported: {certfile}')

    def import_key(self):
        # 打开文件对话框
        global keyfile
        keyfile, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if keyfile:
            config["keypath"] = keyfile
            save_config(config)
            print(f'File imported: {keyfile}')

    def ask_http(self):
        global http
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('网络协议')
        msg_box.setText("您使用的网络协议是？")
        http_button = msg_box.addButton("HTTP", QMessageBox.NoRole)
        https_button = msg_box.addButton("HTTPS", QMessageBox.YesRole)

        result = msg_box.exec_()

        if msg_box.clickedButton() == http_button:
            http = "http"
            self.show_success_message("更改成功，需重启控制台生效！")
        elif msg_box.clickedButton() == https_button:
            http = "https"
            self.show_success_message("更改成功，需重启控制台生效！")
        elif result == QMessageBox.Rejected:  # The "X" button
            http = config["http"]

        config["http"] = http
        save_config(config)

    def save_socketport(self, ui):
        # 打开文件对话框
        global socketport, socketio
        socketport = ui.lineEdit_13.text()
        config["socketport"] = socketport
        save_config(config)

        # 显示自定义成功提示框
        self.show_success_message("保存成功，需重启控制台生效！")

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
        # 计算窗口中心位置
        center_x = (self.width() - self.msg_label.width()) // 2
        center_y = (self.height() - self.msg_label.height()) // 2
        self.msg_label.move(center_x, center_y)
        self.msg_label.show()

        # 使用计时器关闭提示框
        QtCore.QTimer.singleShot(3000, self.msg_label.close)  # 提示框显示 1 秒后关闭

    def closeEvent(self, event):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('提醒')
        msg_box.setText("是否隐藏到托盘？")
        yes_button = msg_box.addButton("是", QMessageBox.NoRole)
        no_button = msg_box.addButton("否", QMessageBox.YesRole)

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
        quit_action = QAction("退出程序", self.parent())
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

    # 启动Flask服务器线程
    flask_thread = threading.Thread(target=run_flask_app, daemon=True)
    flask_thread.start()

    win.show()
    sys.exit(qt_app.exec_())
