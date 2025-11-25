# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:13:32 2025

@author: ESTUDIANTE
"""

import RPi.GPIO as GPIO
import time

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

class Robot:
    def __init__(self, nombre, modelo, pin_led=LED_PIN):
        self.nombre = nombre
        self.modelo = modelo
        self.pin_led = pin_led

    def encender(self):
        GPIO.output(self.pin_led, GPIO.HIGH)
        print(self.nombre, "está encendido.")

    def apagar(self):
        GPIO.output(self.pin_led, GPIO.LOW)
        print(self.nombre, "está apagado.")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)

class RobotObrero(Robot):
    def __init__(self, nombre, modelo, tarea, pin_led=LED_PIN):
        super().__init__(nombre, modelo, pin_led)
        self.tarea = tarea

    def trabajar(self):
        print(self.nombre, "está realizando la tarea:", self.tarea)
        self.encender()
        time.sleep(1)
        self.apagar()

if __name__ == "__main__":
    robot_fabrica = RobotObrero("Brazo-A3", "Atlas-2024", "Ensamblar Componente")
    
    robot_fabrica.estado()

    robot_fabrica.encender()
    time.sleep(2)
    
    robot_fabrica.trabajar()

    robot_fabrica.apagar()
    time.sleep(1)
    
    GPIO.cleanup()