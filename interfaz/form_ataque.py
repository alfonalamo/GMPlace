import tkinter as tk
from tkinter import messagebox as mb, ttk

from interfaz import items
from interfaz.formulario import Formulario
import constantes as cons

class FormularioAtacar(Formulario):
    def __init__(self, contenedor, controlador, pj):
        super().__init__(contenedor,  controlador)
        self.pj = pj
        self.personajes = self.controlador.obtener_personajes()
        self.armas = self.controlador.obtener_armas(pj.id)
        self.dict_alias_pj = dict()
        self.dict_alias_nombreobj = dict()
        self.lista_personajes = list()
        self.lista_armas = list()
        self.arma = tk.StringVar()
        self.objetivo = tk.StringVar()
        self.israndom = tk.BooleanVar()
        self.llenar_desplegables()
        self.cargarwidgets()

    def cargarwidgets(self):
        items.LabelEstandar(self, "Atacar a: ").pack(side= tk.LEFT, padx=5)
        ttk.Combobox(self, values=self.lista_personajes, state="readonly", textvariable=self.objetivo
                     ).pack(side= tk.LEFT, padx=5)
        items.LabelEstandar(self, "con: ").pack(side= tk.LEFT, padx=5)
        ttk.Combobox(self, values=self.armas, state="readonly", textvariable=self.arma
                     ).pack(side= tk.LEFT, padx=5)
        tk.Checkbutton(self, text= "¿Tirada random?:", variable= self.israndom
                       ).pack(side= tk.LEFT, padx=5)
        items.BotonEstandar(self, "Atacar", self.atacar).pack(side= tk.LEFT, padx=5)

    def atacar(self):
        if self.controlador.ataque(self.pj, self.dict_alias_pj[self.objetivo.get()], self.arma.get()):
            mb.showinfo("Ataque realizado","Ataque realizado correctamennte")
            self.destroy()
        else:
            mb.showerror("ERROR", "Algo ha fallado")

    def llenar_desplegables(self):
        for pj in self.personajes:
            alias = f"{pj.nombre} - {pj.jugador}"
            self.dict_alias_pj[alias] = pj
            self.lista_personajes.append(alias)
        for arma in self.lista_armas:
            alias = f"{arma.nombre}"
            self.dict_alias_nombreobj[alias] = arma
            self.lista_armas.append(arma.nombre.replace(" ", "_"))





