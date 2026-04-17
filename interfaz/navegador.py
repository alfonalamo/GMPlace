import tkinter as tk
from constantes import estilos


class Navegador(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.configure(background=estilos.Color.FONDO_NAV, width=300)
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
                        "Combate",
                       self.controlador
                       )

        BotonNavegador(self,
                        "Elementos",
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
            justify=tk.LEFT
        )
        self.pack(
            side= tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=20)
