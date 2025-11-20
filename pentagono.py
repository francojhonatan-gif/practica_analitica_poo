import math

class Pentagono :
    def __init__(self,lado,parametro,apotema):
        self.lado = lado
        self.parametro = parametro
        self.apotema = apotema
        
    def area (self):
        return self.parametro * self.apotema /  self.lado
        