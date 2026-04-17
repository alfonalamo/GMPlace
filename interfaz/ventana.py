import tkinter as tk
from constantes import estilos
from interfaz.navegador import Navegador, NavegadorVertical
from interfaz.pantallas import Inicio, Combate, Elementos

class Ventana(tk.Tk):
    def __init__(self, controlador, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GM place")
        self.geometry("600x600")
        self.minsize(200,200)
        self.config(background=estilos.Color.FONDO)
        self.pantallas ={}
        self.modo = ""
        self.controlador = controlador

        navegador = NavegadorVertical(self, self.controlador)
        navegador.pack(
            side= tk.TOP,
            fill= tk.X,
            expand= False,
            padx= 0,
            pady= 0
        )

        self.contenedor_principal = tk.Frame(self)
        self.contenedor_principal.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand= False,
            padx= 22,
            pady= 11
        )
        self.contenedor_principal.configure(background=estilos.Color.FONDO)
        self.contenedor_principal.grid_columnconfigure(0, weight=1)
        self.contenedor_principal.grid_rowconfigure(0, weight=1)

