# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:19:41 2024

@author: HP
"""

import time
from model import LEDModel
from view import LEDView

class LEDController:
    def _init_(self, model, view):
        self.model = model
        self.view = view
    
    def turn_on_led(self):
        self.model.turn_on()
        self.view.display_status(True)
        time.sleep(1)  # Espera 1 segundo con el LED encendido
        self.model.turn_off()
        self.view.display_status(False)
        self.model.cleanup()