#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27  2017

@author: Somchai Somphadung
"""

from bluepy import btle
import Microbit as Ubit 

from Services import BTService, UBitBtnService,AccelService
from Actors import GPIODriver, DriveJob,SteeringJob

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        
    def handleNotification(self,cHandle, data):
        global stop_flag,a_btn_serv,b_btn_serv,motor,accel_serv,a_pressed,b_pressed,pi,steer
        x = 0
        pi.gpio_driver.write(6,1)
        if cHandle == a_btn_serv.cHandle :
            a_pressed = a_btn_serv.get_data(data)
        if cHandle == b_btn_serv.cHandle :
            b_pressed = b_btn_serv.get_data(data)        
        if cHandle == accel_serv.cHandle :
            x,_,_ = accel_serv.get_data(data)
            steer.steer(x,pi.gpio_driver)
            
            
        #print(a_pressed,b_pressed) 
        
        if (a_pressed,b_pressed) == (True,False) :
            if motor.direction != 1 :
                motor.park(pi.gpio_driver)
                motor.forward(pi.gpio_driver)
            
        elif (a_pressed,b_pressed) == (False,True) :    
            if motor.direction != 2 :
                motor.park(pi.gpio_driver)
                motor.backward(pi.gpio_driver)
            
        elif (a_pressed,b_pressed) == (True,True) :
            stop_flag = True
            
            
        if (a_pressed,b_pressed) in [(True,False),(False,True)] :
            if motor.min_pwm <= motor.pwm < motor.max_pwm :
                motor.pwm += 1
            motor.accelerate(pi.gpio_driver) 
            #print(motor.pwm)
        if (a_pressed,b_pressed) == (False,False) :
            if motor.min_pwm < motor.pwm <= motor.max_pwm :
                motor.pwm -= 1
            #print(motor.pwm)
            motor.accelerate(pi.gpio_driver)
        pi.gpio_driver.write(6,0)

pi = GPIODriver()
a_pressed = b_pressed = False
stop_flag = False

ble_serv = BTService(peripheral_addr=Ubit.pizez)
motor = DriveJob()
steer = SteeringJob()

a_btn_serv = UBitBtnService(Ubit.BTN_SRV,Ubit.BTN_A_STATE,Ubit.CCCD_UUID,ble_serv.device,27)
b_btn_serv = UBitBtnService(Ubit.BTN_SRV,Ubit.BTN_B_STATE,Ubit.CCCD_UUID,ble_serv.device,30)
accel_serv = AccelService(Ubit.ACCEL_SRV,Ubit.ACCEL_DATA,Ubit.CCCD_UUID,ble_serv.device,21)
ble_serv.set_delegate(MyDelegate())

a_btn_serv.start_notify(Ubit.START_NOTIFY_CODE)
b_btn_serv.start_notify(Ubit.START_NOTIFY_CODE)
accel_serv.start_notify(Ubit.START_NOTIFY_CODE)
motor._on(pi.gpio_driver)

while not stop_flag :
    if ble_serv.notify(0.5) : continue

motor.park(pi.gpio_driver)
motor.reset()    
a_btn_serv.stop_notify(Ubit.STOP_NOTIFY_CODE)
b_btn_serv.stop_notify(Ubit.STOP_NOTIFY_CODE)
accel_serv.stop_notify(Ubit.STOP_NOTIFY_CODE)
    
motor._off(pi.gpio_driver)
ble_serv.disconnect()
pi.stop()





