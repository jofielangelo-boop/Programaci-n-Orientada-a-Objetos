

class Camiondecargas:
    def __init__(self):
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            print("El camion está encendido.")
            self.encendido = True
        else:
            print("El camion ya está encendido.")

    def apagar(self):
        if self.encendido:
            print("El camion está apagado.")
            self.encendido = False
            self.velocidad = 0
        else:
            print("El camion ya está apagado.")

    def avanzar(self):
        if self.encendido:
            self.velocidad += 1
            print(f"El camion avanza a {self.velocidad} km/h.")
        else:
            print("El camion está apagado. No puede avanzar.")

    def retroceder(self):
        if self.encendido:
            self.velocidad -= 1
            print(f"El camion retrocede a {self.velocidad} km/h.")
        else:
            print("El camion está apagado. No puede retroceder.")


mi_camiondecargas = Camiondecargas()
mi_camiondecargas.encender()
mi_camiondecargas.avanzar()
mi_camiondecargas.retroceder()
mi_camiondecargas.apagar()
