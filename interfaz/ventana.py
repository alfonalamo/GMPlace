import tkinter as tk
from constantes import estilos
from interfaz import items
from interfaz.navegador import Navegador, NavegadorSuperior
from interfaz.pantalla_elementos import Elementos
from interfaz.pantalla_combate import Combate
from interfaz.pantalla_inicio import Inicio


class Ventana(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        # Características generales
        self.title("GM place")
        self.geometry("600x600")
        self.minsize(600,600)
        self.config(background=estilos.Color.FONDO)

        self.controlador = controlador
        self.contenedor_principal = items.ContenedorPrincipal(self)

        tupla_pantallas = (Inicio, Combate, Elementos)
        self.pantallas = {}  # Diccionario de pantallas dentro de la ventana key:nombre, value:objeto Pantalla
        self.pantalla_activa = "Inicio" # La pantalla que se verá por defecto al inicio # Todo: cambiar para que sea un objeto

        for Pantalla in tupla_pantallas:
            pantalla = Pantalla(self.contenedor_principal, self.controlador)
            self.pantallas[str(pantalla.nombre)] = pantalla
        self.controlador.cambiar_pantalla(self, self.pantalla_activa)

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


    def cargar_pantallas(self, ventana, tupla):
        for Pantalla in tupla:
            pantalla = Pantalla(ventana.contenedor_principal, self)
            ventana.pantallas[str(pantalla.nombre)] = pantalla