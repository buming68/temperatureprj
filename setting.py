# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingForm(object):
    def setupUi(self, settingForm):
        settingForm.setObjectName("settingForm")
        settingForm.resize(1024, 768)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        settingForm.setPalette(palette)
        settingForm.setToolTip("")
        self.stackedWidget = QtWidgets.QStackedWidget(settingForm)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 60, 991, 701))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.page_1.setPalette(palette)
        self.page_1.setObjectName("page_1")
        self.label_page1 = QtWidgets.QLabel(self.page_1)
        self.label_page1.setGeometry(QtCore.QRect(380, 20, 81, 31))
        self.label_page1.setObjectName("label_page1")
        self.lineEdit_A11 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A11.setGeometry(QtCore.QRect(290, 100, 181, 21))
        self.lineEdit_A11.setText("")
        self.lineEdit_A11.setObjectName("lineEdit_A11")
        self.label_01 = QtWidgets.QLabel(self.page_1)
        self.label_01.setGeometry(QtCore.QRect(60, 70, 101, 16))
        self.label_01.setObjectName("label_01")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_11.setGeometry(QtCore.QRect(400, 70, 71, 21))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 70, 71, 21))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_A10 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A10.setGeometry(QtCore.QRect(60, 100, 181, 21))
        self.lineEdit_A10.setText("")
        self.lineEdit_A10.setObjectName("lineEdit_A10")
        self.label_02 = QtWidgets.QLabel(self.page_1)
        self.label_02.setGeometry(QtCore.QRect(290, 70, 101, 16))
        self.label_02.setObjectName("label_02")
        self.lineEdit_A12 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A12.setGeometry(QtCore.QRect(530, 100, 181, 21))
        self.lineEdit_A12.setText("")
        self.lineEdit_A12.setObjectName("lineEdit_A12")
        self.lineEdit_A13 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A13.setGeometry(QtCore.QRect(750, 100, 181, 21))
        self.lineEdit_A13.setText("")
        self.lineEdit_A13.setObjectName("lineEdit_A13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_12.setGeometry(QtCore.QRect(640, 70, 71, 21))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_03 = QtWidgets.QLabel(self.page_1)
        self.label_03.setGeometry(QtCore.QRect(530, 70, 101, 16))
        self.label_03.setObjectName("label_03")
        self.label_04 = QtWidgets.QLabel(self.page_1)
        self.label_04.setGeometry(QtCore.QRect(750, 70, 101, 16))
        self.label_04.setObjectName("label_04")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_13.setGeometry(QtCore.QRect(860, 70, 71, 21))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_05 = QtWidgets.QLabel(self.page_1)
        self.label_05.setGeometry(QtCore.QRect(60, 160, 101, 16))
        self.label_05.setObjectName("label_05")
        self.lineEdit_A17 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A17.setGeometry(QtCore.QRect(750, 190, 181, 21))
        self.lineEdit_A17.setText("")
        self.lineEdit_A17.setObjectName("lineEdit_A17")
        self.lineEdit_A15 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A15.setGeometry(QtCore.QRect(290, 190, 181, 21))
        self.lineEdit_A15.setText("")
        self.lineEdit_A15.setObjectName("lineEdit_A15")
        self.lineEdit_A14 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A14.setGeometry(QtCore.QRect(60, 190, 181, 21))
        self.lineEdit_A14.setText("")
        self.lineEdit_A14.setObjectName("lineEdit_A14")
        self.label_08 = QtWidgets.QLabel(self.page_1)
        self.label_08.setGeometry(QtCore.QRect(750, 160, 101, 16))
        self.label_08.setObjectName("label_08")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_15.setGeometry(QtCore.QRect(400, 160, 71, 21))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_06 = QtWidgets.QLabel(self.page_1)
        self.label_06.setGeometry(QtCore.QRect(290, 160, 101, 16))
        self.label_06.setObjectName("label_06")
        self.lineEdit_A16 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A16.setGeometry(QtCore.QRect(530, 190, 181, 21))
        self.lineEdit_A16.setText("")
        self.lineEdit_A16.setObjectName("lineEdit_A16")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_16.setGeometry(QtCore.QRect(640, 160, 71, 21))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_07 = QtWidgets.QLabel(self.page_1)
        self.label_07.setGeometry(QtCore.QRect(530, 160, 101, 16))
        self.label_07.setObjectName("label_07")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_14.setGeometry(QtCore.QRect(170, 160, 71, 21))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_09 = QtWidgets.QLabel(self.page_1)
        self.label_09.setGeometry(QtCore.QRect(60, 250, 101, 16))
        self.label_09.setObjectName("label_09")
        self.lineEdit_A19 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A19.setGeometry(QtCore.QRect(290, 280, 181, 21))
        self.lineEdit_A19.setText("")
        self.lineEdit_A19.setObjectName("lineEdit_A19")
        self.lineEdit_A18 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_A18.setGeometry(QtCore.QRect(60, 280, 181, 21))
        self.lineEdit_A18.setText("")
        self.lineEdit_A18.setObjectName("lineEdit_A18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_19.setGeometry(QtCore.QRect(400, 250, 71, 21))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_010 = QtWidgets.QLabel(self.page_1)
        self.label_010.setGeometry(QtCore.QRect(290, 250, 101, 16))
        self.label_010.setObjectName("label_010")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_18.setGeometry(QtCore.QRect(170, 250, 71, 21))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_17.setGeometry(QtCore.QRect(860, 160, 71, 21))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_page2 = QtWidgets.QLabel(self.page_2)
        self.label_page2.setGeometry(QtCore.QRect(380, 20, 81, 31))
        self.label_page2.setObjectName("label_page2")
        self.stackedWidget.addWidget(self.page_2)
        self.saveButton = QtWidgets.QPushButton(settingForm)
        self.saveButton.setGeometry(QtCore.QRect(754, 20, 151, 28))
        self.saveButton.setObjectName("saveButton")
        self.layoutWidget = QtWidgets.QWidget(settingForm)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 20, 301, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settionButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.settionButton_1.setObjectName("settionButton_1")
        self.horizontalLayout.addWidget(self.settionButton_1)
        self.settionButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.settionButton_2.setObjectName("settionButton_2")
        self.horizontalLayout.addWidget(self.settionButton_2)

        self.retranslateUi(settingForm)
        self.stackedWidget.setCurrentIndex(0)
        self.settionButton_1.clicked.connect(settingForm.settingselect1)
        self.settionButton_2.clicked.connect(settingForm.settingselect2)
        self.saveButton.clicked.connect(settingForm.saveSetting)
        QtCore.QMetaObject.connectSlotsByName(settingForm)

    def retranslateUi(self, settingForm):
        _translate = QtCore.QCoreApplication.translate
        settingForm.setWindowTitle(_translate("settingForm", "Form"))
        self.label_page1.setText(_translate("settingForm", "第一页参数"))
        self.lineEdit_A11.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.label_01.setText(_translate("settingForm", "传感器01"))
        self.lineEdit_11.setPlaceholderText(_translate("settingForm", "0-99"))
        self.lineEdit_10.setPlaceholderText(_translate("settingForm", "0-99"))
        self.lineEdit_A10.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.label_02.setText(_translate("settingForm", "传感器02"))
        self.lineEdit_A12.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_A13.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_12.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_03.setText(_translate("settingForm", "传感器03"))
        self.label_04.setText(_translate("settingForm", "传感器04"))
        self.lineEdit_13.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_05.setText(_translate("settingForm", "传感器05"))
        self.lineEdit_A17.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_A15.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_A14.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.label_08.setText(_translate("settingForm", "传感器08"))
        self.lineEdit_15.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_06.setText(_translate("settingForm", "传感器06"))
        self.lineEdit_A16.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_16.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_07.setText(_translate("settingForm", "传感器07"))
        self.lineEdit_14.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_09.setText(_translate("settingForm", "传感器09"))
        self.lineEdit_A19.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_A18.setPlaceholderText(_translate("settingForm", "传感器名称和位置"))
        self.lineEdit_19.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_010.setText(_translate("settingForm", "传感器10"))
        self.lineEdit_18.setPlaceholderText(_translate("settingForm", "0-99"))
        self.lineEdit_17.setPlaceholderText(_translate("settingForm", "0-99"))
        self.label_page2.setText(_translate("settingForm", "第二页参数"))
        self.saveButton.setText(_translate("settingForm", "保 存"))
        self.settionButton_1.setText(_translate("settingForm", "设置第一页"))
        self.settionButton_2.setText(_translate("settingForm", "设置第二页"))


