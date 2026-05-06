import tkinter as tk
from tkinter import messagebox as mb
import constantes as cons
from interfaz import items
from interfaz.formulario import Formulario
from logica import util


class FormularioCrearPJ(Formulario):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.tipo = "pj"
        self.dic_modificadores = {}
        self.dic_caracteristicas_spin = {}
        self.nombre_pj = tk.StringVar()
        self.jugador = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.pv = tk.IntVar()
        self.ca = tk.IntVar()
        self.cargawidgets()
        self.resizable(False, False)
        self.actualizacion_periodica()

    def cargawidgets(self):
        imagen = tk.PhotoImage(file="constantes/silueta.png")
        label = tk.Label(self, image=imagen)
        label.pack(side=tk.LEFT)
        label.image = imagen

        frame_texto = tk.Frame(self)
        frame_texto.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        frame_nombre = tk.Frame(frame_texto)
        frame_nombre.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_nombre, text="Nombre").pack(side=tk.LEFT)
        tk.Entry(frame_nombre, textvariable=self.nombre_pj).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_jugador = tk.Frame(frame_texto)
        tk.Label(frame_jugador, text="Jugador").pack(side=tk.LEFT)
        tk.Entry(frame_jugador, textvariable=self.jugador).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)
        frame_jugador.pack(side=tk.TOP, fill=tk.X)

        frame_descripcion = tk.Frame(frame_texto)
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_descripcion, text="Descripción").pack(side=tk.TOP)
        tk.Entry(frame_descripcion, textvariable=self.descripcion).pack(side=tk.TOP, fill=tk.BOTH, padx=2, expand=True)

        frame_caracteristicas = tk.LabelFrame(frame_texto, text="Caracteristicas")
        frame_caracteristicas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        columna, fila = 0, 0
        for caracteristica in cons.caracteristicas.keys():
            frame = tk.Frame(frame_caracteristicas)
            frame.grid(column=columna, row=fila)
            tk.Label(frame,text=caracteristica, width=5).grid(column=0,row=0)

            self.dic_caracteristicas_spin[caracteristica] = tk.IntVar()
            tk.Spinbox(
                frame,
                from_=0,
                to=20,
                increment=1,
                width=2,
                textvariable=self.dic_caracteristicas_spin[caracteristica]
            ).grid(column=1,row=0)
            self.dic_caracteristicas_spin[caracteristica].set(10)
            if fila <1: fila+=1
            else:
                columna+=1
                fila=0

        frame_variables = tk.Frame(frame_texto)
        frame_variables.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_modificadores = tk.LabelFrame(frame_variables, text="Modificadores")
        frame_modificadores.pack(side=tk.LEFT,fill=tk.X,expand=False,padx=0)
        columna, fila = 0, 0
        for caracteristica in cons.caracteristicas.keys():
            frame = tk.Frame(frame_modificadores)
            frame.grid(column=columna, row=fila)
            tk.Label(frame,text=caracteristica, width=5).grid(column=0,row=0)
            self.dic_modificadores[caracteristica] = tk.IntVar()
            tk.Label(frame,textvariable=self.dic_modificadores[caracteristica]).grid(column=1,row=0)
            if fila <1:
                fila+=1
            else:
                columna+=1
                fila=0

        frame_armadura = tk.Frame(frame_variables)
        frame_armadura.pack(side=tk.LEFT, fill=tk.BOTH)
        tk.Label(frame_armadura,text="DEF").pack(side=tk.TOP,pady=10)
        tk.Label(frame_armadura,textvariable=self.ca).pack(side=tk.TOP)

        frame_vida = tk.Frame(frame_variables)
        frame_vida.pack(side=tk.LEFT, fill=tk.BOTH)
        tk.Label(frame_vida,text="PV").pack(side=tk.TOP,pady=10)
        tk.Label(frame_vida,textvariable=self.pv).pack(side=tk.TOP)

        items.BotonEstandar(frame_texto, "Crear personaje", self.crear_personaje
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            pady=5
        )

    def crear_personaje(self):
        if not self.comprobar_campos():
            return
        dic_caracteristicas = {}
        for clave,valor in self.dic_caracteristicas_spin.items():
            dic_caracteristicas[clave] = int(valor.get())

        if self.controlador.crear_personaje(
            self.nombre_pj.get(),
            self.tipo,
            self.jugador.get(),
            self.descripcion.get(),
            dic_caracteristicas,
            self.pv.get()
        ):
            mb.showinfo("Personaje creado",f"{self.nombre_pj.get()} se ha creado correctamente")
            self.destroy()
        else:
            mb.showerror("ERROR",f"{self.nombre_pj.get()} ya existe",)

    def comprobar_campos(self):
        if self.nombre_pj.get().strip(" ") == "":
            mb.showerror("ERROR", f"El nombre no puede estar vacío",)
            return False
        if self.jugador.get().strip(" ") == "":
            mb.showerror("ERROR", f"El jugador no puede estar vacío",)
            return False
        return True

    def actualizacion_periodica(self):
        self.calcular_modificadores()
        self.calcular_ca()
        self.calcular_vida()
        self.after(100,self.actualizacion_periodica)

    def calcular_modificadores(self):
        for clave in self.dic_modificadores.keys():
            self.dic_modificadores[clave].set(util.calcular_modificador(self.dic_caracteristicas_spin[clave].get()))

    def calcular_ca(self):
        self.ca.set(util.calcular_ca(self.dic_caracteristicas_spin["CON"].get()))

    def calcular_vida(self):
        self.pv.set(util.calcular_pv(self.dic_caracteristicas_spin["CON"].get()))

class FormularioCrearEnemigo(FormularioCrearPJ):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.tipo = "enemigo"