import tkinter as tk
from tkinter import messagebox as mb, ttk
import constantes as cons
from interfaz import items
from interfaz.formulario import Formulario
from logica import util


class FormularioModObj(Formulario):
    def __init__(self, contenedor, controlador, objeto):
        super().__init__(contenedor,  controlador)
        self.objeto = objeto
        print(self.objeto)
        self.nombre_ant = self.objeto.nombre
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
        entry_nombre = tk.Entry(frame_nombre, textvariable=self.nombre)
        entry_nombre.pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)
        print(self.objeto.nombre)
        entry_nombre.insert(0,self.objeto.nombre)

        frame_descripcion = tk.Frame(frame_texto)
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_descripcion, text="Descripción").pack(side=tk.TOP)
        desc = tk.Entry(frame_descripcion, textvariable=self.descripcion)
        desc.pack(side=tk.TOP, fill=tk.BOTH, padx=2, expand=True)
        desc.insert(0,self.objeto.descripcion)

        frame_tipo = tk.Frame(frame_texto)
        frame_tipo.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_tipo, text="Tipo").pack(side=tk.LEFT)
        desplegable = ttk.Combobox(frame_tipo, values=cons.tipos_objetos, state="readonly", textvariable=self.tipo)
        desplegable.pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)
        desplegable.set(self.objeto.tipo)

        frame_modificador = tk.Frame(frame_texto)
        frame_modificador.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_modificador, text="Modificador").pack(side=tk.LEFT)
        spinbox = tk.Spinbox(
            frame_modificador,
            from_=-10,
            to=10,
            increment=1,
            width=1,
            textvariable=self.modificador
        )
        spinbox.pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)
        self.modificador.set(self.objeto.modificador)

        frame_precio = tk.Frame(frame_texto)
        frame_precio.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_precio, text="Precio").pack(side=tk.LEFT)
        precio = tk.Entry(frame_precio, textvariable=self.precio)
        precio.pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)
        self.precio.set(self.objeto.precio)

        items.BotonEstandar(frame_texto, "Modificar objeto", self.modificar_obj).pack(side=tk.TOP, fill=tk.X)
        borrar = items.BotonEstandar(frame_texto, "Borrar Objeto", self.eliminar_objeto)
        borrar.config(background="red")
        borrar.pack(
            side=tk.TOP,
            fill=tk.X,
            pady=5
        )

    def modificar_obj(self):
        if not self.comprobar_campos():
            return
        if self.controlador.modificar_obj(self.nombre.get(), self.descripcion.get(), self.tipo.get(),
                                          self.precio.get(), self.modificador.get(), self.nombre_ant):
            mb.showinfo("Objeto modificado",f"{self.nombre.get()} se ha modificado correctamente")
            self.destroy()

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

    def eliminar_objeto(self):
        if not mb.askokcancel("PELIGRO", f"¿Seguro que quieres borrar {self.objeto.nombre}?"):
            mb.showinfo(f"Mantienes {self.objeto.nombre} en todos los inventarios")
            return
        else:
            if self.controlador.borrar_objeto(self.objeto):
                mb.showwarning("INFO",f"{self.objeto.nombre} ha sido borrado de todos los inventarios")
                self.destroy()
            else:
                mb.showwarning("ERROR", f"{self.objeto.nombre} no se ha podido borrar")