from abc import ABC
from logica import util

# class Personaje (ABC):
#     """Clase abstracta de la que heredan todos los tipos de personajes"""
    # def __init__(self, nombre, clase,  caracteristicas, vida_max):
    #     self.nombre = self.tratar_nombre(nombre) # Usar solo si da problemas los nombres con espacio
    #     self.clase = clase
    #     self.nivel = 0
    #     self.inventario = Inventario() # ToDo: Pensar como gestionar esto, igual con una clase inventario
    #     self.caracteristicas = caracteristicas # Esto va a ser un diccionario
    #     self.defensa = defensa # La CA, es decir, la dificultad de que le de un golpe
    #     self.vida_max = vida_max
    #     self.vida_actual = vida_max # Cuando se crea un personaje tiene la vida max, luego se modifica
    #     self.vivo = True # Booleano que indica si el pj está vivo o muerto
    #     self.nivel = 1
    #     self.inventario = []

class Personaje:
    def __init__(self, nombre, caracteristicas, vida_max):
        self.nombre = self.tratar_nombre(nombre) # Usar solo si da problemas los nombres con espacio
        self.nivel = 0
        self.caracteristicas = caracteristicas # Esto va a ser un diccionario
        self.defensa = caracteristicas["CON"] # La CA, es decir, la dificultad de que le de un golpe
        self.vida_max = vida_max
        self.vida_actual = vida_max # Cuando se crea un personaje tiene la vida max, luego se modifica
        self.vivo = True # Booleano que indica si el pj está vivo o muerto
        self.nivel = 1
        print(f"Ha nacido {self.nombre}")

    def recibir_ataque(self, ataque, dagno):
        if ataque > self.defensa:
            mensaje = f"El ataque entra, {self.nombre} recibe {dagno} puntos de daño"
            util.mostrar_mensaje(mensaje)
            self.recibir_dagno(dagno)
        else:
            mensaje = f"{self.nombre} para el ataque, no recibe daño"
            util.mostrar_mensaje(mensaje)

    def tratar_nombre(self,nombre_bruto):
        nombre_bruto = str(nombre_bruto).title()
        nombre_tratado = nombre_bruto.replace(" ", "_")
        return nombre_tratado

    def recibir_dagno(self, dagno):
        self.vida_actual -= dagno
        if self.vida_actual <= 0:
            self.vida_actual = 0
            self.vivo = False
            mensaje = f"{self.nombre} ha muerto, RIP"
        else:
            mensaje = f"{self.nombre} ha recibido {dagno} puntos de daño, le quedan {self.vida_actual} puntos de vida"
        util.mostrar_mensaje(mensaje)

    def curarse(self, puntos_curacion):
        self.vida_actual += puntos_curacion
        if self.vida_actual > self.vida_max:
            self.vida_actual = self.vida_max
            mensaje = f"{self.nombre} ha recuperado todos los puntos de vida"
        else:
            mensaje = f"{self.nombre}  ha recuperado {puntos_curacion} tiene {self.vida_actual} puntos de vida"
        util.mostrar_mensaje(mensaje)

    # def modificar_vida(self,mod):
    #     self.vida += mod
    #     return

    def subir_nivel(self):
        self.nivel += 1
        mensaje = f" {self.nombre} ha subido a nivel {self.nivel}"
        util.mostrar_mensaje(mensaje)

    def atacar(self, objetivo, arma=None):
        modificador = self.caracteristicas["FUE"]
        if arma:
            modificador += arma.modificador
        tirada = util.tirar_dado(20)
        ataque = tirada + modificador
        mensaje = f"{self.nombre} ataca a {objetivo.nombre} con {tirada} + {modificador} = {ataque}"
        util.mostrar_mensaje(mensaje)
        dagno = self.calcular_dagno(arma) + modificador
        objetivo.recibir_ataque(ataque,dagno)

    def calcular_dagno(self, arma=None):
        return 0

# class PersonajeJugable(Personaje):
#     def __init__(self, nombre, clase, inventario, caracteristicas,jugador):
#         super().__init__(nombre, clase, inventario, caracteristicas)
#         self.jugador = jugador
#
# class PersonajeNoJugador(Personaje):
#     def __init__(self, nombre, clase, inventario, caracteristicas):
#         super().__init__(nombre, clase, inventario, caracteristicas)
#