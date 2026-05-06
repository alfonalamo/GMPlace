import tkinter as tk
from tkinter import messagebox as msg
import constantes as cons
from constantes import estilos, textos
from interfaz import items
from interfaz.formulario import Formulario
from logica import util

class FormularioCrearCamp(Formulario):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.controlador = controlador
        # self.protocol("WM_DELETE_WINDOW", self.recoger_datos)
        self.config(background=estilos.Color.FONDO_NAV)
        self.nombre_master = tk.StringVar()
        self.nombre_campagna = tk.StringVar()
        items.LabelEstandar(
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
        entrada_nombre = tk.Entry(self, textvariable=self.nombre_master)
        entrada_nombre.pack()
        entrada_nombre.insert(tk.END,"Master")
        items.LabelEstandar(
            self,
            "Nombre de la campaña:"
        ).pack()
        entrada_campagna = tk.Entry(self, textvariable=self.nombre_campagna)
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
            "campagna" :self.nombre_campagna.get()
        }
        if self.controlador.escribir_config(config):
            msg.showinfo("OK", "Campaña creada correctamente")
            self.destroy()
            self.controlador.rearranque(config["campagna"],config["nombre"])
        else:
            msg.showerror("ERROR", "La campaña existe")


    #     self.config(background=estilos.Color.FONDO_NAV)
    #     self.nombre_master = tk.StringVar()
    #     self.nombre_campagna = tk.StringVar()
    #     items.LabelEstandar(
    #         self,
    #         textos.tutorial
    #     ).pack(
    #         side=tk.TOP,
    #         fill=tk.BOTH,
    #         expand=False,
    #         pady=20,
    #         padx=10
    #     )
    #     items.LabelEstandar(
    #         self,
    #         "Nombre del director de juego:"
    #     ).pack()
    #     entrada_nombre = tk.Entry(textvariable=self.nombre_master)
    #     entrada_nombre.pack()
    #     entrada_nombre.insert(tk.END,"Master")
    #     items.LabelEstandar(
    #         self,
    #         "Nombre de la campaña:"
    #     ).pack()
    #     entrada_campagna = tk.Entry(textvariable=self.nombre_campagna)
    #     entrada_campagna.pack(
    #        pady=5
    #     )
    #     entrada_campagna.insert(tk.END,"Campaña")
    #     items.BotonEstandar(
    #         self,
    #         "Crear campaña",
    #         self.recoger_datos
    #     ).pack(
    #         pady=10
    #     )
    #
    # def recoger_datos(self):
    #     config = {
    #         "nombre" : self.nombre_master.get(),
    #         "campagna" :self.nombre_campagna.get()
    #     }
    #     self.controlador.escribir_config(config)
    #     self.destroy()