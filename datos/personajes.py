class Personaje:
    def __init__(self, nombre, clase, inventario, caracteristicas):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 0
        self.inventario = inventario # ToDo: Pensar como gestionar esto, igual con una clase inventario
        self.caracteristicas = caracteristicas # ToDo: Pensar si pasar un diccionario o una clase

class PersonajeJugable(Personaje):
    def __init__(self, nombre, clase, inventario, caracteristicas):
        super().__init__(nombre, clase, inventario, caracteristicas)

class PersonajeNoJugador(Personaje):
    def __init__(self, nombre, clase, inventario, caracteristicas):
        super().__init__(nombre, clase, inventario, caracteristicas)