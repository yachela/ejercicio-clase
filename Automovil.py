class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.ruedas = 4
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

mi_bm = Automovil("Azul", "BMW", 2.6, 150)
    
print(f"Numero de ruedas: {mi_bm.ruedas}")
print(f"Aceleración de: {mi_bm.aceleracion}")