# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:07:23 2024

@author: HP
"""

class SensorError(Exception):
    pass

class DataNotFoundError(SensorError):
    def __init__(self, message="Data not found"):
        self.message = message
        super().__init__(self.message)
