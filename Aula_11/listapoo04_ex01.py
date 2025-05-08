import random

class Bingo:
    def __init__(self, numBolas):
        if numBolas <= 0:
            raise ValueError("O número de bolas deve ser positivo.")
        self.numBolas = numBolas
        self.bolas = []

    def Proximo(self):
        if len(self.bolas) == self.numBolas:
            return -1  # Todas as bolas já foram sorteadas
        while True:
            bola = random.randint(1, self.numBolas)
            if bola not in self.bolas:
                self.bolas.append(bola)
                return bola

    def Sorteados(self):
        return sorted(self.bolas)
        
class BingoUI:
    bingo = None  # Referência à instância de Bingo

    @classmethod
    def menu(cls):
        while True:
            print("\n--- MENU BINGO ---")
            print("1. Iniciar Jogo")
            print("2. Sortear uma bola")
            print("3. Visualizar bolas sorteadas")
            print("4. Encerrar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cls.iniciar_jogo()
            elif opcao == '2':
                cls.sortear_bola()
            elif opcao == '3':
                cls.visualizar_sorteados()
            elif opcao == '4':
                print("Encerrando o programa. Obrigado por jogar!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    @classmethod
    def iniciar_jogo(cls):
        try:
            num = int(input("Digite o número total de bolas: "))
            cls.bingo = Bingo(num)
            print(f"Jogo iniciado com {num} bolas.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")

    @classmethod
    def sortear_bola(cls):
        if cls.bingo is None:
            print("Você precisa iniciar um jogo primeiro.")
            return
        bola = cls.bingo.Proximo()
        if bola == -1:
            print("Todas as bolas já foram sorteadas.")
        else:
            print(f"Bola sorteada: {bola}")

    @classmethod
    def visualizar_sorteados(cls):
        if cls.bingo is None:
            print("Você precisa iniciar um jogo primeiro.")
            return
        sorteados = cls.bingo.Sorteados()
        print("Bolas sorteadas:", sorteados if sorteados else "Nenhuma até agora.")

BingoUI.menu()