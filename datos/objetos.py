class Objeto:
    def __init__(self, campagna, nombre, personaje, descripcion, tipo, precio, modificador):
        self.campagna = campagna
        self.nombre = nombre
        self.personaje = personaje
        self.descripcion = descripcion
        self.tipo = tipo
        self.precio = precio
        self.modificador = modificador

class ObjetoConsumible(Objeto):
    def __init__(self, nombre, descripcion, precio, modificador):
        super().__init__(nombre, descripcion, precio, modificador)
        pass


class ObjetoEquipable(Objeto):
    def __init__(self, nombre, descripcion, precio, modificador):
        super().__init__(nombre, descripcion, precio, modificador)
        self.equipado = False
        pass

    def equipar_objeto(self):
        if self.equipado:
            mensaje = f"Objeto {self.nombre} ya equipado"
        else:
            self.equipado = True
            mensaje = f"Se ha equipado el objeto {self.nombre}"
        print(mensaje)
        pass

