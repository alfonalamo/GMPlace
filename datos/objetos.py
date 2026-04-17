class Objeto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        pass

class ObjetoConsumible(Objeto):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion, precio)
        pass


class ObjetoEquipable(Objeto):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion, precio)
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

