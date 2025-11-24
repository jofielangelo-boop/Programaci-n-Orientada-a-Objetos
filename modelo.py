# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:18:57 2024

@author: HP
"""

import RPi.GPIO as GPIO
import time

class LEDModel:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
    
    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
    def cleanup(self):
        GPIO.cleanup()