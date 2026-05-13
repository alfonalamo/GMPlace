import tkinter as tk
from tkinter import messagebox as mb, ttk

from interfaz import items
from interfaz.formulario import Formulario
import constantes as cons

class FormularioObjetos(Formulario):
    def __init__(self, contenedor, controlador, pj):
        super().__init__(contenedor,  controlador)
        self.pj = pj
        self.lista_objetos = items.ListBoxObjetos(self)
        self.lista_objetos_pj = items.ListBoxObjetos(self)
        self.cargarwidgets()

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
        self.lista_objetos.actualizar(self.controlador.objetos)
        self.lista_objetos_pj.actualizar_con_lista(self.controlador.obtener_objetos_pj(self.pj))

    def cargar_obj(self):
        if self.lista_objetos.get_seleccion():
            obj = self.lista_objetos.get_seleccion()
            self.controlador.dar_obj(obj,self.pj)
            self.lista_objetos_pj.actualizar_con_lista(self.controlador.obtener_objetos_pj(self.pj))
    # def cargarwidgets(self):
    #     items.LabelEstandar(self, "Atacar a: ").pack(side= tk.LEFT, padx=5)
    #     ttk.Combobox(self, values=self.lista_personajes, state="readonly", textvariable=self.objetivo
    #                  ).pack(side= tk.LEFT, padx=5)
    #     items.LabelEstandar(self, "con: ").pack(side= tk.LEFT, padx=5)
    #     ttk.Combobox(self, values=["a","b","c"], state="readonly", textvariable=self.arma
    #                  ).pack(side= tk.LEFT, padx=5)
    #     tk.Checkbutton(self, text= "¿Tirada random?:", variable= self.israndom
    #                    ).pack(side= tk.LEFT, padx=5)
    #     items.BotonEstandar(self, "Atacar", self.atacar).pack(side= tk.LEFT, padx=5)
    #
    # def atacar(self):
    #     if self.controlador.ataque(self.pj, self.objetivo.get(), self.arma.get()):
    #         mb.showinfo("Ataque realizado")
    #         self.destroy()
    #     else:
    #         mb.showerror("ERROR")
    #
    # def llenar_desplegables(self):
    #     for pj in self.personajes:
    #         alias = f"{pj.nombre} - {pj.jugador}"
    #         self.dict_alias_pj[alias] = pj
    #         self.lista_personajes.append(alias)
    #     for arma in self.lista_armas:
    #         self.lista_armas.append(arma.nombre)


