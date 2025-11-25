import RPi.GPIO as GPIO
import time
class LED():
   def __init__(self, pin_gpio):
       self.PIN_LED = pin_led

       self.estado_led =False
       print("Iniciando led{self.PIN_LED}")
   def encender(self):
       self.estado_led=True
       print("led{self.PIN_LED}encendido")
   def apagar(self):
       self.estado_led=False
       print("led{self.PIN_LED}apagado")
   def blink(self, veces=3):
       print("Parpadeando led{self.PIN_LED}{veces}")
       for i in    
