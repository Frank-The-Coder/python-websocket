# admin_gui.py

import sys
import warnings
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from qt_ui import pyqt_ui2

warnings.filterwarnings("ignore", category=DeprecationWarning)

ICON_PATH = "../img/favicon.ico"
TITLE = "Websocket Service Console"


class MainWindowNew(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = pyqt_ui2.Ui_MainWindow()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QIcon(ICON_PATH))
        ui.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", TITLE))

    def closeEvent(self, event):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Message')
        msg_box.setText("Minimize to tray？")
        yes_button = msg_box.addButton("Yes", QMessageBox.NoRole)
        no_button = msg_box.addButton("No", QMessageBox.YesRole)

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
    win.show()
    sys.exit(qt_app.exec_())
