import sys
from PyQt5 import QtWidgets
from Receive import Ui_Form
from PyQt5.QtCore import QTimer
import serial
import serial.tools.list_ports


def open_port(port, bps, timeout):  # 打开串口
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(port, bps, timeout=timeout)
        # 判断是否打开成功
        if ser.is_open:
            ret = True
            print(port + "打开了")
            # threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        print("---异常---：", e)
    return ret, ser


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.sendPort = None  # 发送串口
        self.sendCondition = False  # 发送串口状态
        self.receivePort = None  # 接收串口
        self.receiveCondition = False  # 接收串口状态
        self.setupUi(self)
        self.init()
        self.timer = QTimer(self)  # 初始化一个定时器

        self.setWindowTitle("Data_monitoring_System")

    def generate(self):
        head = '0xA1'
        direction = "0x01"
        distance = "0x10"
        tail = "0xEE"
        l = str(head) + str(direction) + str(distance) + str(tail)
        self.sendData.append(l)

    def init(self):  # 把按钮等控件和函数对应起来
        self.startGenerate.clicked.connect(self.generate_start)  # 开始自动生成数据
        self.stopGenerate.clicked.connect(self.generate_close)  # 停止自动生成数据

        self.openSend.clicked.connect(self.open_send_port)  # 打开发送端口
        self.closeSend.clicked.connect(self.close_send_port)  # 关闭发送端口

        self.openReceive.clicked.connect(self.open_receive_port)  # 打开接收端口
        self.closeReceive.clicked.connect(self.close_receive_port)  # 关闭接收端口

        self.startSend.clicked.connect(self.start_send)  # 开始发送
        self.clearSend.clicked.connect(self.clear_send)  # 清空发送数据界面

        self.startReceive.clicked.connect(self.start_receive)  # 开始接收
        self.clearReceive.clicked.connect(self.clear_receive)  # 清空接收数据界面

    def generate_start(self):
        self.timer.start(1000)  # 设置计时间隔并启动
        self.timer.timeout.connect(self.generate)

    def generate_close(self):
        self.timer.stop()

    def open_send_port(self):  # 打开发送数据接口
        port = self.sendName.currentText()  # 发送接口的名字
        bps = self.sendBit.currentText()  # 发送接口的波特率
        timeout = None  # 发送接口的连接时间
        self.sendCondition, self.sendPort = open_port(port, bps, timeout)

    def open_receive_port(self):  # 关闭发送接口
        port = self.receiveName.currentText()  # 接收接口的名字
        bps = self.receiveBit.currentText()  # 接受接口的波特率
        timeout = None  # 接收接口的连接时间
        self.receiveCondition, self.receivePort = open_port(port, bps, timeout)

    def close_send_port(self):
        try:
            # 判断是否打开成功
            if self.sendPort.is_open:
                self.sendPort.close()
                self.sendCondition = False  # 更新串口状态
        except Exception as e:
            print("---异常---：", e)

    def close_receive_port(self):  # 关闭数据接收端口
        try:
            # 判断是否打开成功
            if self.receivePort.is_open:
                self.receivePort.close()  # 关闭数据接收端口
                self.receiveCondition = False  # 更新接收端口状态
        except Exception as e:
            print("---异常---：", e)

    def start_send(self):  # 开始发送
        text = self.sendData.toPlainText()  # 得到发送数据界面的当前发送数据
        if self.sendCondition:  # 如果发送数据端口打开
            self.sendPort.write(text.encode("gbk"))  # 写数据

    def clear_send(self):
        self.sendData.clear()

    def start_receive(self):
        if self.receiveCondition:
            text = self.receivePort.read(self.receivePort.in_waiting).decode("gbk")  # 从串口中读入数据
            self.receiveData.append(text)

    def clear_receive(self):
        self.receiveData.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 实例化一个应用对象
    myshow = Pyqt5_Serial()
    myshow.show()  # 让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    sys.exit(app.exec_())  # 程序一直循环运行到主窗口被关闭

