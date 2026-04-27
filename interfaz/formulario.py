import tkinter as tk
from tkinter import StringVar
from typing import Type
import constantes as cons
from logica import util


class Formulario(tk.Toplevel):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor)
        self.contenedor = contenedor
        self.controlador = controlador

    def cargawidgets(self):
        pass

class FormularioPJ(Formulario):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor,  controlador)
        self.nombre_pj = tk.StringVar
        self.cargawidgets()
        self.resizable(False, False)


    def cargawidgets(self):
        imagen = tk.PhotoImage(file="constantes/silueta.png")
        label = tk.Label(self, image=imagen)
        label.image = imagen

        label.pack(side=tk.LEFT)
        frame_texto = tk.Frame(self, background="red")
        frame_nombre = tk.Frame(frame_texto)
        tk.Label(frame_nombre, text="Nombre").pack(side=tk.LEFT)
        tk.Entry(
            frame_nombre,
            textvariable=self.nombre_pj,
        ).pack(
            side=tk.RIGHT,
            fill=tk.X,
            padx=2,
            expand=True
        )
        frame_nombre.pack(side=tk.TOP, fill=tk.X)

        frame_caracteristicas = tk.Frame(frame_texto)
        columna=0
        fila=0
        self.dic_caracteristicas_spin = {}
        for caracteristica in cons.caracteristicas.keys():
            print(caracteristica)
            frame = tk.Frame(frame_caracteristicas)
            tk.Label(frame,text=caracteristica, width=5).grid(column=0,row=0)
            self.dic_caracteristicas_spin[caracteristica] = tk.IntVar()
            tk.Spinbox(
                frame,
                from_=0,
                to=10,
                increment=1,
                width=2,
                textvariable=self.dic_caracteristicas_spin[caracteristica]
            ).grid(column=1,row=0)

            frame.grid(column=columna, row=fila)
            if fila <1:
                fila+=1
            else:
                columna+=1
                fila=0

        frame_caracteristicas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        frame_variables = tk.Frame(frame_texto)

        frame_armadura = tk.Frame(frame_variables)
        ca = tk.IntVar(frame_armadura)

        def calcular_ca():
            ca.set((self.dic_caracteristicas_spin["CON"].get())*3)
            frame_armadura.after(100,calcular_ca)

        tk.Label(frame_armadura,text="CA").pack(side=tk.TOP)
        tk.Label(frame_armadura,textvariable=ca).pack(side=tk.TOP)
        frame_armadura.pack(side=tk.LEFT, fill=tk.BOTH)

        frame_vida = tk.Frame(frame_variables)
        vida_max = tk.IntVar(frame_vida)
        def calcular_vida():
            vida_max.set((self.dic_caracteristicas_spin["CON"].get())*10)
            frame_vida.after(100,calcular_ca)

        calcular_vida()

        tk.Label(frame_vida,text="Vida").pack(side=tk.TOP)
        tk.Label(frame_vida,textvariable=ca).pack(side=tk.TOP)
        frame_vida.pack(side=tk.RIGHT, fill=tk.BOTH)

        frame_variables.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        tk.Button(
            frame_texto,
            text="Crear personaje",
            command= self.obtener_caracteristicas
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        frame_texto.pack(
            side=tk.LEFT,
            padx=10,
            fill=tk.BOTH,
            expand=True
        )

        # tk.Label(self, text="nombre").grid(
        #     column=1,
        #     row=0
        # )
        # tk.Entry(
        #     self,
        #     textvariable=self.nombre_pj
        # ).grid(
        #     column=2,
        #     row=0
        # )
        # tk.Label(self, text="Caracteristicas").grid(
        #     column=2,
        #     row=1
        # )

    def obtener_caracteristicas(self):
        for key,value in self.dic_caracteristicas_spin.items():
            print(key,value.get())