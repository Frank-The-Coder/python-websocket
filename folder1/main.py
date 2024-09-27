import sys
from PyQt5.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                             QLineEdit, QTableWidget, QTableWidgetItem, QFrame, QHeaderView, QScrollArea)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QTimer, Qt

ICON_PATH = "C:\\Users\\Owner\\Desktop\\favicon.ico"

class MainWindowNew(QWidget):
    def __init__(self):
        super().__init__()
        # Set the style in the beginning
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(245,245,250);
                font-family: 'Microsoft Yahei', tahoma, arial, 'Hiragino Sans GB', 'Hiragino Sans GB W3', 宋体;
                font-size: 14px;
            }
            QLineEdit {
                border: 1px solid #C2C2C2;
                border-radius: 4px;
                float: left;
                background-color: #fff;
                padding-left: 3px;
            }
            QLineEdit:focus {
                border-color: #3b7cff;
            }

            QLabel#textLabel1 { margin-right: 8px; }
            QLabel#textLabel2 { margin-right: 8px; }

            QLineEdit#inputBar1 { color: #5e5e5e; }
            QLineEdit#inputBar2 { color: #1771eb; }

            QPushButton#specificButton {
                background-color: #909090;
                color: #fff;
                border: none;
                border-radius: 5px;
            }
        """)

        # Set the window icon
        self.setWindowIcon(
            QIcon(ICON_PATH))
        self.setWindowTitle("链接ERP服务控制台")
        self.resize(800, 450)  # Set the size of the window

        # Create the main vertical layout
        self.main_layout = QVBoxLayout()
        # Create a QHBoxLayout for the top part
        self.top_layout = QHBoxLayout()
        self.top_layout2 = QHBoxLayout()

        # Create a QLabel for the text, a QLineEdit for the input bar, and a QPushButton for the button
        self.text_label = QLabel("连接ERP地址")
        self.input_bar = QLineEdit()
        self.button = QPushButton("连接ERP地址设置")
        self.button.setObjectName("specificButton")  # Add this line for the button styling
        # Assigning ID to an object for stylesheet selector
        self.text_label.setObjectName("textLabel1")
        self.input_bar.setObjectName("inputBar1")

        self.text_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.text_label.setFixedWidth(100)
        self.text_label.setFixedHeight(28)

        self.input_bar.setFixedWidth(250)
        self.input_bar.setFixedHeight(26)

        self.button.setFixedWidth(150)
        self.button.setFixedHeight(30)

        # Add the QLabel, QLineEdit, and QPushButton to the top_layout
        self.top_layout.addWidget(self.text_label)
        self.top_layout.addWidget(self.input_bar)
        self.top_layout.addWidget(self.button)

        self.text_label_2 = QLabel("CRM地址")
        self.input_bar_2 = QLineEdit()
        self.button_2 = QPushButton("数据交换接口配置")
        self.button_2.setObjectName("specificButton")  # Add this line for the button styling

        # Assigning ID to an object for stylesheet selector
        self.text_label_2.setObjectName("textLabel2")
        self.input_bar_2.setObjectName("inputBar2")

        self.text_label_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.text_label_2.setFixedWidth(100)
        self.text_label_2.setFixedHeight(28)

        self.input_bar_2.setFixedWidth(250)
        self.input_bar_2.setFixedHeight(26)

        self.button_2.setFixedWidth(150)
        self.button_2.setFixedHeight(30)

        # Add the QLabel, QLineEdit, and QPushButton to the top_layout
        self.top_layout2.addWidget(self.text_label_2)
        self.top_layout2.addWidget(self.input_bar_2)
        self.top_layout2.addWidget(self.button_2)

        self.top_layout.addStretch()
        self.top_layout2.addStretch()

        # Create a QFrame for the table "box"
        self.table_frame = QFrame(self)

        # Create a QVBoxLayout for the frame, so we can place the table inside
        self.table_layout = QVBoxLayout()
        self.inner_container = QWidget(self.table_frame)
        self.inner_container.setStyleSheet("QWidget { border: none;}")
        self.inner_layout = QVBoxLayout()

        # Create a QTableWidget with 1 row and 6 columns
        self.table = QTableWidget(9, 6)

        # You can set the headers for the table columns if you want, for demonstration:
        headers = ['ERP账套名称', '接口名称', '数据对接方向',
                   '频率', '最近一次时间', '操作']
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color:white;}")

        # Adjust column widths:
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 50)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 80)
        self.table.setRowHeight(0, 30)

        # Add the vertical scrollbar:
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Setting padding for the layout to provide space inside the frame
        self.table_layout.setContentsMargins(8, 10, 0, 6)
        self.inner_layout.setContentsMargins(0, 0, 0, 0)
        self.table_frame.setStyleSheet(
            "QFrame { background-color: white; border: 1px solid black; }")
        self.table.setStyleSheet("""
            QTableWidget{
                border-left: 1px solid #C2C2C2;
            }
            QHeaderView::section {
                background-color: white;
                border-top: 1px solid #C2C2C2;
                border-right:1px solid #C2C2C2;
                border-bottom:1px solid #C2C2C2;
            }
        """)
        self.table_frame.setFixedHeight(167)
        self.table.verticalHeader().setVisible(False)
        self.table.setFrameStyle(QFrame.NoFrame)
        
        # Add table to the layout of the frame
        self.inner_layout.addWidget(self.table)
        self.inner_container.setLayout(self.inner_layout)
        self.table_layout.addWidget(self.inner_container)




        # Create a QFrame for the log
        self.log_frame = QFrame(self)
        self.log_frame.setStyleSheet("font-size: 12px;")

        # Create a QVBoxLayout for the frame
        self.log_layout = QVBoxLayout()
        self.log_layout.setContentsMargins(10,4,0,0)
        self.log_layout.setSpacing(0)

        # Create the QScrollArea and its settings
        self.inner_log_container = QScrollArea(self.log_frame)
        self.inner_log_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.inner_log_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.inner_log_container.setStyleSheet("QScrollArea { border: none; }")

        # Create the inner widget that will be housed within the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("QWidget{background-color:white;}")
        self.inner_log_layout = QVBoxLayout(self.scroll_widget)
        self.inner_log_layout.setContentsMargins(0, 0, 0, 0)
        self.inner_log_layout.setSpacing(0)

        # Create labels and add them to the inner layout
        section_contents = ["数据同步：", "【CRM-ERP】", "销售订单接口没有查询到需要对接的数据！【2023-05-05 12:11:41】"]
        widths = [65, 80, 500]

        for _ in range(20):  # for 20 lines
            line_layout = QHBoxLayout()

            for i, width in enumerate(widths):
                # Create label
                label = QLabel(section_contents[i])
                
                label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                label.setFixedSize(width, 22)
                line_layout.addWidget(label)

            line_layout.addStretch()
            line_layout.setSpacing(0)
            self.inner_log_layout.addLayout(line_layout)

        # Set the inner widget as the content of the QScrollArea
        self.inner_log_container.setWidget(self.scroll_widget)

        # Add the QScrollArea to the main layout
        self.log_layout.addWidget(self.inner_log_container)
        self.log_frame.setLayout(self.log_layout)
        self.log_frame.setStyleSheet("QFrame { background-color: white; border: 1px solid black;}")
        #self.log_frame.setFixedHeight(180)


        # Set the frame's layout
        self.table_frame.setLayout(self.table_layout)
        self.main_layout.addLayout(self.top_layout, 0)
        self.main_layout.addLayout(self.top_layout2, 0)
        self.main_layout.addWidget(self.table_frame, 0)
        self.log_frame.setLayout(self.log_layout)
        self.main_layout.addWidget(self.log_frame, 1)

        # Set the layout for the QWidget
        self.setLayout(self.main_layout)

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

        
        # Now, iterate through the labels in the inner_log_layout and reapply their specific styles
        for i in range(self.inner_log_layout.count()):
            line_layout = self.inner_log_layout.itemAt(i)
            for j in range(line_layout.count()):
                label = line_layout.itemAt(j).widget()
                if isinstance(label, QLabel):
                    label.setStyleSheet("""
                        QLabel {
                            border: none;
                            font-size: 12px;
                        }
                    """)
        
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindowNew()  # Use the new main window directly
    tray = SystemTray(win)  # Pass the new window as parent to the tray
    win.show()
    sys.exit(app.exec_())
