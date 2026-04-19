import tkinter as tk
from abc import abstractmethod, ABC
from constantes import estilos
from interfaz.items import BotonNavegador


class Navegador(tk.Frame):
    def __init__(self, contenedor, controlador, pantallas):
        super().__init__(contenedor)
        self.contenedor = contenedor
        self.controlador = controlador
        self.pantallas = pantallas # Una lista de objetos pantalla que hay que cargar
        self.botones = {}
        self.carga_botones()
        self.boton_activo = self.botones[contenedor.pantalla_activa]
        self.boton_activo.desactivar()
        self.muestra_botones()

        self.configure(background=estilos.Color.FONDO_NAV, width=300)

    def carga_botones(self):
        for pantalla in self.pantallas:
            self.botones[pantalla.nombre] = BotonNavegador(
                self,
                pantalla.nombre,
                self.controlador
            )
    @abstractmethod
    def muestra_botones(self):
        pass

class NavegadorSuperior(Navegador):
    def __init__(self, contenedor, controlador, pantallas):
        super().__init__(contenedor, controlador, pantallas)

    def muestra_botones(self):
        for boton in self.botones.values():
            boton.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=20)

class NavegadorLateral(Navegador):
    def __init__(self, contenedor, controlador, pantallas):
        super().__init__(contenedor, controlador, pantallas)

    def muestra_botones(self):
        for boton in self.botones.values():
            boton.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=5,
            pady=5
            )
