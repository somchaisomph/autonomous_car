#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:01:44 2017

@author: Somchai Somphadung
"""
import pigpio

class GPIODriver():
    def __init__(self):
        self.gpio_driver = pigpio.pi()
        
    def stop(self):
        self.gpio_driver.stop()
        
    

class DriveJob():
    def __init__(self): 
        #threading.Thread.__init__(self)
        #self.queue = None
        self.min_pwm = 40
        self.max_pwm = 250
        self.pwm = self.min_pwm
        self.driver_pins = {"enb":16,"ena":26,"in1":19,"in2":13,"in3":21,"in4":20}
        #self.actuator = None
        self.direction = 0
        
    def reset(self):
        self.pwm = self.min_pwm
        self.direction = 0
        
        
    def _on(self,gpio_driver):
        try:
            for key,val in self.driver_pins.items():
                gpio_driver.set_mode(val,pigpio.OUTPUT)
            
            for key,val in self.driver_pins.items():
                gpio_driver.write(val,1)
        except :
            pass
    

    def _off(self,gpio_driver):
        try:
            for key,val in self.driver_pins.items():
                gpio_driver.write(val,0)
        except :
            pass 

    def park(self, gpio_driver):
        gpio_driver.write(self.driver_pins["in1"],1)
        gpio_driver.write(self.driver_pins["in2"],1)
        gpio_driver.write(self.driver_pins["in3"],1)
        gpio_driver.write(self.driver_pins["in4"],1)
        gpio_driver.set_PWM_dutycycle(self.driver_pins["ena"],0)
        gpio_driver.set_PWM_dutycycle(self.driver_pins["enb"],0)
    
    def left_rotate(self,dir,gpio_driver):
        #if speed > 255 : speed = 255
        #if speed < 0 : speed = 0
        #self.gpio_driver.set_PWM_dutycycle(self.driver_pins["ena"],0)
        self.direction = dir
        if self.direction == 1: #forward
            gpio_driver.write(self.driver_pins["in1"],1)
            gpio_driver.write(self.driver_pins["in2"],0)
        elif self.direction == 2: #backward
            gpio_driver.write(self.driver_pins["in1"],0)
            gpio_driver.write(self.driver_pins["in2"],1)
        
        
    
    def right_rotate(self,dir,gpio_driver):
        #if speed > 255 : speed = 255
        #if speed < 0 : speed = 0
        #self.gpio_driver.set_PWM_dutycycle(self.driver_pins["ena"],0)
        self.direction = dir
        if self.direction == 1 :
            gpio_driver.write(self.driver_pins["in3"],0)
            gpio_driver.write(self.driver_pins["in4"],1)
        elif self.direction == 2 :
            gpio_driver.write(self.driver_pins["in3"],1)
            gpio_driver.write(self.driver_pins["in4"],0)
        
    
    def accelerate(self,gpio_driver):
        gpio_driver.set_PWM_dutycycle(self.driver_pins["ena"],self.pwm)
        gpio_driver.set_PWM_dutycycle(self.driver_pins["enb"],self.pwm)
            
    
    def forward(self,gpio_driver):
        self.left_rotate(1,gpio_driver)
        self.right_rotate(1,gpio_driver)
    

    def backward(self,gpio_driver):
        self.left_rotate(2,gpio_driver)
        self.right_rotate(2,gpio_driver)



class SteeringJob():
    def __init__(self):
        # You need to calibrate these values to fit your environment
        self.min_steer = 1100
        self.max_steer = 1900
        self.mid_steer = int((self.max_steer + self.min_steer)/2)
        self.x_max = 200
        self.x_min = 0
        self.servo = 18
        self.actuator = None
        
    def steer(self,x,gpio_driver):
        
        x_norm = 100 + int(x * 100) #change value of x to be in range of 0 - 200
        pwd = self.max_steer - (self.x_max - x_norm) * (self.max_steer - self.min_steer) / (self.x_max - self.x_min)
        pwd = int(pwd)
        
        if pwd > self.max_steer : pwd = self.max_steer
        elif pwd < self.min_steer : pwd = self.min_steer
        gpio_driver.set_servo_pulsewidth(self.servo,pwd)
    
    
            
