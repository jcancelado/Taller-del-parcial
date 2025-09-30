class S:
    def __init__(self):
        self.__data = [1, 2]
    def size(self):
        return len(self.__data)
s = S()
# Accede a __data (solo para comprobar), sin modificar el código de la clase:
# Escribe una línea que obtenga la lista usando name mangling y laimprima.
#RTA:
print(s._S__data)