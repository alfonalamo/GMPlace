import tkinter as tk
from tkinter import  ttk
from abc import ABC

from constantes import estilos


class TarjetaPersonaje(tk.Frame):
    pass

class BotonNavegador(tk.Button):
    def __init__(self, navegador, pantalla, controlador):
        self.pantalla = pantalla
        self.controlador = controlador
        self.navegador = navegador
        super().__init__(self.navegador)
        self.config(text=pantalla, command= self.comando, **estilos.ESTILO_PREDETERMINADO_BOTON)

    def comando(self):
        self.navegador.boton_activo.activar()
        self.controlador.muestra_pantalla(self.navegador.contenedor,self.pantalla)
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

    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()[0]
            return self.get(indice)

    def actualizar(self, dic):
        self.delete(0,tk.END)
        try:
            for nombre_pj, objeto_pj in dic.items():
                self.insert(tk.END, nombre_pj)
                if objeto_pj.tipo == "pj":
                    self.itemconfig(tk.END, bg=estilos.Color.ALIADO)
                else:
                    self.itemconfig(tk.END, bg="lightred")
        except AttributeError:
            print("error", dic)
            pass
        
class ListBoxPersonajes(ListBoxEstandar)   :     
    def __init__(self, contenedor):
        super().__init__(contenedor)
        
    def actualizar(self, dic_pers):
        try:
            self.delete(0,tk.END)
        except tk.TclError:
            pass
        try:
            for nombre_pj, objeto_pj in dic_pers.items():
                self.insert(tk.END, f"{nombre_pj} - {objeto_pj.jugador}")
                if objeto_pj.tipo == "pj":
                    self.itemconfig(tk.END, bg=estilos.Color.ALIADO)
                else:
                    self.itemconfig(tk.END, bg="red")
        except AttributeError:
            print("error", dic_pers)
            pass

    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()[0]
            return self.get(indice).split("-")[0].strip(" ")


class ListBoxCampagnas(ListBoxEstandar)   :
    def __init__(self, contenedor):
        super().__init__(contenedor)

    def llenar_lista(self, tupla):
        self.delete(0,tk.END)
        for camp in tupla:
            self.insert(0,f"{camp[0]} - {camp[1]}")

    def get_seleccion(self):
        if self.curselection():
            indice = self.curselection()
            campagna = self.get(indice).split("-")[0].strip(" ")
            master = self.get(indice).split("-")[1].strip(" ")
            return campagna, master
