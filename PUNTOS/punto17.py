#¿Qué problema hay aquí?
#RTA: El get data rompe la encapsulacion podiendola modificar desde fuera
#mi solucion fue usar el property con una tupla
class Buffer:
    def __init__(self, data):
        self._data = list(data)
    @property
    def data(self):
        return tuple(self._data)

