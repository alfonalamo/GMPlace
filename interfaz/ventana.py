import tkinter as tk
from constantes import estilos
from interfaz.navegador import Navegador, NavegadorSuperior
from interfaz.pantallas import Inicio, Combate, Elementos

class Ventana(tk.Tk):
    def __init__(self, controlador, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controlador = controlador
        tupla_pantallas = (Inicio, Combate, Elementos)
        self.pantallas = {}  # Diccionario de pantallas dentro de la ventana

        self.contenedor_principal = tk.Frame(self)

        for Pantalla in tupla_pantallas:
            pantalla = Pantalla(self.contenedor_principal, self.controlador)
            self.pantallas[str(pantalla.nombre)] = pantalla

        self.pantalla_activa = "Combate" # La pantalla que se verá por defecto al inicio
        self.barra_navegacion = NavegadorSuperior(self, self.controlador, self.pantallas.values())

        self.title("GM place")
        self.geometry("600x600")
        self.minsize(200,200)
        self.config(background=estilos.Color.FONDO)

        self.barra_navegacion.pack(
            side= tk.TOP,
            fill= tk.X,
            expand= False,
            padx= 0,
            pady= 0
        )

        self.contenedor_principal.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand= True,
            padx= 0,
            pady= 0
        )
        self.contenedor_principal.configure(background=estilos.Color.FONDO)
        self.contenedor_principal.grid_columnconfigure(0, weight=1)
        self.contenedor_principal.grid_rowconfigure(0, weight=1)

    def carga_pantallas(self, ventana, tupla):
        for Pantalla in tupla:
            pantalla = Pantalla(ventana.contenedor_principal, self)
            ventana.pantallas[str(pantalla.nombre)] = pantalla