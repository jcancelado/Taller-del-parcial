
#¿Dónde fallará esto y cómo lo arreglas?
#RTA: Fallara en la funcion get ya que __x tiene name mangling
#lo arregle poniendo el name mangling
class A:
    def __init__(self):
        self.__x = 1

class B(A):
    def get(self):
        #return self.__x # esta no va a funcionar
        return self._a__x