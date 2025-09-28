class A:
    x = 1
    _y = 2
    __z = 3
a = A()
print(a.x)#este lo toma
print(a._y)#este lo toma
#print(a.__z)#este no lo va a tomar
print(a._A__z)#este lo toma
