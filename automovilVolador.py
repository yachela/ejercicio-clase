
class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad


class AutomovilVolador(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad, esta_volando):
        super().__init__(color, marca, aceleracion, velocidad)
        self.ruedas = 6 
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

    def conducir(self):
        return "Conduzco un auto" 


mi_auto_volador = AutomovilVolador("verde", "fiat", 120, 120, False)


print(f"Color del auto volador: {mi_auto_volador.color}")
