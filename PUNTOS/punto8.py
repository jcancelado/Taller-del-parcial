class M:
    def __init__(self):
        self._state = 0
    def _step(self):
        self._state += 1
        return self._state
    def __tick(self):
         return self._step()
m = M()
print(hasattr(m, '_step'), hasattr(m, '__tick'), hasattr(m,
'_M__tick'))
#La funcion hasattr es una funcion que devuelve si encuentra atributos y metodos y el metodo tick
#al estar protegido "privado", no lo va a encontrar y va a devolver false