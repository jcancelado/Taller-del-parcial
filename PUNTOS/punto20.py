class Contador:
    def __init__(self):
        self._n = 0  

    def inc(self):
        self._n += 1
        self.__log()  

    @property
    def n(self):
        return self._n   

    def __log(self):
        print("tick")
