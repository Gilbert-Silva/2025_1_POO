import math 

class Circulo:
    def __init__(self):
        self.r = 0  # valor padrão = valor inicial do campo/atributo
    def calc_area(self): # método de instância
        return math.pi * self.r ** 2 