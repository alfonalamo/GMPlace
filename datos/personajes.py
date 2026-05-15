from abc import ABC
from logica import util

class Personaje:
    def __init__(self, nombre, tipo, jugador, descripcion, caracteristicas, pv, campagna, nivel=1):
        self.nombre = nombre.strip(" ") # Usar solo si da problemas los nombres con espacio
        self.tipo = tipo
        self.jugador = jugador
        self.descripcion = descripcion
        self.nivel = nivel
        self.caracteristicas = caracteristicas # Esto va a ser un diccionario
        self.modificadores = {}
        self.calcular_modificadores(caracteristicas)
        self.defensa = caracteristicas["CON"] # La CA, es decir, la dificultad de que le de un golpe
        self.pv_max = util.calcular_pv(caracteristicas["CON"])
        self.pv_actual = pv
        self.campagna = campagna
        self.id = self.crear_id() # Usar solo si da problemas los nombres con espacio

    def crear_id(self):
        id = f"{self.nombre.replace(" ", "-")}_{self.campagna}"
        return id

    def atacar(self, objetivo, arma=None):
        modificador = self.modificadores["FUE"]
        if arma:
            modificador += arma.modificador
        tirada = util.tirar_dado(20)
        ataque = tirada + modificador
        mensaje = f"{self.nombre} ataca a {objetivo.nombre}, ha sacado un {tirada} + {modificador} = {ataque}"
        dagno = self.calcular_dagno(arma) + modificador
        return ataque, dagno, mensaje

    def calcular_dagno(self, arma=None):
        return 0

    def recibir_ataque(self, ataque, dagno):
        if ataque > self.defensa:
            mensaje = f" El ataque es mayor que la defensa: {self.defensa}, {self.nombre} recibe {dagno} puntos de daño"
            self.recibir_dagno(dagno)
            return  mensaje
        else:
            mensaje = f"{self.nombre} para el ataque con defensa de: {self.defensa}, no recibe daño"
            return mensaje

    def recibir_dagno(self, dagno):
        self.pv_actual -= dagno
        if self.pv_actual <= 0:
            self.pv_actual = 0
            mensaje = f"{self.nombre} ha muerto, RIP"
        else:
            mensaje = f"{self.nombre} ha recibido {dagno} puntos de daño, le quedan {self.pv_actual} puntos de vida"
        util.mostrar_mensaje(mensaje)

    def curarse(self, puntos_curacion):
        self.pv_actual += puntos_curacion
        if self.pv_actual > self.pv_max:
            self.pv_actual = self.pv_max
            mensaje = f"{self.nombre} ha recuperado todos los puntos de vida"
        else:
            mensaje = f"{self.nombre}  ha recuperado {puntos_curacion} tiene {self.pv_actual} puntos de vida"
        return mensaje

    def subir_nivel(self):
        self.nivel += 1
        mensaje = f" {self.nombre} ha subido a nivel {self.nivel}"
        util.mostrar_mensaje(mensaje)

    def calcular_modificadores(self, caracteristicas):
        for clave, valor in caracteristicas.items():
            self.modificadores[clave] = util.calcular_modificador(valor)

    def to_string(self):
        string = (f"{self.nombre}, es un {self.tipo} de {self.jugador}, "
                f"Caracteristicas: {self.caracteristicas}, "
                f"Modificadores: {self.modificadores} "
                f"PV: {self.pv_actual}, CA: {self.defensa} "
                f"Descripción :  {self.descripcion}.")
        return string