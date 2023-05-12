import configparser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator, QPalette, QPixmap, QBrush
import configui1 as u1
import multiwin as u3
import os
# from PyQt5.Qt import *

class SettingWindow(QMainWindow):
    def __init__(self, parent = None):
        super(SettingWindow, self).__init__(parent)
        self.ui = u3.Ui_settingForm()
        self.ui.setupUi(self)

        portValidator = QIntValidator(0, 99)
        # self.ui.lineEdit_10.setValidator(portValidator)       #设置输入限制，整数0--99
        for index in range(10,70):
            str1 = "self.ui.lineEdit_" + str(index) + ".setValidator(portValidator)"
            # print(str1)
            eval(str1)


    def show(self):
        # print("show")
        self.setVisible(True)
        try:
            self.read_config()
            print("settting window visable")
        except:
            self.saveSetting()
            print("can not read config,    saveSetting, ")


    def read_config(self):
        """
        读取串口配置
        :return:
        """
        self.cfg_path = ''  # 配置文件的路径
        self.cfg_dir = 'settings'  # 配置文件目录
        self.conf_file_name = "cfg.ini"  # 配置文件名
        self.confParse = configparser.ConfigParser()  # 配置文件解析ConfigParser对象
        self.cfg_path = os.path.join( self.cfg_dir, self.conf_file_name)  # 获取配置文件路径
        # 判断读取配置文件是否正常
        if self.confParse.read(self.cfg_path, encoding='gbk'):
            # 判断读取section是否正常
            try:
                items3 = self.confParse.items('alarm_setting')  # 获取 terminal_setting section，返回字典
                self.cfg_alarm_dic = dict(items3)
                items4 = self.confParse.items('address_setting')  # 获取 terminal_setting section，返回字典
                self.cfg_address_dic = dict(items4)
                # print(self.cfg_alarm_dic)
                # print(self.cfg_address_dic)

                for index in range(10, 70):
                    str1 = "self.ui.lineEdit_" + str(index) + ".setText(self.cfg_alarm_dic[\'" + str(index) + "\'])"
                    # print(str1)
                    eval(str1)
                    str1 = "self.ui.lineEdit_A" + str(index) + ".setText(self.cfg_address_dic[\'a" + str(index) + "\'])"
                    # print(str1)
                    eval(str1)

                # self.ui.lineEdit_10.setText(self.cfg_alarm_dic["10"])
                # self.ui.lineEdit_A10.setText(self.cfg_address_dic["a10"])

            # 未找到section
            except configparser.NoSectionError:
                self.confParse.add_section('alarm_setting')  # 添加section3
                self.confParse.add_section('address_setting')  # 添加section4
                self.confParse.write(open(self.cfg_path, 'w'))  # 保存到配置文件

        # 异常
        else:
            # 判断目录是否存在,不存在的话新建目录
            if not os.path.exists(self.cfg_dir):
                os.mkdir(self.cfg_dir)
                print("directory not exsist!")

            self.confParse.add_section('serial_setting')  # 添加section
            self.confParse.add_section('terminal_setting')  # 添加section2
            self.confParse.add_section('alarm_setting')  # 添加section3
            self.confParse.add_section('address_setting')  # 添加section4
            self.confParse.write(open(self.cfg_path, 'w'))  # 保存到配置文件


    def closeEvent(self, event):
        win.show()


    def settingselect1(self):
        print("setting  select 1")
        # self.saveSetting()
        self.ui.stackedWidget.setCurrentIndex(0)

    def settingselect2(self):
        print("setting  select 2")
        self.ui.stackedWidget.setCurrentIndex(1)

    def settingselect3(self):
        print("setting  select 3")
        self.ui.stackedWidget.setCurrentIndex(2)

    def saveSetting(self):
        print("setting window 3  ")
        """
        保存配置
        :return:
        """
        question = QMessageBox.question(self,
                                        '确认',
                                        '是否保存修改的设置',
                                        )
        if question == QMessageBox.Yes:
            print("您选择了Yes保存设置")
            for index in range(10, 70):
                str1 = "self.confParse.set('alarm_setting', \'" + str(index) + "\', self.ui.lineEdit_" + str(
                    index) + ".text())"
                # print(str1)
                eval(str1)
                str1 = "self.confParse.set('address_setting', \'a" + str(index) + "\', self.ui.lineEdit_A" + str(
                    index) + ".text())"
                # print(str1)
                eval(str1)
            # self.confParse.set('alarm_setting', '10', self.ui.lineEdit_10.text())
            # self.confParse.set('address_setting', 'a10', self.ui.lineEdit_A10.text())
            self.confParse.write(open(self.cfg_path, 'w'))

        else:
            print("您选择了No，修改的设置未保存")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = u1.Ui_MainWindow()
        self.ui.setupUi(self)

        if os.path.exists("./mypic20.jpg"):
            # print("mypic20.jpg  picture founded!")
            palette = QPalette()
            pix = QPixmap("./mypic20.jpg")
            pix = pix.scaled(self.width(),self.height())
            palette.setBrush(QPalette.Background, QBrush(pix))
            self.setPalette(palette)
        else:
            print("mypic20.jpg  picture not exsisted!")

    def closeEvent(self, event):
        print("close main window")
        win3.close()
        self.ui.stop_send()
        self.close()

    def slot1(self):
        self.hide()
        self.ui.stop_send()
        win3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win3 = SettingWindow()
    sys.exit(app.exec_())


# pip install pyinstaller
# pyinstaller -F -w --onefile monitor1.py
# pyinstaller --console --onefile monitor2.py
# pyinstaller -F -w --onefile monitor2.py
# pyinstaller -F  --onefile monitor1.py

# pyinstaller -F  --onefile  --hidden-import="serial" monitor1.py

