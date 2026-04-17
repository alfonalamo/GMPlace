from datos.personajes import Personaje

# (nombre, caracteristicas, vida_max)
elfon = Personaje("elfon", {"CON":8,"FUE":2},30)
blingo = Personaje("blingo", {"CON":6,"FUE":3},30)

blingo.atacar(elfon)
