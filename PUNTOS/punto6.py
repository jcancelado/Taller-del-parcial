class Caja:
 __slots__ = ('x',)
c = Caja()
c.x = 10
c.y = 20
#RTA: Esto ya que se estan limitando los atributos
#AttributeError: 'Caja' object has no attribute 'y'