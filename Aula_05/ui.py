import triangulo
import retangulo
import circulo

class UI:
    @staticmethod
    def menu():
        print("Selecione a figura: 1-Triângulo, 2-Retângulo, 3-Círculo, 9-Fim")
        return int(input())

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.retangulo()
            if op == 3: UI.circulo()

    @staticmethod
    def triangulo(): # método da classe
        x = triangulo.Triangulo()
        print("Informe o valor da base do triângulo: ")
        #x.b = float(input())
        x.set_base(float(input()))
        print("Informe o valor da altura do triângulo: ")
        #x.h = float(input())
        x.set_altura(float(input()))
        #print(f"A área do triângulo de base {x.b} e altura {x.h}")
        print(f"A área do triângulo de base {x.get_base()} e altura {x.get_altura()}")
        print(f"é {x.calc_area()}")

    @staticmethod
    def retangulo(): # método da classe
        x = retangulo.Retangulo()
        print("Informe o valor da base do retângulo: ")
        x.b = float(input())
        print("Informe o valor da altura do retângulo: ")
        x.h = float(input())
        print(f"A área do retângulo de base {x.b} e altura {x.h}")
        print(f"é {x.calc_area()}")

    @staticmethod
    def circulo(): # método da classe
        x = circulo.Circulo()
        print("Informe o valor do raio do círculo: ")
        x.r = float(input())
        print(f"A área do círculo de raio {x.r}")
        print(f"é {x.calc_area()}")

UI.main()
