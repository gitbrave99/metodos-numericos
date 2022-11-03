# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainReglasebzdpE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(777, 418)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 100, 81, 16))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxTipoRegla = QComboBox(self.centralwidget)
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.setObjectName(u"cbxTipoRegla")
        self.cbxTipoRegla.setGeometry(QRect(390, 60, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.cbxTipoRegla.setFont(font1)
        self.cbxTipoRegla.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(231, 230, 234); \n"
"border: 1px solid #ced4da;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"border:0;\n"
"}\n"
"QComboBox:on\n"
"{\n"
"border: 4px solid #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"font-size:12px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"padding: 5px;\n"
"background-color: #fff;\n"
"outline:0px;\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left: 10px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover{\n"
"		background-color: #1e90ff;\n"
"}\n"
"\n"
"QComboBox QListView::item:selected{\n"
"		background-color: #1e90ff;\n"
"}\n"
"\n"
"")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 100, 81, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinB = QDoubleSpinBox(self.centralwidget)
        self.spinB.setObjectName(u"spinB")
        self.spinB.setGeometry(QRect(150, 120, 101, 22))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.spinB.setFont(font2)
        self.spinB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinB.setDecimals(4)
        self.spinA = QDoubleSpinBox(self.centralwidget)
        self.spinA.setObjectName(u"spinA")
        self.spinA.setGeometry(QRect(20, 120, 101, 22))
        self.spinA.setFont(font2)
        self.spinA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinA.setDecimals(4)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(390, 35, 81, 21))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtH = QLineEdit(self.centralwidget)
        self.txtH.setObjectName(u"txtH")
        self.txtH.setEnabled(False)
        self.txtH.setGeometry(QRect(560, 175, 181, 21))
        font3 = QFont()
        font3.setPointSize(11)
        self.txtH.setFont(font3)
        self.txtH.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtH.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.spinN = QDoubleSpinBox(self.centralwidget)
        self.spinN.setObjectName(u"spinN")
        self.spinN.setGeometry(QRect(280, 120, 101, 22))
        self.spinN.setFont(font2)
        self.spinN.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinN.setDecimals(0)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(520, 180, 31, 16))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tblXFx = QTableWidget(self.centralwidget)
        if (self.tblXFx.columnCount() < 4):
            self.tblXFx.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblXFx.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblXFx.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblXFx.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblXFx.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblXFx.setObjectName(u"tblXFx")
        self.tblXFx.setGeometry(QRect(20, 180, 471, 192))
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 35, 81, 16))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 100, 81, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtFormula = QLineEdit(self.centralwidget)
        self.txtFormula.setObjectName(u"txtFormula")
        self.txtFormula.setGeometry(QRect(20, 60, 291, 21))
        self.txtFormula.setFont(font3)
        self.txtFormula.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtFormula.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(520, 220, 31, 16))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtH_2 = QLineEdit(self.centralwidget)
        self.txtH_2.setObjectName(u"txtH_2")
        self.txtH_2.setEnabled(False)
        self.txtH_2.setGeometry(QRect(560, 215, 181, 21))
        self.txtH_2.setFont(font3)
        self.txtH_2.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtH_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tarea", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.cbxTipoRegla.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione opci\u00f3n", None))
        self.cbxTipoRegla.setItemText(1, QCoreApplication.translate("MainWindow", u"Trapecio Simple", None))
        self.cbxTipoRegla.setItemText(2, QCoreApplication.translate("MainWindow", u"Trapecio M\u00faltiple", None))
        self.cbxTipoRegla.setItemText(3, QCoreApplication.translate("MainWindow", u"Simpson 1/3", None))
        self.cbxTipoRegla.setItemText(4, QCoreApplication.translate("MainWindow", u"Simpson 1/3 m\u00faltiple", None))
        self.cbxTipoRegla.setItemText(5, QCoreApplication.translate("MainWindow", u"Simpson 3/8", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Regla", None))
        self.txtH.setText("")
        self.txtH.setPlaceholderText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"H =", None))
        ___qtablewidgetitem = self.tblXFx.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tblXFx.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"V", None));
        ___qtablewidgetitem2 = self.tblXFx.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"F(x)", None));
        ___qtablewidgetitem3 = self.tblXFx.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"V", None));
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"F\u00f3rmula", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.txtFormula.setText("")
        self.txtFormula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejemplo: 0.2+25x-200x", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"I =", None))
        self.txtH_2.setText("")
        self.txtH_2.setPlaceholderText("")
    # retranslateUi

