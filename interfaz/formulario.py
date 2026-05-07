import tkinter as tk
from abc import abstractmethod, ABC


class Formulario(tk.Toplevel, ABC):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor)
        self.contenedor = contenedor
        self.controlador = controlador
        self.resizable(False, False)

    @abstractmethod
    def cargarwidgets(self):
        pass