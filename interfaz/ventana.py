import tkinter as tk
from constantes import estilos
from interfaz.navegador import Navegador, NavegadorSuperior
from interfaz.pantalla_elementos import Elementos
from interfaz.pantalla_combate import Combate
from interfaz.pantalla_inicio import Inicio


class Ventana(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        # Defino las características principales de la ventana principal
        self.title("GM place")
        self.geometry("600x600")
        self.minsize(600,600)
        self.config(background=estilos.Color.FONDO)

        self.controlador = controlador
        self.contenedor_principal = tk.Frame(self)

        # Creo y lleno el diccionario de pantallas con las que le doy en la tupla
        tupla_pantallas = (Inicio, Combate, Elementos)
        self.pantallas = {}  # Diccionario de pantallas dentro de la ventana key:nombre, value:objeto Pantalla
        self.pantalla_activa = "Inicio" # La pantalla que se verá por defecto al inicio # Todo: cambiar para que sea un objeto

        for Pantalla in tupla_pantallas:
            pantalla = Pantalla(self.contenedor_principal, self.controlador)
            self.pantallas[str(pantalla.nombre)] = pantalla
        self.controlador.muestra_pantalla(self,self.pantalla_activa)

        self.barra_navegacion = NavegadorSuperior(self, self.controlador, self.pantallas.values())

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