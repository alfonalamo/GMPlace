import tkinter as tk

from constantes import estilos
from interfaz.pantallas import Inicio, Combate, Elementos
from interfaz.navegador import Navegador


class Controlador(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GM place")
        self.geometry("600x600")
        self.minsize(200,200)
        self.config(background=estilos.Color.FONDO)

        navegador = Navegador(self, self)
        navegador.pack(
            side= tk.TOP,
            fill= tk.X,
            expand= False,
            padx= 0,
            pady= 0
        )

        contenedor_principal = tk.Frame(self)
        self.modo = ""
        contenedor_principal.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand= False,
            padx= 22,
            pady= 11
        )
        contenedor_principal.configure(background=estilos.Color.FONDO)
        contenedor_principal.grid_columnconfigure(0, weight=1)
        contenedor_principal.grid_rowconfigure(0, weight=1)

        # Creamos un diccionario de frames y lo llenamos con los distintos frames de pantallas.py,
        # desde ese diccionario lo cargamos al contenedor principal
        self.frames ={}

        for F in (Inicio, Combate, Elementos):
            frame = F(contenedor_principal, self)
            self.frames[str(frame.nombre)] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        print("Frames = ", self.frames)
        self.muestra_frame("Inicio")

    def muestra_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()

    def cambia_pantalla(self, nombre_pantalla):
        pass