import tkinter as tk
from tkinter import messagebox as mb, ttk
import constantes as cons
from interfaz import items
from interfaz.formulario import Formulario
from logica import util


class FormularioVerObj(Formulario):
    def __init__(self, contenedor, controlador, objeto, pj):
        super().__init__(contenedor,  controlador)
        self.objeto = objeto
        self.pj = pj
        self.nombre_ant = self.objeto.nombre
        self.nombre = tk.StringVar()
        self.tipo = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.precio = tk.DoubleVar()
        self.modificador = tk.IntVar()
        self.cargarwidgets()
        self.resizable(False, False)
        self.geometry("300x200")

    def cargarwidgets(self):
        frame_texto = tk.Frame(self)
        frame_texto.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        frame_nombre = tk.Frame(frame_texto)
        frame_nombre.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_nombre, text="Nombre: ").pack(side=tk.LEFT)
        items.LabelEstandar(frame_nombre, self.objeto.nombre).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_descripcion = tk.Frame(frame_texto)
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_descripcion, text="Descripción: ").pack(side=tk.TOP)
        items.LabelEstandar(frame_descripcion, self.objeto.descripcion).pack(side=tk.TOP, fill=tk.BOTH, padx=2, expand=True)

        frame_tipo = tk.Frame(frame_texto)
        frame_tipo.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_tipo, text="Tipo: ").pack(side=tk.LEFT)
        items.LabelEstandar(frame_tipo, self.objeto.tipo).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_modificador = tk.Frame(frame_texto)
        frame_modificador.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_modificador, text="Modificador: ").pack(side=tk.LEFT)
        items.LabelEstandar(frame_modificador, self.objeto.modificador).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_precio = tk.Frame(frame_texto)
        frame_precio.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_precio, text="Precio: ").pack(side=tk.LEFT)
        items.LabelEstandar(frame_precio, self.objeto.precio).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        if self.objeto.tipo == "pocion":
            items.BotonEstandar(frame_texto, "Usar poción", self.usar_obj).pack(side=tk.TOP, fill=tk.X)

        items.BotonEstandar(frame_texto, "Quitar objeto", self.quitar_obj).pack(side=tk.TOP, fill=tk.X)


    def usar_obj(self):
        if self.objeto.tipo == "pocion":
            self.controlador.curacion(self.pj, self.objeto)
            self.quitar_obj()

    def quitar_obj(self):
        if self.controlador.quitar_obj(self.objeto, self.pj):
            self.contenedor.actualizar_listas()
            self.destroy()