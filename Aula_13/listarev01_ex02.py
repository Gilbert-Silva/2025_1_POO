from datetime import datetime, timedelta

class Treino:
    def __init__(self, data, dist, tempo):
        #self.__data = data
        #self.__distancia = dist
        #self.__tempo = tempo
        self.set_data(data)
        self.set_distancia(dist)
        self.set_tempo(tempo)
    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data = data
    def set_distancia(self, dist):
        if dist <= 0: raise ValueError("Distância não pode ser negativa")
        self.__distancia = dist
    def set_tempo(self, tempo):
        if tempo.seconds <= 0: raise ValueError("Tempo não pode ser negativo")
        self.__tempo = tempo
    def get_data(self): return self.__data    
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo    
    def __str__(self):
        s = f"Data = {self.__data.strftime("%d/%m/%Y %H:%M")}, "
        s += f"Distância = {self.__distancia} metros, "
        s += f"Tempo = {self.__tempo}"
        return s
    def pace(self):
        return (self.__tempo.seconds / 60) / (self.__distancia / 1000)

class Atleta:
    def __init__(self, nome, nascimento):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__treinos = []
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome == nome
    def get_nome(self):
        return self.__nome
    def set_nascimento(self, nascimento):
        if nascimento > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__nascimento == nascimento
    def get_nascimento(self):
        return self.__nascimento
    def inserir(self, t):
        self.__treinos.append(t)
    def remover(self, t):
        self.__treinos.remove(t)
    def listar(self):
        return self.__treinos
    def distancia_total(self):
        total = 0
        for treino in self.__treinos:
            total += treino.get_distancia()
        return total
    def menor_pace(self):
        p = []
        for treino in self.__treinos:
            p.append(treino.pace())
        return min(p)    
    def __str__(self):
        s =  f"{self.__nome} nasceu em {self.__nascimento.strftime("%d/%m/%Y")} tem "
        s += f"{len(self.__treinos)} treino(s) cadastrado(s)"
        return s

a = Atleta("Bráulio", datetime(1970, 10, 10))

x = Treino(datetime(2025, 5, 12, 6, 45), 5000, timedelta(minutes=30))
y = Treino(datetime(2025, 5, 14, 6, 30), 5000, timedelta(minutes=30, seconds=45))
z = Treino(datetime(2024, 5, 14, 6, 30), 42000, timedelta(hours=2, seconds=35))

a.inserir(x)
a.inserir(y)
a.inserir(z)

print("Dados do atleta")
print(a)
print("Treinos do atleta")
for treino in a.listar():
    print(treino)
    print("Pace =", treino.pace(), "min/km")
print("Distância total")
print(a.distancia_total(), " metros")
print("Menor pace")
print(a.menor_pace(), " min/km")
