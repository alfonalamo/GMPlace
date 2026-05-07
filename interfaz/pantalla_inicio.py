import tkinter as tk

from constantes import estilos, config
from interfaz import items
from interfaz.form_cambiar_camp import FormularioCambiarCamp
from interfaz.form_crear_camp import FormularioCrearCamp
from interfaz.pantalla import Pantalla


class Inicio(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Inicio")
        self.carga_widgets()

    def carga_widgets(self):
        frame_superior = tk.Frame(self, background=estilos.Color.FONDO)
        frame_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        frame_campagna = tk.Frame(frame_superior, background=estilos.Color.FONDO)
        frame_campagna.pack(side=tk.LEFT, fill=tk.NONE, expand=False, pady=5, padx=5)
        camp = items.LabelEstandar(frame_campagna, f"Nombre de campaña: {self.controlador.campagna}")
        camp.pack(side=tk.TOP, fill=tk.NONE, expand=False)
        # camp.config(background=estilos.Color.FONDO)
        items.BotonEstandar(frame_campagna,"Cambiar de campaña", self.abrir_formulario_cambio
                            ).pack(side=tk.TOP, fill=tk.NONE, expand=False, pady=5)

        frame_master = tk.Frame(frame_superior, background=estilos.Color.FONDO)
        frame_master.pack(side=tk.LEFT, fill=tk.NONE, expand=False, pady=5, padx=5)
        master = items.LabelEstandar(frame_master, f"Nombre del director de juego: {self.controlador.nombre_master}")
        master.pack(side=tk.TOP, fill=tk.NONE, expand=True)
        # master.config(background=estilos.Color.FONDO)
        items.BotonEstandar(frame_master,"Crear nueva campaña", self.abrir_formulario_crear_campagna
                            ).pack(side=tk.TOP, fill=tk.NONE, expand=True, pady=5)

        frame_inferior = tk.Frame(self)
        frame_inferior.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def abrir_formulario_cambio(self):
        FormularioCambiarCamp(self, self.controlador)

    def abrir_formulario_crear_campagna(self):
        FormularioCrearCamp(self,self.controlador)