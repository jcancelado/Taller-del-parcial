class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)
# Define aquí la propiedad temperatura_f: F = C * 9/5 + 32
#RTA:
    @property
    def temperatura_f(self):
        return self._c*9/5 +32
