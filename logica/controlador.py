import json
from pathlib import Path
from constantes import estilos
from interfaz.form_ataque import FormularioAtacar
from interfaz.form_mod_pj import FormularioModPJ
from interfaz.ventana_tutorial import Tutorial
from logica import util, util_bbdd
import tkinter as tk
from datos.personajes import Personaje

from interfaz.ventana import Ventana
from interfaz.form_manejarpj import FormularioVerPJ


class Controlador:
    def __init__(self):
        self.ventana = None
        self.campagnas = None
        self.ruta_miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json") # En el json se guarda la campaña en uso
        self.config = None
        self.nombre_master = ""
        self.campagna = ""
        self.personajes = {} # TODOS LOS PERSONAJES
        self.aliados = {}
        self.enemigos = {}
        self.historial = None # Este es el fichero del historial
        self.cuadro_historial = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_personajes = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_aliados = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_enemigos = None
        self.arranque()


    def arranque(self):
        self.inicializar()
        self.arranque_bbdd() # crear las bases de datos si no existen
        self.ruta_miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json")
        if not self.ruta_miscelanea.exists() or not self.ruta_miscelanea.is_dir():
            self.ruta_miscelanea.mkdir()
            print("Se ha creado la carpeta miscelanea")
        if not self.ruta_config.exists() or not self.ruta_config.is_file() or self.ruta_config.stat().st_size==0:
            self.primer_uso()
        self.continuar_arranque()
        self.ventana = Ventana(self)  # Defino la ventana principal
        self.cargar_historial()
        self.actualizar_listas()
        self.listbox_personajes.bind("<<ListboxSelect>>", self.abrir_ventana_pj)
        self.listbox_elem_aliados.bind("<<ListboxSelect>>", self.abrir_ventana_mod_pj)
        self.listbox_elem_enemigos.bind("<<ListboxSelect>>", self.abrir_ventana_mod_pj)

        self.ventana.mainloop()

    def rearranque(self, campagna, master):
        self.campagna = campagna
        print("rearanque ", campagna)
        self.master = master
        datos_config = {"nombre": master, "campagna": campagna }
        self.escribir_config_ra(datos_config)
        self.ventana.destroy()
        self.arranque()

    def arranque_bbdd(self):
        util_bbdd.crear_tabla_personajes()
        util_bbdd.crear_tabla_campa()

    def primer_uso(self):
        self.ruta_config.touch()
        tutorial = Tutorial(self)
        tutorial.mainloop() # Esto lleva a escribir_config() con el nombre y la campaña

    def escribir_config(self, datos_config):
        datos_config["historial"] = self.define_ruta_historial(datos_config["campagna"])
        if not util_bbdd.insertar_campa(datos_config):
            return False
        with self.ruta_config.open("w", encoding="utf-8") as conf:
            print("dc",datos_config)
            json.dump(datos_config, conf)
            print(self.config)
        return True # Esto lleva a continuar_arranque

    def escribir_config_ra(self, datos_config):
        datos_config["historial"] = self.define_ruta_historial(datos_config["campagna"])
        with self.ruta_config.open("w", encoding="utf-8") as conf:
            print("dc",datos_config)
            json.dump(datos_config, conf)
            print(self.config)
        return True

    def continuar_arranque(self):
        self.cargar_config() # Rellena los campos self.campagna y self.nombre_master desde el json
        self.define_ruta_historial(self.campagna)
        if not self.historial.exists() or not self.historial.is_file():
            self.historial.touch()
        # Desde aquí sigue con la creación de la ventana

    def define_ruta_historial(self,campagna):
        ruta_historial = f"miscelanea/historial_{campagna}.txt"
        self.historial = Path(ruta_historial)
        return ruta_historial

    def cargar_historial(self):
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

    def actualizar_listas(self):
        self.actualizar_lista_pers()

    def actualizar_lista_pers(self):
        self.obtener_personajes()
        self.obtener_aliados()
        self.obtener_enemigos()
        self.listbox_personajes.actualizar(self.personajes)
        try:
            self.listbox_elem_aliados.actualizar(self.aliados)
        except AttributeError:
            pass
        try:
            self.listbox_elem_enemigos.actualizar(self.enemigos)
        except AttributeError:
            pass
    def obtener_personajes(self):
        self.personajes = {}
        print(f"Estoy en campaña {self.campagna}")
        lista_personajes = util_bbdd.leer_personajes(self.campagna)
        for tupla in lista_personajes:
            nombre = tupla[1]
            tipo = tupla[3]
            jugador = tupla[4]
            descripcion = tupla[2]
            nivel = tupla[5]
            pv = tupla[6]
            campagna = tupla[13]
            caracteristicas = {"FUE": tupla[7], "CON": tupla[8], "SAB": tupla[9], "INT": tupla[10], "DES": tupla[11],
                               "CAR": tupla[12]}
            personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, campagna, nivel)
            self.personajes[personaje.id] = personaje

    def obtener_aliados(self):
        self.aliados = {}
        print(f"Estoy en campaña {self.campagna}")
        lista_personajes = util_bbdd.leer_aliados(self.campagna)
        for tupla in lista_personajes:
            nombre = tupla[1]
            tipo = tupla[3]
            jugador = tupla[4]
            descripcion = tupla[2]
            nivel = tupla[5]
            pv = tupla[6]
            campagna = tupla[13]
            caracteristicas = {"FUE": tupla[7], "CON": tupla[8], "SAB": tupla[9], "INT": tupla[10], "DES": tupla[11],
                               "CAR": tupla[12]}
            personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, campagna, nivel)
            self.aliados[personaje.id] = personaje

    def obtener_enemigos(self):
        self.enemigos = {}
        print(f"Estoy en campaña {self.campagna}")
        lista_personajes = util_bbdd.leer_enemigos(self.campagna)
        for tupla in lista_personajes:
            nombre = tupla[1]
            tipo = tupla[3]
            jugador = tupla[4]
            descripcion = tupla[2]
            nivel = tupla[5]
            pv = tupla[6]
            campagna = tupla[13]
            caracteristicas = {"FUE": tupla[7], "CON": tupla[8], "SAB": tupla[9], "INT": tupla[10], "DES": tupla[11],
                               "CAR": tupla[12]}
            personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, campagna, nivel)
            self.enemigos[personaje.id] = personaje

    def recuperar_info_campas(self):
        campagnas = util_bbdd.leer_campas()
        return campagnas


    def cargar_config(self):
        with self.ruta_config.open("r", encoding="utf-8") as conf:
                config = json.load(conf)
                self.nombre_master = config["nombre"]
                self.campagna = config["campagna"]

    def crear_personaje(self, nombre, tipo, jugador, descripcion, caracteristicas, pv):
        personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, self.campagna)
        if util_bbdd.insertar_personaje(personaje):
            self.escribir_en_historial(f" Ha nacido {personaje.to_string()}")
            self.actualizar_listas()
            return True
        else: return False

    def modificar_personaje(self, id_antiguo, nombre, tipo, jugador, descripcion, caracteristicas, pv):
        self.borrar_personaje(id_antiguo)
        personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, self.campagna)
        if util_bbdd.insertar_personaje(personaje):
            self.escribir_en_historial(f" Se ha modificado la ficha de: {nombre}")
            self.actualizar_listas()
            return True
        else: return False

    def borrar_personaje(self, id_antiguo):
        if util_bbdd.borrar_personaje(id_antiguo):
            self.escribir_en_historial(f" Se ha borrado la ficha de: {id_antiguo}")
            self.actualizar_listas()
            return True
        else: return False

    def muestra_pantalla(self, ventana, pantalla):
        pantalla = ventana.pantallas[pantalla]
        pantalla.tkraise()

    def abrir_ventana_pj(self, event):
        # listbox = event.widget
        personaje = self.listbox_personajes.get_seleccion()
        try:
            FormularioVerPJ(self.ventana, self, self.personajes[personaje])
        except KeyError:
            pass

    def abrir_ventana_mod_pj(self, event):
        # listbox = event.widget
        try:
            personaje = self.listbox_elem_aliados.get_seleccion()
            FormularioModPJ(self.ventana, self, self.personajes[personaje])
        except KeyError:
            pass
        try:
            personaje = self.listbox_elem_enemigos.get_seleccion()
            FormularioModPJ(self.ventana, self, self.enemigos[personaje])
        except KeyError:
            pass

    def abrir_menu_ataque(self, formulario_pj, pj):
        FormularioAtacar(formulario_pj, self, pj)

    def ataque(self, atacante, objetivo, arma):
        atacante.atacar(objetivo,arma)


    def abrir_menu_objetos(self):
        pass

    def inicializar(self):
        self.ventana = None
        self.campagnas = None
        self.ruta_miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json") # En el json se guarda la campaña en uso
        self.config = None
        self.nombre_master = ""
        self.campagna = ""
        self.personajes = {} # TODOS LOS PERSONAJES
        self.aliados = {}
        self.enemigos = {}
        self.historial = None # Este es el fichero del historial
        self.cuadro_historial = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_personajes = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_aliados = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_enemigos = None

