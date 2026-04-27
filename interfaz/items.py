import tkinter as tk
from abc import ABC

from constantes import estilos


class TarjetaPersonaje(tk.Frame):
    pass

class BotonNavegador(tk.Button):
    def __init__(self, navegador, pantalla, controlador):
        self.pantalla = pantalla
        self.controlador = controlador
        self.navegador = navegador
        super().__init__(
            navegador,
            text=pantalla,
            command= self.comando,
            **estilos.ESTILO_DEFAULT,
            relief=tk.FLAT,
            # activebackground=estilos.Color.FONDO,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO,
            disabledforeground=estilos.COLOR_FONDO,
            justify=tk.LEFT
        )

    # ToDo : desactivar el botón del menú activo
    def comando(self):
        # self.controlador.reactiva_boton()
        self.navegador.boton_activo.activar()
        self.controlador.muestra_pantalla(self.navegador.contenedor,self.pantalla)
        self.desactivar()
        self.navegador.boton_activo = self

    def desactivar(self):
        self.configure(state=tk.DISABLED)

    def activar(self):
        self.configure(state=tk.NORMAL)