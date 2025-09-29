class Base:
    def __init__(self):
        self._token = "abc"
class Sub(Base):
    def reveal(self):
        return self._token
print(Sub().reveal())
#¿Qué se imprime y por qué no hay error de acceso?
#RTA: abc, no hay error ya la convención _ es precisamente para el uso en la misma clase o las subclases