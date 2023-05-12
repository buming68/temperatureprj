# -*- coding: utf-8 -*-

#  def IsSubString(SubStrList,Str)
#  def GetFileList(FindPath,FlagStr=[]):
#  功能:读取指定目录下特定类型的文件名列表
#  Data: 2013-08-08,星期四
# from PIL import Image
# import piexif
from binascii import unhexlify
from crcmod import mkCrcFun
import serial

#提取字符串的的场强和数据，转换成整型数字列表
def FS_Get(stringSource1, stringSource2):
    number = [0]*6
    string_list = stringSource1.split()                     #以空格符号分割字符串
    number[0] = int(string_list[2])                         #信号1  场强
    number[1] = int(string_list[3])                         #信噪比
    number[2] = int(string_list[5])                         #锁定状态
    string_list = stringSource2.split()
    number[3] = int(string_list[2])
    number[4] = int(string_list[3])
    number[5] = int(string_list[5])
    return  number

#将6个场强数据，转换成发送给DTU的字符串命令
def Str_Get(fs_d):
    global s1
    s1 = ""                                                 #用于MODBUS CRC运算用的字符串
    data = [0] * 6                                          #定义8位数字列表
    data[0] = 0x01
    data[1] = 0x03
    data[2] = 0x00
    data[3] = 0x00
    data[4] = 0x00
    data[5] = 0x0A
    # data[10] = fs_d[3]
    # data[12] = fs_d[4]
    # data[14] = fs_d[5]

    for d1 in data:                                         #将整数转换成2位的16进制数，拼接成字符串
        if d1 > 100:                                        #限制最大数字是100
            d1 = 100
        if d1 >= 16:                                        #去除
            s2 = str(hex(d1)).upper()
            s2 = s2[: 0] + "" + s2[2:]
            # print(s2)
            s1 = s1 + s2
        if d1 < 16:
            s2 = str(hex(d1)).upper()
            s2 = s2[: 0] + "0" + s2[2:]
            # print(s2)
            s1 = s1 + s2
    s3 = crc16_modbus(s1)                                   #计算MODBUS 16 CRC校验
    s1 = s1 + s3                                            #合成8位长的含CRC的命令字符串
    return s1

#将6个场强数据，转换成发送给DTU的字符串命令
def Str_lunxun(address, ch_number):
    global s1
    s1 = ""                                                 #用于MODBUS CRC运算用的字符串
    data = [0] * 6                                          #定义8位数字列表
    data[0] = address
    data[1] = 0x03
    data[2] = 0x00
    data[3] = 0x00
    data[4] = 0x00
    data[5] = ch_number

    for d1 in data:                                         #将整数转换成2位的16进制数，拼接成字符串
        if d1 > 100:                                        #限制最大数字是100
            d1 = 100
        if d1 >= 16:                                        #去除
            s2 = str(hex(d1)).upper()
            s2 = s2[: 0] + "" + s2[2:]
            # print(s2)
            s1 = s1 + s2
        if d1 < 16:
            s2 = str(hex(d1)).upper()
            s2 = s2[: 0] + "0" + s2[2:]
            # print(s2)
            s1 = s1 + s2
    s3 = crc16_modbus(s1)                                   #计算MODBUS 16 CRC校验
    s1 = s1 + s3                                            #合成8位长的含CRC的命令字符串
    return s1


# CRC16/MODBUS
def crc16_modbus(s):
    crc16 = mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    return get_crc_value(s, crc16)

def get_crc_value(s, crc16):
    data = s.replace(' ', '')
    crc_out = hex(crc16(unhexlify(data))).upper()
    str_list = list(crc_out)
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0
    crc_data = ''.join(str_list[2:])
    return crc_data[2:]+crc_data[:2]

#字符串转换成16进制数
def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])

def GetComPortName():  # 获取计算机所有串口的名字列表
    port_list = list(serial.tools.list_ports.comports())
    port_list_name = []
    if len(port_list) <= 0:
        port_list_name.append("未发现串口，请检查")
        # print("The Serial port can't find!")
    else:
        for each_port in port_list:
            port_list_name.append(each_port[0])
    return port_list_name



