import contabancaria

class UI:
    @staticmethod
    def menu():
        print("Selecione a figura: 1-Abrir Conta, 2-Depositar, 3-Sacar, 4-Ver Saldo, 9-Fim")
        return int(input())

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: x = UI.abrir_conta()
            if op == 2: UI.depositar(x)
            if op == 3: UI.sacar(x)
            if op == 4: UI.ver_saldo(x)

    @staticmethod
    def abrir_conta(): # método da classe
        x = contabancaria.ContaBancaria()
        titular = input("Informe o titular da conta: ")
        numero = input("Informe o número da conta: ")
        x.set_titular(titular)
        x.set_numero(numero)
        return x

    @staticmethod
    def depositar(x): # método da classe
        print(f"Seu saldo atual é {x.get_saldo()}")
        valor = float(input("Informe o valor do depósito: "))
        x.depositar(valor)
        print(f"Seu saldo agora é {x.get_saldo()}")

    @staticmethod
    def sacar(x): # método da classe
        print(f"Seu saldo atual é {x.get_saldo()}")
        valor = float(input("Informe o valor do saque: "))
        x.sacar(valor)
        print(f"Seu saldo agora é {x.get_saldo()}")

    @staticmethod
    def ver_saldo(x): # método da classe
        print(f"Seu saldo atual é {x.get_saldo()}")

UI.main()