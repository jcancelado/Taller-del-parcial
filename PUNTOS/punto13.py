class Usuario:
    def __init__(self, nombre):
        self._nombre = None
        self.nombre = nombre   

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise TypeError("el valor debe ser str")
        else:
            self._nombre = valor

