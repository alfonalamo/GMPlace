import tkinter as tk

from constantes import estilos
from pantallas import Inicio, Campana, Personajes
from navegador import Navegador


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
            fill= tk.BOTH,
            expand= False,
            padx= 22,
            pady= 11
        )

        contenedor = tk.Frame(self)
        self.modo = ""
        contenedor.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand= False,
            padx= 22,
            pady= 11
        )
        contenedor.configure(background=estilos.Color.FONDO)
        contenedor.configure(background="red")
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_rowconfigure(0, weight=1)

        # Creamos un diccionario de frames y lo llenamos con los distintos frames de pantallas.py,
        # desde ese diccionario lo cargamos al contenedor principal
        self.frames ={}

        for F in (Inicio, Campana, Personajes):
            frame = F(contenedor, self)
            self.frames[str(frame.nombre)] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        print("Frames = ", self.frames)
        self.muestra_frame("Inicio")
        # self.muestra_frame(Inicio)

    def muestra_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()

    def cambia_pantalla(self, nombre_pantalla):
        pass