# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_PrincipalGXMvpn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Principal(object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.resize(640, 454)
        self.centralwidget = QWidget(Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.miStack = QStackedWidget(self.centralwidget)
        self.miStack.setObjectName(u"miStack")
        self.miStack.setGeometry(QRect(40, 70, 561, 291))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(158, 200, 255)\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 70, 201, 31))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 40, 91, 21))
        self.label_4.setStyleSheet(u"font-size:20px;")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 140, 201, 31))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 110, 101, 21))
        self.label_5.setStyleSheet(u"font-size:20px;")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(300, 70, 221, 171))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 40, 101, 21))
        self.label_6.setStyleSheet(u"font-size:20px;")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 210, 201, 31))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 180, 101, 21))
        self.label_7.setStyleSheet(u"font-size:20px;")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(500, 270, 51, 16))
        self.label_14.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.frame)

        self.miStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color: rgb(130, 255, 108);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 30, 61, 21))
        self.label_8.setStyleSheet(u"font-size:20px;")
        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem28)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 60, 481, 201))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(500, 270, 51, 16))
        self.label_13.setStyleSheet(u"")

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.miStack.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	background-color: rgb(255, 251, 124);\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.frame_3)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 150, 171, 111))
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 110, 61, 21))
        self.label_9.setStyleSheet(u"font-size:20px;")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 60, 171, 31))
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 30, 61, 21))
        self.label_10.setStyleSheet(u"font-size:20px;")
        self.calendarWidget = QCalendarWidget(self.frame_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(240, 60, 301, 201))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 30, 121, 21))
        self.label_11.setStyleSheet(u"font-size:20px;")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(500, 270, 51, 16))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.miStack.addWidget(self.page_3)
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(40, 380, 181, 41))
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(240, 380, 161, 41))
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(420, 380, 181, 41))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(190, 20, 261, 31))
        self.label_15.setStyleSheet(u"font-size:25px;")
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)

        self.miStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(QCoreApplication.translate("Principal", u"QStackedWidget Slider - ALEX7320", None))
        self.label_4.setText(QCoreApplication.translate("Principal", u"Texto", None))
        self.label_5.setText(QCoreApplication.translate("Principal", u"Texto", None))
        self.label_6.setText(QCoreApplication.translate("Principal", u"Texto", None))
        self.label_7.setText(QCoreApplication.translate("Principal", u"Texto", None))
        self.label_14.setText(QCoreApplication.translate("Principal", u"index 1", None))
        self.label_8.setText(QCoreApplication.translate("Principal", u"Tabla", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Principal", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Principal", u"NOMBRE", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Principal", u"CORREO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Principal", u"CARGO", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Principal", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Principal", u"Nueva fila", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Principal", u"Nueva fila", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Principal", u"Nueva fila", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Principal", u"Nueva fila", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Principal", u"1", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Principal", u"Nombreuno", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Principal", u"uno@gmail.com", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Principal", u"Cargouno", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Principal", u"2", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Principal", u"Nombredos", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Principal", u"dos@gmail.com", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Principal", u"Cargodos", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Principal", u"3", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Principal", u"Nombretres", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Principal", u"tres@gmail.com", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Principal", u"Cargotres", None));
        ___qtablewidgetitem21 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Principal", u"4", None));
        ___qtablewidgetitem22 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Principal", u"Nombrecuatro", None));
        ___qtablewidgetitem23 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Principal", u"cuatro@gmail.com", None));
        ___qtablewidgetitem24 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Principal", u"Cargocuatro", None));
        ___qtablewidgetitem25 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Principal", u"5", None));
        ___qtablewidgetitem26 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Principal", u"Nombrecinco", None));
        ___qtablewidgetitem27 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Principal", u"cinco@gmail.com", None));
        ___qtablewidgetitem28 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Principal", u"Cargocinco", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_13.setText(QCoreApplication.translate("Principal", u"index 2", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Principal", u"Nuevo elemento", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_9.setText(QCoreApplication.translate("Principal", u"Lista", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Principal", u"Nuevo elemento", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Principal", u"Nuevo elemento", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Principal", u"Nuevo elemento", None))

        self.label_10.setText(QCoreApplication.translate("Principal", u"Opci\u00f3n", None))
        self.label_11.setText(QCoreApplication.translate("Principal", u"Calendario", None))
        self.label_12.setText(QCoreApplication.translate("Principal", u"index 3", None))
        self.btn1.setText(QCoreApplication.translate("Principal", u"1", None))
        self.btn2.setText(QCoreApplication.translate("Principal", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Principal", u"3", None))
        self.label_15.setText(QCoreApplication.translate("Principal", u"QStackedWidget Slider", None))
    # retranslateUi

