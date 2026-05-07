import tkinter as tk
from tkinter import messagebox as mb, ttk

from interfaz import items
from interfaz.formulario import Formulario
import constantes as cons

class FormularioAtacar(Formulario):
    def __init__(self, contenedor, controlador, pj):
        super().__init__(contenedor,  controlador)
        self.pj = pj
        self.personajes = self.controlador.personajes.keys()
        self.arma = tk.StringVar()
        self.objetivo = tk.StringVar()
        self.israndom = tk.BooleanVar()
        self.cargarwidgets()

    def cargarwidgets(self):
        items.LabelEstandar(self, "Atacar a: ").pack(side= tk.LEFT, padx=5)
        ttk.Combobox(self, values=self.personajes, state="readonly", textvariable=self.objetivo
                     ).pack(side= tk.LEFT, padx=5)
        items.LabelEstandar(self, "con: ").pack(side= tk.LEFT, padx=5)
        ttk.Combobox(self, values=["a","b","c"], state="readonly", textvariable=self.arma
                     ).pack(side= tk.LEFT, padx=5)
        tk.Checkbutton(self, text= "¿Tirada random?:", variable= self.israndom
                       ).pack(side= tk.LEFT, padx=5)
        items.BotonEstandar(self, "Atacar", self.atacar).pack(side= tk.LEFT, padx=5)

    def atacar(self):
        if self.controlador.ataque(self.pj, self.objetivo, self.arma):
            mb.showinfo("Ataque realizado")
            self.destroy()
        else:
            mb.showerror("ERROR")





