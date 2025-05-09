class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.ruedas = 4
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelerar(self):
        self.aceleracion = 3
        self.velocidad = 150

    def frenar(self):
    self.aceleracion = 0
    self.velocidad = 0

mi_bm = Automovil("Azul", "BMW", 2.6, 150)
mi_audi = Automovil("Negro", "Audi", 2.9, 180)
    
print(f"Numero de ruedas: {mi_bm.ruedas}")
print(f"Aceleración de: {mi_bm.aceleracion}")

mi_bm.aceleracion = 2.9;
print(f"Aceleración de: {mi_bm.aceleracion}")

mi_audi.frenar