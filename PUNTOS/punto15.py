
class Motor:
    def __init__(self, velocidad):
        self._velocidad = 0 
        self.velocidad = velocidad 
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velo):
        if self.velo < 0:
            print("la velocidad no puede ser menor que cero")
        elif self.velo > 200:
            print("la velocidad no puede ser mayor a 200")
velocidad = int(input("ingrese la velocidad"))
carro=Motor(velo)
carro.velocidad


#Escribe la versión con @property.