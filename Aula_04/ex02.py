class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def teste(self):
        return "Olá"
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo() # executa o método __init__
print(x)
print(x.b, x.h)
x.b = 10
x.h = 20
print(x.teste())
print(x.b, x.h)
print(x.calc_area())  # calc_area(x)
# self é usado para o python saber qual objeto é usado na operação


y = Triangulo()
print(y)
print(y.teste())
print(y.b, y.h)
print(y.calc_area())  # calc_area(y)

