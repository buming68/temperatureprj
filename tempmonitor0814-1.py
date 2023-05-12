#coding:utf-8
import tkinter as tk
from tkinter import *
from tkinter import ttk # 导入ttk模块，因为下拉菜单控件在ttk中
import serial
import serial.tools.list_ports
import time
from functions import *

Flag_COM = 0                               #全局变量，串口COM打开标志，1=打开，0=未打开
def comgo(*args):                          #下拉列表选择后处理程序，*args表示可变参数
    global t, Flag_COM                     #t serail通讯口对象，因要在主程序中使用，全局变量
    COMPORT = cmb.get()
    # print(COMPORT)  # 打印选中的值
    try:
        t = serial.Serial(COMPORT,9600,timeout=0.5)          #发送给DTU的通讯口，0.5秒超时
        Flag_COM = 1
        print((COMPORT + "  已经打开"))
    except Exception:
        print(COMPORT+"   COM通讯口无法打开,无法发送数据")   #自定义异常提示
        Flag_COM = 0

if __name__ == "__main__":
    top = tk.Tk()                                                               #tkinter 主窗口
    top.wm_title("微波接收机实时监测塔石物联网终端软件V1.0                         by zjjohn WXBTV")
    top.geometry('640x400')
    # 第一接收频率3个标签信息 1-场强  2-信噪比 3-频率锁定指示
    var1_1 = tk.StringVar()
    Label(top, justify="left", textvariable=var1_1, anchor='nw',font=("黑体", 14), fg="green", width=30, height=2)\
           .place(x=20, y=150)
    var1_2 = tk.StringVar()
    Label(top, justify="left", textvariable=var1_2, anchor='nw', font=("黑体", 14), fg="green", width=30, height=2)\
           .place(x=20, y=200)
    var1_3 = tk.StringVar()
    Label(top, justify="left", textvariable=var1_3,  anchor='nw',font=("黑体", 14), fg="red", width=26, height=2)\
           .place(x=20, y=100)
    # 第二接收频率3个标签信息
    var2_1 = tk.StringVar()
    Label(top, justify="left", textvariable=var2_1, anchor='nw',font=("黑体", 14), fg="green", width=30, height=2)\
           .place(x=320, y=150)
    var2_2 = tk.StringVar()
    Label(top, justify="left", textvariable=var2_2, anchor='nw', font=("黑体", 14), fg="green", width=30, height=2)\
           .place(x=320, y=200)
    var2_3 = tk.StringVar()
    Label(top,justify="left", textvariable=var2_3, anchor='nw', font=("黑体", 14), fg="red", width=26, height=2)\
           .place(x=320, y=100)

    var3 = tk.StringVar()                               #串口连接状态指示
    Label(top,justify="left", textvariable=var3, anchor='nw', font=("黑体", 14), fg="green", width=22, height=2)\
           .place(x=320, y=20)

    count = 0                                           #在与接收机UDP通讯的计数
    var1_3.set('温度')
    var2_3.set('湿度')
    var1_1.set('温度')
    var2_1.set('温度')
    var1_2.set('温度')
    var2_2.set('温度')
    def refreshText():                                  #每0.6秒定时执行，获取接收机场强，根据塔石云的轮询，发送信息

        portname = GetComPortName()  # 下拉框获取选择通讯串口名称
        cmb['value'] = portname
        if Flag_COM == 1:                                   #串口打开成功标志
            var3.set("串口连接成功")
            time.sleep(0.2)                                 # sleep() 与 inWaiting() 最好配对使用
            try:
                num = t.inWaiting()                         #等待接收串口缓冲区中的数据
            except Exception:
                num = 0
                var3.set("串口通讯异常")
            if num:                                         #接收到数据，数量
                recedata = t.read(num)                      # 清除接收数据，无需判断接收数据
                # print(recedata)

                text_list = re.findall(".{2}", recedata.hex())  #收到的温度数据
                new_text = " ".join(text_list)
                print('收到监测终端的数据： '+new_text)
                                                                #转换成16进制字符
                strTemp1 = '温度1: '+str((int(text_list[3], 16) * 256 + int(text_list[4], 16))/10)+'度'
                strTemp10 = '湿度: ' + str((int(text_list[21], 16) * 256 + int(text_list[22], 16)) / 10) + '%'

                var1_3.set(strTemp1)
                var2_3.set(strTemp10)
                var1_1.set(strTemp1)
                var2_1.set(strTemp10)
                var1_2.set(strTemp1)
                var2_2.set(strTemp10)
        else:
            var3.set("串口连接失败")

        # 定时发送命令（900ms）
        if Flag_COM == 1:
            fs_d = [5, 1, 0]                            # 获取3个参数（波特率、地址、回传间隔）
            command_tashi = Str_Get(fs_d)               # 转换成塔石1104命令
            t.write(bytes.fromhex(command_tashi))       # 发送数据1104
            print("发往监测终端命令：" + command_tashi)
            var3.set("发往监测终端正常")

        top.after(600, refreshText)

    # 创建下拉菜单,com串口
    cmb = ttk.Combobox(values=GetComPortName(), state='readonly')
    cmb.grid(padx=30, pady=20)
    cmb.bind("<<ComboboxSelected>>", comgo)                 # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    # 设置默认值，即默认下拉框中的内容
    cmb.current(0)

    top.after(900, refreshText)                             #定时执行程序，refreshText
    top.mainloop()                                          #主窗口循环


#pip install pyinstaller
#pyinstaller --console --onefile wbjc20220405.py
#pyinstaller -F -w --onefile wbjc20220411.py

