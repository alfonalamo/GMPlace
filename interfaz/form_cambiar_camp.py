import tkinter as tk
from constantes import estilos, textos
from interfaz import items
from interfaz.formulario import Formulario

class FormularioCambiarCamp(Formulario):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.config(background=estilos.Color.FONDO_NAV)
        self.nombre_master = tk.StringVar()
        self.nombre_campagna = tk.StringVar()
        self.lista_campagna = items.ListBoxCampagnas(
            self,
        )
        self.lista_campagna.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=5,
            padx=5
        )
        items.BotonEstandar(
            self,
            "Cambiar a esta campaña",
            self.cambiar_campagna
        ).pack(
            side=tk.TOP,
            pady=10,
            padx=10
        )
        self.lista_campagna.llenar_lista(self.controlador.recuperar_info_campas())

    def cambiar_campagna(self):
        if self.lista_campagna.curselection():
            campagna, master = self.lista_campagna.get_seleccion()
            self.controlador.rearranque(campagna,master)
            self.destroy()
