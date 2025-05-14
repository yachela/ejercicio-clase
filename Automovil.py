class Automovil(Vehiculo):
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

    def conducir(self):  
        return "Conduzco un auto"    

mi_bm = Automovil("Azul", "BMW", 2.6, 150)
mi_audi = Automovil("Negro", "Audi", 2.9, 180)
    
print(f"Numero de ruedas de BMW: {mi_bm.ruedas}")
print(f"Aceleración de BMW: {mi_bm.aceleracion}")

mi_bm.aceleracion = 2.9
print(f"Aceleración nueva de BMW: {mi_bm.aceleracion}")

mi_audi.frenar() 
print(f"Velocidad de Audi: {mi_audi.velocidad}")
