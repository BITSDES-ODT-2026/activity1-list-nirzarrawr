from machine import Pin
import time

val = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

red1 = Pin(12,Pin.OUT)
red2 = Pin(26,Pin.OUT)
green1 = Pin(18,Pin.OUT)
green2 = Pin(5,Pin.OUT)

for i in val:
    red1.value(i[0])
    red2.value(i[1])
    green1.value(i[2])
    green2.value(i[3])
    time.sleep(1)
