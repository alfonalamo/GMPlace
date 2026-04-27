import tkinter as tk
from abc import abstractmethod
from constantes import estilos, config
from interfaz.navegador import NavegadorLateral


class Pantalla(tk.Frame):
    def __init__(self, contenedor, controlador, nombre):
        super().__init__(contenedor)
        self.configure(background=estilos.Color.FONDO)
        self.controlador = controlador
        self.nombre = nombre
        self.opcion_seleccionada = tk.StringVar(self, value="a")
        self.grid(row=0, column=0, sticky=tk.NSEW)


    @abstractmethod
    def carga_widgets(self):
        pass