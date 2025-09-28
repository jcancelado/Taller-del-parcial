class A:
    def __init__(self):
        self.__secret = 42
a = A()
print(hasattr(a, '__secret'), hasattr(a, '_A__secret'))
#RTA: El primero va a devolver false y el segundo true