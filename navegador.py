import tkinter as tk
from constantes import estilos


class Navegador(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.configure(background=estilos.Color.FONDO)
        self.controlador = controlador
        # self.opcion_seleccionada = tk.StringVar(self, value="a")
        self.carga_widgets()

        print("navegador", self.controlador)

    def carga_widgets(self):
        BotonNavegador(self,
                        "Inicio",
                       self.controlador
                       )

        BotonNavegador(self,
                        "Campaña",
                       self.controlador
                       )

        BotonNavegador(self,
                        "Personajes",
                       self.controlador
                       )

class BotonNavegador(tk.Button):
    def __init__(self, parent, texto, controlador):
        super().__init__(
            parent,
            text=texto,
            command=lambda: controlador.muestra_frame(texto),
            **estilos.ESTILO_DEFAULT,
            relief=tk.FLAT,
            # activebackground=estilos.Color.FONDO,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO,
        )
        self.pack(
            side= tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5)
