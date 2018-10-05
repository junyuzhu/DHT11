#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 13:25
# @Author  : Aries
# @Site    : 
# @File    : moving.py
# @Software: PyCharm

"""
想要实现的功能如下：
1、能自动创建日期的文件夹
2、将文件复制到存档文件夹后删除原来的两个记录文件
"""
import time
import os
import shutil



theDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(theDate)
os.mkdir(theDate)

#fileName = 'hud_data.txt, tmp_data.txt'

#copy files
shutil.copy('/home/pi/DHT11/hud_data.txt', '/home/pi/DHT11/'+theDate+'/hud_data.txt')
shutil.copy('/home/pi/DHT11/tmp_data.txt', '/home/pi/DHT11/'+theDate+'/tmp_data.txt')

#delete files
os.unlink('/home/pi/DHT11/hud_data.txt')
os.unlink('/home/pi/DHT11/tmp_data.txt')



