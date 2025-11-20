from figurasgeometricas import FigurasGeometricas

class Rombo(FigurasGeometricas):
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    
    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
