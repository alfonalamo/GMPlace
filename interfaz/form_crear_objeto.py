import tkinter as tk
from tkinter import messagebox as mb, ttk
import constantes as cons
from interfaz import items
from interfaz.formulario import Formulario
from logica import util


class FormularioCrearObjeto(Formulario):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.nombre = tk.StringVar()
        self.tipo = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.precio = tk.DoubleVar()
        self.modificador = tk.IntVar()
        self.cargarwidgets()
        self.resizable(False, False)

    def cargarwidgets(self):
        frame_texto = tk.Frame(self)
        frame_texto.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        frame_nombre = tk.Frame(frame_texto)
        frame_nombre.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_nombre, text="Nombre").pack(side=tk.LEFT)
        tk.Entry(frame_nombre, textvariable=self.nombre).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_descripcion = tk.Frame(frame_texto)
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_descripcion, text="Descripción").pack(side=tk.TOP)
        tk.Entry(frame_descripcion, textvariable=self.descripcion).pack(side=tk.TOP, fill=tk.BOTH, padx=2, expand=True)

        frame_tipo = tk.Frame(frame_texto)
        frame_tipo.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_tipo, text="Tipo").pack(side=tk.LEFT)
        ttk.Combobox(frame_tipo, values=cons.tipos_objetos, state="readonly", textvariable=self.tipo
                     ).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_modificador = tk.Frame(frame_texto)
        frame_modificador.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_modificador, text="Modificador").pack(side=tk.LEFT)
        tk.Spinbox(
            frame_modificador,
            from_=-10,
            to=1000,
            increment=1,
            width=1,
            textvariable=self.modificador
        ).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_precio = tk.Frame(frame_texto)
        frame_precio.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_precio, text="Precio").pack(side=tk.LEFT)
        tk.Entry(frame_precio, textvariable=self.precio).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        items.BotonEstandar(frame_texto, "Crear objeto", self.crear_obj).pack(side=tk.TOP, fill=tk.X)


    def crear_obj(self):
        if not self.comprobar_campos():
            return
        if self.controlador.crear_obj(self.nombre.get(), self.descripcion.get(), self.tipo.get(),
                                          self.precio.get(), self.modificador.get()):
            mb.showinfo("Objeto creado",f"{self.nombre.get()} se ha creado correctamente")
            self.destroy()

        #
        # if self.controlador.crear_personaje(
        #     self.nombre_pj.get(),
        #     self.tipo,
        #     self.jugador.get(),
        #     self.descripcion.get(),
        #     dic_caracteristicas,
        #     self.pv.get()
        # ):
        #     mb.showinfo("Personaje creado",f"{self.nombre_pj.get()} se ha creado correctamente")
        #     self.destroy()
        # else:
        #     mb.showerror("ERROR",f"{self.nombre_pj.get()} ya existe",)

    def comprobar_campos(self):
        if self.nombre.get().strip(" ") == "":
            mb.showerror("ERROR", f"El nombre no puede estar vacío",)
            return False
        try:
            precio = float(self.precio.get())
        except tk.TclError:
            mb.showerror("ERROR", f"El precio tiene que ser un número",)
            return False
        if self.descripcion.get().strip(" ") == "":
            mb.showerror("ERROR", f"La descripcion no puede estar vacío",)
            return False
        return True

