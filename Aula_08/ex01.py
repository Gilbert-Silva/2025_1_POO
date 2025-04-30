class Triangulo:
    def __init__(self, b, h):
        # opção 1 - repetir o código do set
        if b >= 0: self.__b = b
        else: raise ValueError("Base deve ser positiva")
        # opção 2 - chamar o set diretamente
        self.set_altura(self, hex)
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
    def __str__(self):
        return f"Base = {self.__b}, Altura = {self.__h}"

x = Triangulo(10, 20)
print(x.calc_area())
print(x)
y = Triangulo(30, 40)
print(y)

