import tkinter as tk
from tkinter import messagebox as mb

from interfaz import items
from interfaz.formulario import Formulario
import constantes as cons

class FormularioVerPJ(Formulario):
    def __init__(self, contenedor, controlador, pj):
        super().__init__(contenedor,  controlador)
        self.dic_modificadores = {}
        self.dic_caracteristicas_spin = {}
        self.pj = pj
        self.pv_actual = tk.IntVar()
        self.cargarwidgets()
        self.resizable(False, False)
        self.actualizacion_periodica()

    def cargarwidgets(self):
        imagen = tk.PhotoImage(file="constantes/silueta.png")
        label = tk.Label(self, image=imagen)
        label.image = imagen
        label.pack(side=tk.LEFT)

        frame_texto = tk.Frame(self)
        frame_texto.pack(side=tk.TOP ,padx=10 ,fill=tk.BOTH ,expand=True)

        frame_nombre = tk.Frame(frame_texto)
        frame_nombre.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_nombre, text="Nombre: ").pack(side=tk.LEFT)
        tk.Label(frame_nombre, text=self.pj.nombre).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_jugador = tk.Frame(frame_texto)
        frame_jugador.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_jugador, text="Jugador: ").pack(side=tk.LEFT)
        tk.Label(frame_jugador, text=self.pj.jugador).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_descripcion = tk.Frame(frame_texto)
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_descripcion, text="Descripcion: ").pack(side=tk.LEFT)
        tk.Label(frame_descripcion, text=self.pj.descripcion).pack(side=tk.RIGHT, fill=tk.X, padx=2, expand=True)

        frame_variables1 = tk.Frame(frame_texto)
        frame_variables1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_caracteristicas = tk.LabelFrame(frame_variables1, text="Caracteristicas")
        frame_caracteristicas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        columna, fila = 0, 0
        for caracteristica in self.pj.caracteristicas.keys():
            frame = tk.Frame(frame_caracteristicas)
            frame.grid(column=columna, row=fila)
            tk.Label(frame,text=caracteristica, width=5).grid(column=0,row=0)
            tk.Label(frame,text=self.pj.caracteristicas[caracteristica], width=2).grid(column=1,row=0)
            if fila <1:
                fila+=1
            else:
                columna+=1
                fila=0

        frame_armadura = tk.Frame(frame_variables1)
        frame_armadura.pack(side=tk.LEFT, fill=tk.BOTH)
        tk.Label(frame_armadura,text="DEF").pack(side=tk.TOP,pady=10)
        tk.Label(frame_armadura,text=self.pj.defensa).pack(side=tk.TOP)


        frame_variables2 = tk.Frame(frame_texto)
        frame_variables2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_modificadores = tk.LabelFrame(frame_variables2, text="Modificadores")
        frame_modificadores.pack(side=tk.LEFT,fill=tk.X,expand=False,padx=0)
        columna, fila = 0, 0
        for modificador in self.pj.modificadores.keys():
            frame = tk.Frame(frame_modificadores)
            frame.grid(column=columna, row=fila)
            tk.Label(frame,text=modificador, width=5).grid(column=0,row=0)
            tk.Label(frame,text=self.pj.modificadores[modificador], width=2).grid(column=1,row=0)
            if fila <1:
                fila+=1
            else:
                columna+=1
                fila=0

        frame_vida = tk.Frame(frame_variables2)
        frame_vida.pack(side=tk.LEFT, fill=tk.BOTH)
        tk.Label(frame_vida,text="PV").pack(side=tk.TOP,pady=10)
        tk.Label(frame_vida,textvariable=self.pv_actual).pack(side=tk.TOP)

        frame_botones = tk.Frame(self)
        frame_botones.pack(side=tk.TOP ,padx=10 ,pady=10 ,fill=tk.BOTH ,expand=True)

        items.BotonEstandar(frame_botones,"ATACAR",lambda: self.controlador.abrir_menu_ataque(self, self.pj)
                            ).pack(side=tk.LEFT ,padx=10 ,fill=tk.X ,expand=True)
        items.BotonEstandar(frame_botones,"OBJETOS",lambda: self.controlador.abrir_menu_objetos(self, self.pj)
                            ).pack(side=tk.LEFT ,padx=10 ,fill=tk.X ,expand=True)


    def actualizacion_periodica(self):
        self.pj = self.controlador.personajes[self.pj.id]
        self.pv_actual.set(self.pj.pv_actual)
        self.after(1000,self.actualizacion_periodica)


