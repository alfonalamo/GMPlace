import tkinter as tk
from constantes import textos, estilos


class Tutorial(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.protocol("WM_DELETE_WINDOW", self.recoger_datos)
        self.config(background=estilos.Color.FONDO_NAV)
        self.nombre_master = tk.StringVar()
        self.nombre_campagna = tk.StringVar()
        tk.Label(
            text=textos.tutorial,
            background=estilos.Color.FONDO_NAV,
            **estilos.ESTILO_PREDETERMINADO
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=20,
            padx=10
        )
        tk.Label(
            text="Nombre del director de juego:",
            background=estilos.Color.FONDO_NAV,
            **estilos.ESTILO_PREDETERMINADO
        ).pack()
        entrada_nombre = tk.Entry(textvariable=self.nombre_master)
        entrada_nombre.pack()
        entrada_nombre.insert(tk.END,"Master")
        tk.Label(
            text="Nombre de la campaña:",
            background=estilos.Color.FONDO_NAV,
            **estilos.ESTILO_PREDETERMINADO
        ).pack()
        entrada_campagna = tk.Entry(textvariable=self.nombre_campagna)
        entrada_campagna.pack(
           pady=5
        )
        entrada_campagna.insert(tk.END,"Campaña")
        tk.Button(
            text="Crear campaña",
            **estilos.ESTILO_PREDETERMINADO,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO,
            command=self.recoger_datos
        ).pack(
            pady=10
        )

    def recoger_datos(self):
        config = {
            "nombre" : self.nombre_master.get(),
            "campagna" :self.nombre_campagna.get()
        }
        self.controlador.escribir_config(config)
        self.destroy()

