import json
from pathlib import Path
from constantes import estilos
from datos.objetos import Objeto
from interfaz.form_ataque import FormularioAtacar
from interfaz.form_mod_pj import FormularioModPJ
from interfaz.form_objetos import FormularioObjetos
from interfaz.ventana_tutorial import Tutorial
from logica import util, util_bbdd
import tkinter as tk
from datos.personajes import Personaje
from interfaz.ventana import Ventana
from interfaz.form_manejarpj import FormularioVerPJ


class Controlador:
    def __init__(self):
        # Elementos graficos
        self.ventana = None
        self.cuadro_historial = None
        self.listbox_personajes = None
        self.listbox_elem_aliados = None
        self.listbox_elem_enemigos = None
        self.listbox_elem_objetos = None


        self.config = None
        self.historial = None # Objeto tipo Path()
        self.ruta_miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json") # En el json se guarda la campaña en uso
        self.nombre_master = ""
        self.campagna = ""
        self.personajes = {} # TODOS LOS PERSONAJES
        self.aliados = {}
        self.enemigos = {}
        self.objetos = {}

        self.arranque()

    # Metodos de inicio
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
        self.escribir_config_rearranque(datos_config)
        self.ventana.destroy()
        self.arranque()

    def arranque_bbdd(self):
        util_bbdd.crear_tabla_personajes()
        util_bbdd.crear_tabla_campa()
        util_bbdd.crear_tabla_objetos()

    def inicializar(self):
        self.ventana = None
        self.ruta_miscelanea = Path("miscelanea")
        self.ruta_config = Path("miscelanea/config.json") # En el json se guarda la campaña en uso
        self.nombre_master = ""
        self.campagna = ""
        self.personajes = {} # TODOS LOS PERSONAJES
        self.aliados = {}
        self.enemigos = {}
        self.objetos = {}
        self.config = None
        self.historial = None # Este es el fichero del historial
        self.cuadro_historial = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_personajes = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_aliados = None  # Esto va a ser util para actualizar desde cualquier sitio
        self.listbox_elem_enemigos = None
        self.listbox_elem_objetos = None


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

    def escribir_config_rearranque(self, datos_config):
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

    def cargar_config(self):
        with self.ruta_config.open("r", encoding="utf-8") as conf:
                config = json.load(conf)
                self.nombre_master = config["nombre"]
                self.campagna = config["campagna"]

    # Metodos intermediarios con base de datos
    def recuperar_info_campas(self):
        campagnas = util_bbdd.leer_campas()
        return campagnas

    def recuperar_info_obj(self):
        campagnas = util_bbdd.recuperar_objetos(self.objetos)
        return campagnas

    def crear_personaje(self, nombre, tipo, jugador, descripcion, caracteristicas, pv):
        personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, self.campagna)
        if util_bbdd.insertar_personaje(personaje):
            self.escribir_en_historial(f" Ha nacido {personaje.to_string()}")
            self.actualizar_listas()
            return True
        else: return False

    def crear_obj(self, nombre,descripcion, tipo, precio, modificador):
        objeto = Objeto(self.campagna, nombre, "comun", descripcion, tipo, precio, modificador)
        if util_bbdd.insertar_objeto(objeto):
            self.escribir_en_historial(f" Creado objeto: {objeto.nombre} del tipo:  {objeto.tipo}")
            self.actualizar_listas()
            return True
        else: return False

    def dar_obj(self, objeto, pj):
        objeto.personaje = pj.id
        if util_bbdd.insertar_objeto(objeto):
            self.escribir_en_historial(f" Creado objeto: {objeto.nombre} del tipo:  {objeto.tipo}")
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

    def modificar_personaje_con_pj(self, pj):
        self.borrar_personaje(pj.id)
        if util_bbdd.insertar_personaje(pj):
            self.actualizar_listas()
            return True
        else: return False

    def borrar_personaje(self, id_antiguo):
        if util_bbdd.borrar_personaje(id_antiguo):
            # self.escribir_en_historial(f" Se ha borrado la ficha de: {id_antiguo}")
            self.actualizar_lista_pers()
            return True
        else: return False

    def cargar_dicc_personajes(self):
        self.personajes = {}
        lista_pers = self.obtener_personajes()
        for personaje in lista_pers:
            self.personajes[personaje.id] = personaje

    def cargar_dicc_aliados(self):
        self.aliados = {}
        lista_pers = self.obtener_aliados()
        for personaje in lista_pers:
            self.aliados[personaje.id] = personaje

    def cargar_dicc_enemigos(self):
        self.enemigos = {}
        lista_pers = self.obtener_enemigos()
        for personaje in lista_pers:
            self.enemigos[personaje.id] = personaje

    def cargar_dicc_objetos(self):
        self.objetos = {}
        lista_objs = self.obtener_objetos()
        for objeto in lista_objs:
            self.objetos[objeto.nombre] = objeto

    def obtener_personajes(self):
        lista_bruta = util_bbdd.recuperar_personajes(self.campagna)
        print(lista_bruta)
        return util.traducir_resultado_bbdd(lista_bruta)

    def obtener_aliados(self):
        lista_bruta = util_bbdd.recuperar_aliados(self.campagna)
        return util.traducir_resultado_bbdd(lista_bruta)

    def obtener_enemigos(self):
        lista_bruta = util_bbdd.recuperar_enemigos(self.campagna)
        return util.traducir_resultado_bbdd(lista_bruta)

    def obtener_armas(self, id_personaje):
        lista = util_bbdd.recuperar_armas(self.personajes[id_personaje])
        return lista

    def obtener_objetos(self):
        lista = util_bbdd.recuperar_objetos(self.campagna)
        return util.traducir_objeto_bbdd(lista)

    def obtener_objetos_pj(self, pj):
        lista = util_bbdd.recuperar_objetos(self.campagna, pj.id)
        return util.traducir_objeto_bbdd(lista)


    # Metodos graficos
    def cambiar_pantalla(self, ventana, pantalla):
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

    def abrir_menu_objetos(self, formulario_pj, pj):
        FormularioObjetos(formulario_pj,self, pj)

    def escribir_en_historial(self, msj):
        msj = util.crear_mensaje(msj)
        with self.historial.open("a", encoding="utf-8") as his:
            his.write(msj)
        self.cuadro_historial.configure(state=tk.NORMAL)
        self.cuadro_historial.insert(0.0,msj)
        self.cuadro_historial.configure(state=tk.DISABLED)

    def actualizar_listas(self):
        self.actualizar_lista_pers()
        self.actualizar_lista_objs()

    def actualizar_lista_pers(self):
        self.cargar_dicc_personajes()
        self.cargar_dicc_aliados()
        self.cargar_dicc_enemigos()
        self.listbox_personajes.actualizar(self.personajes)
        try:
            self.listbox_elem_aliados.actualizar(self.aliados)
        except AttributeError:
            pass
        try:
            self.listbox_elem_enemigos.actualizar(self.enemigos)
        except AttributeError:
            pass

    def actualizar_lista_objs(self):
        self.cargar_dicc_objetos()
        try:
            self.listbox_elem_objetos.actualizar(self.objetos)
        except AttributeError:
            pass

    # Metodos intermediarios entre objetos
    def ataque(self, atacante, objetivo, arma):
        try:
            ataque, dagno, mensaje = atacante.atacar(objetivo,self.objetos[arma])
            self.escribir_en_historial(mensaje)
            mensaje = objetivo.recibir_ataque(ataque,dagno)
            self.escribir_en_historial(mensaje)
            self.modificar_personaje_con_pj(objetivo)
            return True
        except:
            return False
