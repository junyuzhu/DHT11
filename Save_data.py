#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


def get_data():
    """获取DHT11传感器的数据"""
    channel = 4
    data = []
    j = 0
    GPIO.setmode(GPIO.BCM)
    time.sleep(1)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        continue
    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            continue
        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1
    # print("sensor is working.")
    # print(data)
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0
    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7-i)
        humidity_point += humidity_point_bit[i] * 2 ** (7-i)
        temperature += temperature_bit[i] * 2 ** (7-i)
        temperature_point += temperature_point_bit[i] * 2 ** (7-i)
        check += check_bit[i] * 2 ** (7-i)
    tmp = humidity + humidity_point + temperature + temperature_point
    # print(check)
    # print(tmp)
    """调用比较函数,传递check, tmp, temperature, humidity的值"""
    operation(check, tmp, temperature, humidity)


def operation(check1, tmp1, temperature1, humidity1):
    """如果check == tmp 表示数据正确,如果!=则重新运行get_data()函数进行获取数据"""
    if check1 == tmp1:
        """调用data_input函数经行写入数据"""
        data_input(temperature1, humidity1)
        # print("Temperature is %d,humidity is %d." % (temperature1, humidity1))
    else:
        # print("wrong")
        GPIO.cleanup()
        time.sleep(1)
        get_data()


def data_input(temp, hum):
    temp = str(temp)
    hum = str(hum)
    with open('/home/pi/DHT11/tmp_data.txt', 'a') as tmp_output:
        tmp_output.write(
            temp + 'C' + ' in ' + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + '\r\n')

    with open('/home/pi/DHT11/hud_data.txt', 'a') as hud_output:
        hud_output.write(
            hum + '%' + ' in ' + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + '\r\n')


if __name__ == '__main__':
    # 程序开始,调用获取数据函数
    get_data()
