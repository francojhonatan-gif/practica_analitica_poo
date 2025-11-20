from figurasgeometricas import FigurasGeometricas
from math import pi

class Cilindro (FigurasGeometricas):
    def __init__(self,radio,altura) :
        self.radio = radio
        self.altura = altura
        
        @property
        def radio(self) -> float:
         return self.radio
    
        @radio.setter
        def radio(self,radio:float):
          self.radio = radio
        
        @property
        def altura(self) -> float:
         return self.altura
    
        @altura.setter
        def altura(self, altura : float):
         self.altura = altura
        
    def area(self):
        return 2 * pi * self.radio(self.radio + self.altura)
        