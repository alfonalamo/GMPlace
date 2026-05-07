import tkinter as tk
from tkinter import messagebox as msg
from constantes import textos, estilos
from interfaz import items


class Tutorial(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.protocol("WM_DELETE_WINDOW", self.recoger_datos)
        self.config(background=estilos.Color.FONDO_NAV)
        self.nombre_master = tk.StringVar()
        self.nombre_campagna = tk.StringVar()
        items.MessageEstandar(
            self,
            textos.tutorial
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=20,
            padx=10
        )
        items.LabelEstandar(
            self,
            "Nombre del director de juego:"
        ).pack()
        entrada_nombre = tk.Entry(textvariable=self.nombre_master)
        entrada_nombre.pack()
        entrada_nombre.insert(tk.END,"Master")
        items.LabelEstandar(
            self,
            "Nombre de la campaña:"
        ).pack()
        entrada_campagna = tk.Entry(textvariable=self.nombre_campagna)
        entrada_campagna.pack(
           pady=5
        )
        entrada_campagna.insert(tk.END,"Campaña")
        items.BotonEstandar(
            self,
            "Crear campaña",
            self.recoger_datos
        ).pack(
            pady=10
        )

    def recoger_datos(self):
        config = {
            "nombre" : self.nombre_master.get(),
            "campagna" :self.nombre_campagna.get().replace(" ","_")
        }
        if self.controlador.escribir_config(config):
            msg.showinfo("OK", "Campaña creada correctamente")
            self.controlador.continuar_arranque()
            self.destroy()
        else:
            msg.showerror("No deberias ver esto", "La campaña existe")
            # pass