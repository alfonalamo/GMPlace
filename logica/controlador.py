import json
from pathlib import Path
import constantes as cons
from interfaz.tutorial import Tutorial
from logica import util, util_bbdd
import tkinter as tk
from datos.personajes import Personaje

from interfaz.ventana import Ventana


class Controlador:
    def __init__(self):

        self.ruta_config = Path("miscelanea/config.json")
        self.nombre_master = ""
        self.campagna = ""
        self.personajes = {} # Un diccionario id:Personaje
        self.historial = None # Este es el fichero del historial
        self.cuadro_historial = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_personajes = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.config = None
        self.arranque()
        self.ventana = Ventana(self)  # Defino la ventana principal
        self.gestionar_historial()
        self.ventana.mainloop()

    def muestra_pantalla(self, ventana, pantalla):
        pantalla = ventana.pantallas[pantalla]
        pantalla.tkraise()

    def gestionar_historial(self):
        self.historial = self.crear_archivo_historial()
        with self.historial.open("r", encoding="utf-8") as his:
            for linea in his:
                self.cuadro_historial.insert(0.0,linea)
        self.cuadro_historial.configure(state=tk.DISABLED)

    def escribir_en_historial(self, msj):
        msj = util.crear_mensaje(msj)
        with self.historial.open("a", encoding="utf-8") as his:
            his.write(msj)
        self.cuadro_historial.configure(state=tk.NORMAL)
        self.cuadro_historial.insert(0.0,msj)
        self.cuadro_historial.configure(state=tk.DISABLED)

    def crear_archivo_historial(self):
        miscelanea = Path("miscelanea")
        historial = Path("miscelanea/historial.txt")
        if not miscelanea.exists() or not miscelanea.is_dir():
            miscelanea.mkdir()
            print("Se ha creado la carpeta miscelanea")
        if not historial.exists() or not historial.is_file():
            historial.touch()
            print("Se ha creado el fichero de historial")
        return historial

    def crear_personaje(self, nombre, tipo, jugador, descripcion, caracteristicas):
        personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas)
        if util_bbdd.insertar_personaje(personaje):
            self.escribir_en_historial(f" Ha nacido {personaje.to_string()}")
            self.actualizar_lista_personajes()
            return True
        else: return False

    def obtener_personajes(self):
        lista_personajes = util_bbdd.leer_personajes()
        for tupla in lista_personajes:
            nombre = tupla[1]
            tipo = tupla[3]
            jugador = tupla[4]
            descripcion = tupla[2]
            nivel = tupla[5]
            caracteristicas = {"FUE": tupla[7], "CON": tupla[8], "SAB": tupla[9], "INT": tupla[10], "DES": tupla[11],
                               "CAR": tupla[12]}
            personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, nivel)
            self.personajes[personaje.id] = personaje

    def arranque(self):
        self.arranque_bbdd()
        miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json")
        if not miscelanea.exists() or not miscelanea.is_dir():
            miscelanea.mkdir()
            print("Se ha creado la carpeta miscelanea")
        if not self.ruta_config.exists() or not self.ruta_config.is_file() or self.ruta_config.stat().st_size==0:
            self.ruta_config.touch()
            tutorial = Tutorial(self)
            tutorial.mainloop()

        with self.ruta_config.open("r", encoding="utf-8") as conf:
                self.config = json.load(conf)
                print(self.config)


        self.nombre_master = self.config["nombre"]
        self.campagna = self.config["campagna"]

    def escribir_config(self, datos_config):
        with self.ruta_config.open("w", encoding="utf-8") as conf:
            print("dc",datos_config)
            json.dump(datos_config, conf)
            print(self.config)

    def actualizar_lista_personajes(self):
        self.listbox_personajes.delete(0,tk.END)
        self.obtener_personajes()
        try:
            for personaje in self.personajes.values():
                self.listbox_personajes.insert(tk.END, personaje.nombre)
        except AttributeError:
            print("dsandsla", self.personajes)
            pass

    def arranque_bbdd(self):
        util_bbdd.crear_tabla_personajes()
