import tkinter as tk
from constantes import estilos
from interfaz import items
from interfaz.form_crearpj import FormularioCrearPJ, FormularioCrearEnemigo
from interfaz.pantalla import Pantalla
from interfaz.navegador import NavegadorLateral


class Elementos(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Elementos")
        categorias =  ("Personaje", "Enemigo", "Objeto")
        self.pantalla_activa = "Personaje" # La pantalla que se verá por defecto al inicio
        self.pantallas = {}
        self.contenedor_principal = tk.Frame(self)

        for categoria in categorias:
            pantalla = Subpantalla(self.contenedor_principal, self.controlador, categoria)
            self.pantallas[str(pantalla.nombre)] = pantalla

        controlador.muestra_pantalla(self, self.pantalla_activa)

        self.barra_navegacion = NavegadorLateral(self, self.controlador, self.pantallas.values())
        self.carga_widgets()


    def carga_widgets(self):
        self.barra_navegacion.pack(
            side= tk.LEFT,
            fill= tk.Y,
            expand= False,
            padx= 0,
            pady= 0
        )
        self.contenedor_principal.pack(
            side = tk.LEFT,
            fill = tk.BOTH,
            expand= True,
            padx= 0,
            pady= 0
        )
        self.contenedor_principal.configure(background=estilos.Color.FONDO)
        self.contenedor_principal.grid_columnconfigure(0, weight=1)
        self.contenedor_principal.grid_rowconfigure(0, weight=1)

class Subpantalla(Pantalla):
    def __init__(self, contenedor, controlador, nombre):
        super().__init__(contenedor, controlador, nombre)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.carga_widgets()

    def carga_widgets(self):
        nuevo_elemento = items.BotonEstandar(self, f"Crear {self.nombre}", self.abre_formulario)
        nuevo_elemento.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=5,
            pady=5)

        frame_lista = tk.Frame(self)
        frame_lista.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=10)

        self.carga_lista_especifica(frame_lista)
    def abre_formulario(self):
        if self.nombre == "Personaje":
            FormularioCrearPJ(self, self.controlador)
        elif self.nombre == "Enemigo":
            FormularioCrearEnemigo(self, self.controlador)
        else:
            toplevel = tk.Toplevel(
                self
            )
            tk.Label(toplevel,text="Formulario no creado aún, sorry").pack()
            tk.Button(toplevel, text="Cerrar", command=lambda: toplevel.destroy()).pack(fill=tk.X)

    def carga_lista_especifica(self, contenedor):
        if self.nombre == "Personaje":
            lista_elem_pers = items.ListBoxPersonajes(contenedor)
            lista_elem_pers.pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True
            )
            self.controlador.listbox_elem_aliados = lista_elem_pers
        elif self.nombre == "Enemigo":
            lista_elem_enemigos = items.ListBoxPersonajes(contenedor)
            lista_elem_enemigos.pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True
            )
            self.controlador.listbox_elem_enemigos = lista_elem_enemigos