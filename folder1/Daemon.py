import sys
import threading
import socket
import sqlite3
import queue
from PyQt5.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox, QMainWindow)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from flask import Flask, Response
from flask_cors import CORS
import test1

ICON_PATH = "C:\\Users\\Owner\\Desktop\\favicon.ico"

# Flask application
app = Flask(__name__)
CORS(app)
clients = []


@app.route('/subscribe')
def subscribe():
    def gen():
        q = queue.Queue()
        clients.append(q)
        try:
            while True:
                msg = q.get()
                yield f'data: {msg}\n\n'
        except GeneratorExit:
            clients.remove(q)

    return Response(gen(), mimetype='text/event-stream')


def notify_clients(message):
    for client in clients:
        client.put(message)


# Background task to listen for socket messages
def db_check_and_notify():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 12345))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(1024)
        if data == b'1':
            conn = sqlite3.connect('../messages.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM messages WHERE user_id = 'userA'")
            messages = cursor.fetchall()
            conn.close()
            for message in messages:
                notify_clients(message)
        conn.close()
        s.close()


class MainWindowNew(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = test1.Ui_MainWindow()
        ui.setupUi(self)

    def closeEvent(self, event):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Message')
        msg_box.setText("是否隐藏到托盘？")
        yes_button = msg_box.addButton("是", QMessageBox.NoRole)
        no_button = msg_box.addButton("否", QMessageBox.YesRole)

        result = msg_box.exec_()
        print(result)

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

        # Create the context menu only once during initialization
        self.menu = QMenu()
        quit_action = QAction("退出程序", self.parent())
        quit_action.triggered.connect(self.quit_app)
        self.menu.addAction(quit_action)

    def onTrayIconActivated(self, reason):
        if self.clickend == 1:
            self.clickend = 0
            if reason == QSystemTrayIcon.Trigger:
                if not self.new_window.isVisible():
                    self.new_window.make_window_stay_on_top()  # Call the method to make the window stay on top
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


# Start the Flask application and background task
def start_flask_app():
    app.run(debug=True, use_reloader=False, threaded=True)


def start_background_task():
    threading.Thread(target=db_check_and_notify, daemon=True).start()


if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    win = MainWindowNew()  # Use the new main window directly
    tray = SystemTray(win)  # Pass the new window as parent to the tray

    flask_thread = threading.Thread(target=start_flask_app, daemon=True)
    flask_thread.start()

    start_background_task()

    win.show()
    sys.exit(qt_app.exec_())
