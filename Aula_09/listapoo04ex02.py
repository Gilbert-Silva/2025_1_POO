class PlayList:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []
    def inserir(self, m):
        self.__musicas.append(m)  
    def listar(self):
        return self.__musicas      
    def __str__(self):
        return f"PlayList {self.__nome} tem {len(self.__musicas)} música(s)"    

class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"    

class UI:
    @staticmethod
    def menu():
        return int(input("Menu: 1-Criar Playlist, 2-Inserir música, 3-Listar músicas, 9-Fim: "))

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: x = UI.criar_playlist()
            if op == 2: UI.inserir_musica(x)
            if op == 3: UI.listar_musicas(x)

    @staticmethod
    def criar_playlist(): # método da classe
        nome = input("Informe o nome da playlist: ")
        descricao = input("Informe uma descrição: ")
        x = PlayList(nome, descricao)
        return x

    @staticmethod
    def inserir_musica(x): # método da classe
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista/banda: ")
        album = input("Informe o álbum: ")
        musica = Musica(titulo, artista, album)
        x.inserir(musica)

    @staticmethod
    def listar_musicas(x): # método da classe
        print(x)
        for musica in x.listar():
            print("  ", musica)

UI.main()    

"""
x = PlayList("Rock", "Minhas música de rock preferidas")
y = PlayList("Axé", "Show de Ivete Sangalo - Maracanã")
m1 = Musica("Hotel Califórnia", "Eagles", "Eagles")
m2 = Musica("Beth Balanço", "Barão Vermelho", "Melhores músicas")
m3 = Musica("Arerê", "Ivete", "Show Maracanã")
x.inserir(m1)
x.inserir(m2)
y.inserir(m3)

print(x)
for musica in x.listar():
    print("  ", musica)
print()
print(y)
for musica in y.listar():
    print("  ", musica)

#print(x)
#print(y)
#print(m1)
#print(m2)
#print(m3)

"""
        