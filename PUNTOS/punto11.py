class Cuenta:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo
    @property
    def saldo(self):
        return self._saldo 
    @saldo.setter
    def saldo(self, saldonuevo):
        if saldonuevo < 0:
         print("el saldo no puede ser negativo")
        else:
            self._saldo = saldonuevo 

saldonuevo = int(input("Ingrese un saldo"))
saldonue=Cuenta(saldonuevo)
print(saldonue.saldo) 