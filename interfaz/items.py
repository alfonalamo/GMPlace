import tkinter as tk
from tkinter import  ttk
from abc import ABC, abstractmethod

from constantes import estilos


class ContenedorPrincipal(tk.Frame):
    def __init__(self, contenedor):
        super().__init__(contenedor)
        self.configure(background=estilos.Color.FONDO)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class BotonNavegador(tk.Button):
    def __init__(self, navegador, pantalla, controlador):
        super().__init__(navegador)
        self.navegador = navegador
        self.pantalla = pantalla
        self.controlador = controlador
        self.config(text=str(pantalla).upper(), command= self.comando, **estilos.ESTILO_PREDETERMINADO_BOTON)

    def comando(self):
        self.navegador.boton_activo.activar()
        self.controlador.cambiar_pantalla(self.navegador.contenedor, self.pantalla)
        self.desactivar()
        self.navegador.boton_activo = self

    def desactivar(self):
        self.configure(state=tk.DISABLED)

    def activar(self):
        self.configure(state=tk.NORMAL)

class BotonEstandar(tk.Button):
    def __init__(self, contenedor, texto, comando):
        super().__init__(contenedor)
        self.config(text=texto, command=comando, **estilos.ESTILO_PREDETERMINADO_BOTON)

class MessageEstandar(tk.Message):
    def __init__(self, contenedor, texto):
        super().__init__(contenedor)
        self.config(text=texto, justify=tk.CENTER,  **estilos.ESTILO_PREDETERMINADO_LIGERO)

class LabelEstandar(tk.Label):
    def __init__(self, contenedor, texto):
        super().__init__(contenedor)
        self.config(text=texto, justify=tk.CENTER,  **estilos.ESTILO_PREDETERMINADO_LIGERO)

class ListBoxEstandar(tk.Listbox):
    def __init__(self, contenedor):
        super().__init__(contenedor)
        self.config(background=estilos.Color.FONDO, **estilos.ESTILO_PREDETERMINADO)

    @abstractmethod
    def actualizar(self, dic):
        pass
    @abstractmethod
    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()[0]
            return self.get(indice)

class ListBoxPersonajes(ListBoxEstandar)   :     
    def __init__(self, contenedor):
        super().__init__(contenedor)
        self.lista_pers = dict()
        
    def actualizar(self, dic_pers):
        try:
            self.delete(0,tk.END)
        except tk.TclError:
            pass
        try:
            for id_pj, obj_pj in dic_pers.items():
                alias = f"{obj_pj.nombre} - {obj_pj.jugador}"
                self.lista_pers[alias] = id_pj
                self.insert(tk.END, alias)
                if obj_pj.tipo == "pj":
                    self.itemconfig(tk.END, bg=estilos.Color.ALIADO)
                else:
                    self.itemconfig(tk.END, bg="red")
        except AttributeError:
            print("error", dic_pers)
            pass

    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()[0]
            # return self.get(indice).split("-")[0].strip(" ")
            alias = self.get(indice)
            return self.lista_pers[alias]

class ListBoxCampagnas(ListBoxEstandar)   :
    def __init__(self, contenedor):
        super().__init__(contenedor)

    def actualizar(self, tupla):
        self.delete(0,tk.END)
        for camp in tupla:
            self.insert(0,f"{camp[0]} - {camp[1]}")

    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()
            campagna = self.get(indice).split("-")[0].strip(" ")
            master = self.get(indice).split("-")[1].strip(" ")
            return campagna, master
