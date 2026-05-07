import tkinter as tk
from abc import abstractmethod


class Formulario(tk.Toplevel):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor)
        self.contenedor = contenedor
        self.controlador = controlador
        self.resizable(False, False)

    @abstractmethod
    def cargawidgets(self):
        pass