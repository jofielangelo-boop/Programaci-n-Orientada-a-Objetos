# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 13:28:32 2025

@author: HP
"""

# ----------------------------------------------
# Evaluación POO - Sistema de Robots
# Autor: Angelo Salazar
# Archivo: Salazar_Angelo_Robot.py
# ----------------------------------------------

# --------- CLASE BASE ---------
class Robot:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.nombre} ha sido encendido.")
        else:
            print(f"{self.nombre} ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.nombre} ha sido apagado.")
        else:
            print(f"{self.nombre} ya estaba apagado.")

    def mover(self, direccion):
        if self.encendido:
            print(f"{self.nombre} se mueve hacia {direccion} a velocidad {self.velocidad}.")
        else:
            print(f"{self.nombre} no puede moverse porque está apagado.")


# --------- CLASE HIJA (HERENCIA) ---------
class RobotVolador(Robot):
    def __init__(self, nombre, velocidad, altura_maxima):
        super().__init__(nombre, velocidad)
        self.altura_maxima = altura_maxima

    def despegar(self):
        if self.encendido:
            print(f"{self.nombre} está despegando y puede alcanzar hasta {self.altura_maxima} metros.")
        else:
            print(f"{self.nombre} no puede despegar porque está apagado.")

    def aterrizar(self):
        if self.encendido:
            print(f"{self.nombre} está aterrizando suavemente.")
        else:
            print(f"{self.nombre} no puede aterrizar porque está apagado.")


# --------- SIMULACIÓN ---------
if __name__ == "__main__":
    print("=== SIMULACIÓN DE ROBOTS ===\n")

    # Robot terrestre
    robot1 = Robot("RoboTerra-100", 5)
    robot1.encender()
    robot1.mover("adelante")
    robot1.mover("derecha")
    robot1.apagar()

    print("\n-------------------------\n")

    # Robot volador
    drone = RobotVolador("SkyDrone-X", 12, 150)
    drone.encender()
    drone.despegar()
    drone.mover("norte")
    drone.aterrizar()
    drone.apagar()

    print("\n=== FIN DE LA SIMULACIÓN ===")
