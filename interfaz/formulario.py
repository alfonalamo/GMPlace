import tkinter as tk
from tkinter import messagebox as mb
from typing import Type
import constantes as cons
from constantes import estilos
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
        self.nombre_pj = tk.StringVar()
        self.jugador = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.cargawidgets()
        self.resizable(False, False)


    def cargawidgets(self):
        imagen = tk.PhotoImage(file="constantes/silueta.png")
        label = tk.Label(self, image=imagen)
        label.image = imagen
        label.pack(side=tk.LEFT)

        frame_texto = tk.Frame(self)

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

        frame_jugador = tk.Frame(frame_texto)
        tk.Label(frame_jugador, text="Jugador").pack(side=tk.LEFT)
        tk.Entry(
            frame_jugador,
            textvariable=self.jugador,
        ).pack(
            side=tk.RIGHT,
            fill=tk.X,
            padx=2,
            expand=True
        )
        frame_jugador.pack(side=tk.TOP, fill=tk.X)

        frame_descripcion = tk.Frame(frame_texto)
        tk.Label(frame_descripcion, text="Descripción").pack(side=tk.TOP)
        tk.Entry(
            frame_descripcion,
            textvariable=self.descripcion,
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            padx=2,
            expand=True
        )
        frame_descripcion.pack(side=tk.TOP, fill=tk.X)


        frame_caracteristicas = tk.LabelFrame(frame_texto, text="Caracteristicas")
        columna=0
        fila=0
        self.dic_caracteristicas_spin = {}
        for caracteristica in cons.caracteristicas.keys():
            frame = tk.Frame(frame_caracteristicas)
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

        frame_modificadores = tk.LabelFrame(frame_variables, text="Modificadores")
        columna=0
        fila=0
        self.dic_modificadores = {}
        for caracteristica in cons.caracteristicas.keys():
            frame = tk.Frame(frame_modificadores)
            tk.Label(frame,text=caracteristica, width=5).grid(column=0,row=0)
            self.dic_modificadores[caracteristica] = tk.IntVar()
            tk.Label(
                frame,
                textvariable=self.dic_modificadores[caracteristica]
            ).grid(column=1,row=0)

            frame.grid(column=columna, row=fila)
            if fila <1:
                fila+=1
            else:
                columna+=1
                fila=0

        frame_modificadores.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=False,
            padx=0
        )

        def calcular_modificadores():
            for clave in self.dic_modificadores.keys():
                self.dic_modificadores[clave].set(util.calcular_modificador(self.dic_caracteristicas_spin[clave].get()))
            frame_modificadores.after(100,calcular_modificadores)

        calcular_modificadores()

        frame_armadura = tk.Frame(frame_variables)
        ca = tk.IntVar(frame_armadura)

        def calcular_ca():
            ca.set(util.calcular_ca(self.dic_caracteristicas_spin["CON"].get()))
            frame_armadura.after(100,calcular_ca)

        calcular_ca()
        tk.Label(frame_armadura,text="DEF").pack(side=tk.TOP,pady=10)
        tk.Label(frame_armadura,textvariable=ca).pack(side=tk.TOP)
        frame_armadura.pack(side=tk.LEFT, fill=tk.BOTH)

        frame_vida = tk.Frame(frame_variables)
        vida_max = tk.IntVar(frame_vida)

        def calcular_vida():
            vida_max.set(util.calcular_pv(self.dic_caracteristicas_spin["CON"].get()))
            frame_vida.after(100,calcular_vida)

        calcular_vida()

        tk.Label(frame_vida,text="PV").pack(side=tk.TOP,pady=10)
        tk.Label(frame_vida,textvariable=vida_max).pack(side=tk.TOP)
        frame_vida.pack(side=tk.LEFT, fill=tk.BOTH)

        frame_variables.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        tk.Button(
            frame_texto,
            text="Crear personaje",
            command= self.crear_personaje,
            background=estilos.Color.FONDO,
            activebackground=estilos.Color.COMPONENTE,
            activeforeground=estilos.Color.TEXTO_BLANCO
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            pady=5
        )

        frame_texto.pack(
            side=tk.LEFT,
            padx=10,
            fill=tk.BOTH,
            expand=True
        )

    def crear_personaje(self):
        if not self.comprobar_campos():
            return
        dic_caracteristicas = {}
        for clave,valor in self.dic_caracteristicas_spin.items():
            dic_caracteristicas[clave] = int(valor.get())

        if self.controlador.crear_personaje(
            self.nombre_pj.get(),
            "pj",
            self.jugador.get(),
            self.descripcion.get(),
            dic_caracteristicas
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


