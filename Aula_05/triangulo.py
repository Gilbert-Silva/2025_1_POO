class Triangulo:
    def __init__(self):
        # b e h foram encapsulados na classe Triangulo
        # b e h não são visíveis na classe UI
        self.__b = 0  # valor padrão = valor inicial do campo/atributo
        self.__h = 0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Base deve ser positiva")
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura deve ser positiva")
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self): # método de instância
        return self.__b * self.__h / 2
    