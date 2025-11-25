# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 17:54:26 2025

@author: ESTUDIANTE
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class Robot:
    PIN_LED = 18

    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.led_encendido = False 

    def encender(self):
        print(self.nombre, "está encendido.")
        self.led_encendido = True
        GPIO.output(self.PIN_LED, GPIO.HIGH)
        print(f"**LED: Encendido** (Pin {self.PIN_LED} en HIGH)")

    def apagar(self):
        print(self.nombre, "está apagado.")
        self.led_encendido = False
        GPIO.output(self.PIN_LED, GPIO.LOW)
        print(f"**LED: Apagado** (Pin {self.PIN_LED} en LOW)")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)
        print("Estado del LED (Pin 18):", "Encendido" if self.led_encendido else "Apagado")


class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion

    def presionar_boton_explorar(self):
        print(self.nombre, "ha **PRESIONADO EL BOTÓN** e iniciará la exploración.")
        self.explorar()

    def soltar_boton_explorar(self):
        print(self.nombre, "ha **SOLTADO EL BOTÓN** y se detendrá.")
        self.detener_exploracion()
    
    def explorar(self):
        print(self.nombre, "está explorando la zona:", self.zona_exploracion)

    def detener_exploracion(self):
        print(self.nombre, "se ha **detenido** en la zona:", self.zona_exploracion)


class RobotObrero(Robot):
    def __init__(self, nombre, modelo, tarea):
        super().__init__(nombre, modelo)
        self.tarea = tarea

    def trabajar(self):
        print(self.nombre, "está realizando la tarea:", self.tarea)

class RobotMedico(Robot):
    def __init__(self, nombre, modelo, especialidad):
        super().__init__(nombre, modelo)
        self.especialidad = especialidad
        self.temperatura_detectada = 36.5 
        
    def diagnosticar(self):
        print(self.nombre, "está realizando la especialidad:", self.especialidad)
    
    def detectar_temperatura(self, temperatura):
        self.temperatura_detectada = temperatura
        print(f"**Sensor de Temperatura:** Detectado {self.temperatura_detectada}°C.")
        if self.temperatura_detectada > 37.0:
            print(self.nombre, "recomienda atención médica por posible fiebre.")
        else:
            print(self.nombre, "indica una temperatura corporal normal.")


def simulacion_robots():
    explorador = RobotExplorador("R-Explorer", "XJ-9", "Zona Ártica")
    obrero = RobotObrero("R-Worker", "MK-3", "Construcción de puente")

    print("\n--- Simulación Robot Explorador ---")
    explorador.encender()
    explorador.presionar_boton_explorar()
    explorador.estado()
    explorador.soltar_boton_explorar()
    explorador.apagar()

    print("\n--- Simulación Robot Obrero ---")
    obrero.encender()