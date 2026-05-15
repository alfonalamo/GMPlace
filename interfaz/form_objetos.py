import tkinter as tk
from tkinter import messagebox as mb, ttk

from interfaz import items
from interfaz.form_ver_obj import FormularioVerObj
from interfaz.formulario import Formulario
import constantes as cons

class FormularioObjetos(Formulario):
    def __init__(self, contenedor, controlador, pj):
        super().__init__(contenedor,  controlador)
        self.pj = pj
        self.lista_objetos = items.ListBoxObjetos(self)
        self.lista_objetos_pj = items.ListBoxObjetos(self)
        self.lista_objetos_pj.bind("<<ListboxSelect>>", self.abrir_form_ver_obj)
        self.cargarwidgets()
        self.actualizar_listas()

    def cargarwidgets(self):
        items.LabelEstandar(self, "Objetos disponibles").pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=5,
            padx=5
        )
        self.lista_objetos.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=0,
            padx=5
        )
        items.BotonEstandar(
            self,
            "Cargar objeto",
            self.cargar_obj
        ).pack(
            side=tk.TOP,
            pady=10,
            padx=10
        )
        self.lista_objetos_pj.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
            pady=5,
            padx=5
        )


    def cargar_obj(self):
        if self.lista_objetos.get_seleccion():
            obj = self.lista_objetos.get_seleccion()
            self.controlador.dar_obj(obj,self.pj)
            self.lista_objetos_pj.actualizar_con_lista(self.controlador.obtener_objetos_pj(self.pj))

    def abrir_form_ver_obj(self, event):
        if self.lista_objetos_pj.get_seleccion():
            try:
                objeto = self.lista_objetos_pj.get_seleccion()
                FormularioVerObj(self, self.controlador, objeto, self.pj)
            except KeyError:
                pass

    def actualizar_listas(self):
        self.lista_objetos.actualizar(self.controlador.objetos)
        self.lista_objetos_pj.actualizar_con_lista(self.controlador.obtener_objetos_pj(self.pj))

