import configparser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator

import configui1 as u1
import multiwin as u3
import os

class SettingWindow(QMainWindow):
    def __init__(self, parent = None):
        super(SettingWindow, self).__init__(parent)
        self.ui = u3.Ui_settingForm()
        self.ui.setupUi(self)

        portValidator = QIntValidator(0, 99)
        self.ui.lineEdit_10.setValidator(portValidator)
        self.ui.lineEdit_11.setValidator(portValidator)

    def show(self):
        print("show")
        self.setVisible(True)
        try:
            self.read_config()
            print("read config oK")
        except:
            self.saveSetting()


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

                print(self.cfg_alarm_dic)
                # print(self.cfg_address_dic)
                print(self.cfg_alarm_dic["11"])

                self.ui.lineEdit_10.setText(self.cfg_alarm_dic["10"])
                self.ui.lineEdit_11.setText(self.cfg_alarm_dic["11"])



                self.ui.lineEdit_A10.setText(self.cfg_address_dic["a10"])
                self.ui.lineEdit_A11.setText(self.cfg_address_dic["a11"])



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

    # def save_setting(self):

    def closeEvent(self, event):
        win.show()

    def settingselect1(self):
        print("setting  select 1")
        # self.saveSetting()
        self.ui.stackedWidget.setCurrentIndex(0)

    def settingselect2(self):
        print("setting  select 2")
        self.ui.stackedWidget.setCurrentIndex(1)

    def saveSetting(self):
        print("setting window 3  ")
        """
        保存配置
        :return:
        """

        self.confParse.set('alarm_setting', '10', self.ui.lineEdit_10.text())
        self.confParse.set('alarm_setting', '11', self.ui.lineEdit_11.text())

        print(self.ui.lineEdit_11.text())


        self.confParse.set('alarm_setting', '12', "41")
        self.confParse.set('alarm_setting', '13', "45")
        self.confParse.set('alarm_setting', '14', "46")
        self.confParse.set('alarm_setting', '15', "47")
        self.confParse.set('alarm_setting', '16', "48")
        self.confParse.set('alarm_setting', '17', "49")
        self.confParse.set('alarm_setting', '18', "50")
        self.confParse.set('alarm_setting', '19', "51")
        self.confParse.set('alarm_setting', '20', "39")
        self.confParse.set('alarm_setting', '21', "40")
        self.confParse.set('alarm_setting', '22', "41")
        self.confParse.set('alarm_setting', '23', "45")
        self.confParse.set('alarm_setting', '24', "46")
        self.confParse.set('alarm_setting', '25', "47")
        self.confParse.set('alarm_setting', '26', "48")
        self.confParse.set('alarm_setting', '27', "49")
        self.confParse.set('alarm_setting', '28', "50")
        self.confParse.set('alarm_setting', '29', "51")
        self.confParse.set('alarm_setting', '30', "39")
        self.confParse.set('alarm_setting', '31', "40")
        self.confParse.set('alarm_setting', '32', "41")
        self.confParse.set('alarm_setting', '33', "45")
        self.confParse.set('alarm_setting', '34', "46")
        self.confParse.set('alarm_setting', '35', "47")
        self.confParse.set('alarm_setting', '36', "48")
        self.confParse.set('alarm_setting', '37', "49")
        self.confParse.set('alarm_setting', '38', "50")
        self.confParse.set('alarm_setting', '39', "51")
        self.confParse.set('alarm_setting', '40', "42")
        self.confParse.set('alarm_setting', '41', "43")
        self.confParse.set('alarm_setting', '42', "44")
        self.confParse.set('alarm_setting', '43', "45")
        self.confParse.set('alarm_setting', '44', "46")
        self.confParse.set('alarm_setting', '45', "47")
        self.confParse.set('alarm_setting', '46', "48")
        self.confParse.set('alarm_setting', '47', "49")
        self.confParse.set('alarm_setting', '48', "50")
        self.confParse.set('alarm_setting', '49', "51")
        self.confParse.set('alarm_setting', '50', "49")
        self.confParse.set('alarm_setting', '51', "50")
        self.confParse.set('alarm_setting', '52', "45")
        self.confParse.set('alarm_setting', '53', "46")
        self.confParse.set('alarm_setting', '54', "49")
        self.confParse.set('alarm_setting', '55', "50")
        self.confParse.set('alarm_setting', '56', "45")
        self.confParse.set('alarm_setting', '57', "46")
        self.confParse.set('alarm_setting', '58', "49")
        self.confParse.set('alarm_setting', '59', "50")
        self.confParse.set('alarm_setting', '60', "45")
        self.confParse.set('alarm_setting', '61', "46")
        self.confParse.set('alarm_setting', '62', "45")
        self.confParse.set('alarm_setting', '63', "46")
        self.confParse.set('alarm_setting', '64', "49")
        self.confParse.set('alarm_setting', '65', "50")
        self.confParse.set('alarm_setting', '66', "45")
        self.confParse.set('alarm_setting', '67', "46")
        self.confParse.set('alarm_setting', '68', "49")
        self.confParse.set('alarm_setting', '69', "50")

        self.confParse.set('address_setting', 'a10', self.ui.lineEdit_A10.text())
        self.confParse.set('address_setting', 'a11', self.ui.lineEdit_A11.text())
        self.confParse.set('address_setting', 'a12', "终端1的3号机架温度")

        self.confParse.write(open(self.cfg_path, 'w'))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = u1.Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        print("close main window")
        # win2.close()
        win3.close()

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
# pyinstaller --console --onefile monitor2.py
# pyinstaller -F -w --onefile monitor2.py
# pyinstaller -F -w --onefile monitor1.py

# pyinstaller -F  --onefile  --hidden-import="serial" monitor1.py

