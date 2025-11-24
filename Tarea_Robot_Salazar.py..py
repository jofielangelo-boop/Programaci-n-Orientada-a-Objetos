# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 13:03:50 2025

@author: HP
"""


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        self.x = 0

    def saludar(self):
        return f"Hola, soy {self.nombre}"

    def mover(self, distancia):
        self.x += distancia
        self.bateria -= 10  # Gasto fijo por movimiento

    def status(self):
      return f"batería={self.bateria}, x={self.x}"


class RobotVolador(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.z = 0

    def volar(self, altura):
        self.z += altura
        self.bateria -= abs(altura) * 2  

    def status(self):
       return f"batería={self.bateria}, x={self.x}, z={self.z}"




r = RobotVolador("Atlas")
print(r.saludar())

r.mover(10)      
r.volar(5)       
print(r.status())

r.volar(-3)      
print(r.status())
