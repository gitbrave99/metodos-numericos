# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teswithframe.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(778, 499)
        icon = QIcon()
        icon.addFile(u"../assets/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 777, 501))
        self.frame.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 25, 81, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtFormula = QLineEdit(self.frame)
        self.txtFormula.setObjectName(u"txtFormula")
        self.txtFormula.setGeometry(QRect(30, 50, 501, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.txtFormula.setFont(font1)
        self.txtFormula.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtFormula.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.spinB = QDoubleSpinBox(self.frame)
        self.spinB.setObjectName(u"spinB")
        self.spinB.setGeometry(QRect(160, 110, 101, 22))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.spinB.setFont(font2)
        self.spinB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinB.setDecimals(4)
        self.spinB.setValue(0.800000000000000)
        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(510, 290, 31, 16))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 90, 81, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtFa = QLineEdit(self.frame)
        self.txtFa.setObjectName(u"txtFa")
        self.txtFa.setEnabled(False)
        self.txtFa.setGeometry(QRect(560, 380, 181, 21))
        self.txtFa.setFont(font1)
        self.txtFa.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtFa.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.spinA = QDoubleSpinBox(self.frame)
        self.spinA.setObjectName(u"spinA")
        self.spinA.setGeometry(QRect(30, 110, 101, 22))
        self.spinA.setFont(font2)
        self.spinA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinA.setDecimals(4)
        self.txtFb = QLineEdit(self.frame)
        self.txtFb.setObjectName(u"txtFb")
        self.txtFb.setEnabled(False)
        self.txtFb.setGeometry(QRect(560, 420, 181, 21))
        self.txtFb.setFont(font1)
        self.txtFb.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtFb.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtI = QLineEdit(self.frame)
        self.txtI.setObjectName(u"txtI")
        self.txtI.setEnabled(False)
        self.txtI.setGeometry(QRect(550, 285, 201, 21))
        self.txtI.setFont(font1)
        self.txtI.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtI.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(510, 385, 41, 16))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(570, 350, 141, 16))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinN = QDoubleSpinBox(self.frame)
        self.spinN.setObjectName(u"spinN")
        self.spinN.setGeometry(QRect(290, 110, 101, 22))
        self.spinN.setFont(font2)
        self.spinN.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinN.setDecimals(0)
        self.spinN.setValue(6.000000000000000)
        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(510, 245, 31, 16))
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tblXFx = QTableWidget(self.frame)
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
        self.tblXFx.setGeometry(QRect(30, 220, 471, 261))
        self.tblXFx.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: #55aaff;\n"
"	padding: 2px;\n"
"\n"
"	border:1px solid #fffff8;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	gridline-color: #ff00ff;\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"	background-color: #55aaff;\n"
"	border: 1px solid #ff0000;\n"
"}")
        self.tblXFx.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 90, 81, 16))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(510, 425, 41, 16))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(430, 75, 81, 21))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtH = QLineEdit(self.frame)
        self.txtH.setObjectName(u"txtH")
        self.txtH.setEnabled(False)
        self.txtH.setGeometry(QRect(550, 240, 201, 21))
        self.txtH.setFont(font1)
        self.txtH.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtH.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbxTipoRegla = QComboBox(self.frame)
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.addItem("")
        self.cbxTipoRegla.setObjectName(u"cbxTipoRegla")
        self.cbxTipoRegla.setGeometry(QRect(430, 100, 301, 31))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.cbxTipoRegla.setFont(font4)
        self.cbxTipoRegla.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
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
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 90, 81, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnCalcularMet = QPushButton(self.frame)
        self.btnCalcularMet.setObjectName(u"btnCalcularMet")
        self.btnCalcularMet.setGeometry(QRect(430, 150, 141, 28))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.btnCalcularMet.setFont(font5)
        self.btnCalcularMet.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCalcularMet.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(45,50,50);\n"
"	border: 2px solid rgb(81,93,93);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(81,93,93);\n"
"	border:2px solid rgb(45,50,50);\n"
"}\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"F\u00f3rmula", None))
        self.txtFormula.setText(QCoreApplication.translate("MainWindow", u"0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5", None))
        self.txtFormula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejemplo: 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"I =", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.txtFa.setText("")
        self.txtFa.setPlaceholderText("")
        self.txtFb.setText("")
        self.txtFb.setPlaceholderText("")
        self.txtI.setText("")
        self.txtI.setPlaceholderText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"F(a) =", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Trapecio Simple", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"H =", None))
        ___qtablewidgetitem = self.tblXFx.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tblXFx.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"V", None));
        ___qtablewidgetitem2 = self.tblXFx.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"F(x)", None));
        ___qtablewidgetitem3 = self.tblXFx.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"V", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"F(b) =", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Regla", None))
        self.txtH.setText("")
        self.txtH.setPlaceholderText("")
        self.cbxTipoRegla.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione opci\u00f3n", None))
        self.cbxTipoRegla.setItemText(1, QCoreApplication.translate("MainWindow", u"Trapecio Simple", None))
        self.cbxTipoRegla.setItemText(2, QCoreApplication.translate("MainWindow", u"Trapecio M\u00faltiple", None))
        self.cbxTipoRegla.setItemText(3, QCoreApplication.translate("MainWindow", u"Simpson 1/3", None))
        self.cbxTipoRegla.setItemText(4, QCoreApplication.translate("MainWindow", u"Simpson 1/3 m\u00faltiple", None))
        self.cbxTipoRegla.setItemText(5, QCoreApplication.translate("MainWindow", u"Simpson 3/8", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.btnCalcularMet.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

