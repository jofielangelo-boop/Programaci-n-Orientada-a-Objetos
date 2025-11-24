# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:48:12 2024

@author: HP
"""

import tkinter as tk
from tkinter import ttk

class RobotModel:
    def __init__(self):
        self.elevation = 0
        self.rotation = 0
        self.length = 0

    def move_elevation(self, increment):
        self.elevation += increment

    def move_rotation(self, increment):
        self.rotation += increment

    def move_length(self, increment):
        self.length += increment

    def stop_movement(self):
        print("Movimiento detenido.")

class RobotView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controlador del Robot")

        self.label_elevation = ttk.Label(self, text="Elevacion:")
        self.label_elevation.grid(row=0, column=0)
        self.entry_elevation = ttk.Entry(self)
        self.entry_elevation.grid(row=0, column=1)

        self.label_rotation = ttk.Label(self, text="Rotacion:")
        self.label_rotation.grid(row=1, column=0)
        self.entry_rotation = ttk.Entry(self)
        self.entry_rotation.grid(row=1, column=1)

        self.label_length = ttk.Label(self, text="Longitud:")
        self.label_length.grid(row=2, column=0)
        self.entry_length = ttk.Entry(self)
        self.entry_length.grid(row=2, column=1)

        self.button_submit = ttk.Button(self, text="Enviar", command=self.submit_command)
        self.button_submit.grid(row=3, columnspan=2)

        self.model = RobotModel()

    def submit_command(self):
        try:
            elevation = float(self.entry_elevation.get())
            rotation = float(self.entry_rotation.get())
            length = float(self.entry_length.get())
            self.model.move_elevation(elevation)
            self.model.move_rotation(rotation)
            self.model.move_length(length)
            print("Movimiento del robot actualizado.")
            print("Elevación:", self.model.elevation)
            print("Rotación:", self.model.rotation)
            print("Longitud:", self.model.length)
        except ValueError:
            print("Error: Por favor ingrese valores numéricos.")
            

def main():
    view = RobotView()
    view.mainloop()

if __name__ == "__main__":
    main()
