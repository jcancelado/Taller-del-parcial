class Registro:
    def __init__(self):
        self.__items = []
    def add(self, x):
        self.__items.append(x)
    @property
    def listar_items(self):
        return tuple(self.__items)
# Crea una propiedad 'items' que retorne una tupla inmutable con
#RTA:
R=Registro()
R.add("x")
R.add("t")
R.add("b")
print(R.listar_items)
