import tkinter as tk


class Formulario(tk.Toplevel):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor)
        self.contenedor = contenedor
        self.controlador = controlador

    def cargawidgets(self):
        pass