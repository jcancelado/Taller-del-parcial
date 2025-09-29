class D:
    def __init__(self):
        self.__a = 1
        self._b = 2
        self.c = 3
d = D()
names = [n for n in dir(d) if 'a' in n]
print(names)
#RTA: Es mas probable que aparezca _D__a ya que el dir me devuelve
#el nombre con el name mangling
