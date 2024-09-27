# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 645)
        MainWindow.setStyleSheet("MainWindow{\n"
"    background: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background: #ffffff;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setStyleSheet("            QPushButton {\n"
"                background: #f0f0f0;\n"
"                border: none;\n"
"                font-size: 12px;\n"
"                padding: 10px;\n"
"text-align: left;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: #e0e0e0;\n"
"            }\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background: #c0c0c0;\n"
"    border: 1px solid #a0a0a0;\n"
"}\n"
"\n"
"QWidget{\n"
"    background: #f0f0f0;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.splitter = QtWidgets.QSplitter(self.page1)
        self.splitter.setGeometry(QtCore.QRect(10, 90, 551, 41))
        self.splitter.setStyleSheet("            QPushButton {\n"
"                background: #f0f0f0;\n"
"                border: none;\n"
"                font-size: 12px;\n"
"                padding: 10px;\n"
"text-align: center;\n"
"            }")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(55)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.pushButton_9 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(20, 20, 541, 51))
        self.label.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_11 = QtWidgets.QPushButton(self.page1)
        self.pushButton_11.setGeometry(QtCore.QRect(350, 20, 201, 41))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: #3B7CFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3.sizePolicy().hasHeightForWidth())
        self.page3.setSizePolicy(sizePolicy)
        self.page3.setObjectName("page3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(574, 540))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    border: none;\n"
"}            \n"
"\n"
"QTableWidget::item {\n"
"                border: 1px solid #d0d0d0;\n"
"                padding: 5px;\n"
"            }\n"
"            QHeaderView::section {\n"
"                background-color: #f0f0f0;\n"
"                padding: 5px;\n"
"                border: 1px solid #d0d0d0;\n"
"                font-weight: bold;\n"
"            }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.stackedWidget.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stackedWidget.addWidget(self.page6)
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.stackedWidget.addWidget(self.page7)
        self.page8 = QtWidgets.QWidget()
        self.page8.setObjectName("page8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_3 = QtWidgets.QWidget(self.page8)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setObjectName("formLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_5)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setMinimumSize(QtCore.QSize(96, 26))
        self.label_5.setMaximumSize(QtCore.QSize(96, 26))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setMinimumSize(QtCore.QSize(96, 26))
        self.label_4.setMaximumSize(QtCore.QSize(96, 26))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.widget_5)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(402, 26))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(402, 26))
        self.lineEdit_13.setFrame(True)
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(402, 26))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(402, 26))
        self.lineEdit_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet("QLineEdit:disabled { background-color: #F0F0F0; color: #303030; border: 1px solid #D0D0D0; border-radius: 3px;}")
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setPlaceholderText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_2.addWidget(self.splitter_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.widget_5)
        spacerItem2 = QtWidgets.QSpacerItem(485, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #3B7CFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout_9.addWidget(self.widget_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page8)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "HTTPS证书"))
        self.pushButton_4.setText(_translate("MainWindow", "消息推送"))
        self.pushButton_1.setText(_translate("MainWindow", "设置"))
        self.pushButton_9.setText(_translate("MainWindow", "引入证书文件（certificate）"))
        self.pushButton_10.setText(_translate("MainWindow", "引入密钥文件（key）"))
        self.label.setText(_translate("MainWindow", "网络协议配置"))
        self.pushButton_11.setText(_translate("MainWindow", "更改协议（HTTP/HTTPS）"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "消息类型"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "推送频率"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "操作"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "企业微信"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "3分钟"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "启动/停止 日志"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "钉钉"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "3分钟"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "启动/停止 日志"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "自建应用"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "3分钟"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "启动/停止 日志"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "泛微OA"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "3分钟"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "启动/停止 日志"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "WEB端弹窗"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "30秒"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "启动/停止 日志"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "Socket端口："))
        self.label_4.setText(_translate("MainWindow", "Socket服务名："))
        self.lineEdit_13.setText(_translate("MainWindow", "5000"))
        self.lineEdit_16.setText(_translate("MainWindow", "lingdangsocket"))
        self.pushButton.setText(_translate("MainWindow", "保存"))
