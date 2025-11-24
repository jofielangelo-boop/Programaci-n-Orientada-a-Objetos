# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:20:04 2024

@author: HP
"""

from model import LEDModel
from view import LEDView
from controller import LEDController

def main():
    pin = 18  # Define el pin GPIO donde está conectado el LED
    model = LEDModel(pin)
    view = LEDView()
    controller = LEDController(model, view)
    
    controller.turn_on_led()

if _name_ == "_main_":
    main()