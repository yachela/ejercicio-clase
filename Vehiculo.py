from abc import ABC, abstractmethod


class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Automovil(Vehiculo):
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.ruedas = 4

    def conducir(self):
        return "Conduciendo un auto"

    def acelerar(self):
        self.aceleracion = 3
        self.velocidad = 150

    def frenar(self):
        self.aceleracion = 0
        self.velocidad = 0


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
        
        return "Conduciendo un auto volador"


mi_auto = Automovil("Rojo", "Toyota", 2.5, 100)
mi_auto_volador = AutomovilVolador("Verde", "Fiat", 3.0, 120, False)

print(mi_auto.conducir())
print(mi_auto_volador.conducir())

mi_auto_volador.vuela()
print(mi_auto_volador.conducir())
