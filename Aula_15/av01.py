from datetime import datetime, timedelta

class Contrato:
    def __init__(self, plano, ddd, numero, valor):
        self.set_plano(plano)
        self.set_ddd(ddd)
        self.set_numero(numero)
        self.set_valor(valor)
        # self.__cliente = None

    def set_plano(self, plano):
        if plano == "": raise ValueError("Plano não pode ser vazio")
        self.__plano = plano 
    def set_ddd(self, ddd):
        if 11 >= ddd >= 99: raise ValueError("DDD deve estar entre 11 e 99")
        self.__ddd = ddd 
    def set_numero(self, numero):
        if len(numero) != 9: raise ValueError("Número deve ter 9 algarismo")
        self.__numero = numero
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo")  
        self.__valor = valor      

    def get_plano(self): return self.__plano
    def get_ddd(self): return self.__ddd
    def get_numero(self): return self.__numero
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"{self.__plano}: ({self.__ddd}) {self.__numero} R$ {self.__valor:.2f}"

class Cliente:
    def __init__(self, nome, data_cadastro):
        self.set_nome(nome)
        self.set_data_cadastro(data_cadastro)
        self.__contratos = []

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome 
    def set_data_cadastro(self, data_cadastro):
        if data_cadastro > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data_cadastro = data_cadastro 
    def get_nome(self): return self.__nome
    def get_data_cadastro(self): return self.__data_cadastro

    def inserir(self, contrato):
        self.__contratos.append(contrato)
    def remover(self, contrato):
        if contrato in self.__contratos:
            self.__contratos.remove(contrato)
    def listar(self):
        return self.__contratos
    def tempo(self):
        t = datetime.now() - self.__data_cadastro  # timedelta
        anos = t.days // 365
        dias = t.days % 365
        meses = dias // 30
        return f"{anos} ano(s) e {meses} mes(es)"
    def total(self):
        t = 0
        for contrato in self.__contratos: t += contrato.get_valor()
        return t
    def __str__(self):
        return f"{self.__nome} cadastrado em {self.__data_cadastro.strftime("%d/%m/%Y")} tem {len(self.__contratos)} contrato(s)"    

c = Cliente("Alex", datetime(2024, 3, 1))

x = Contrato("5GB", 11, "987654321", 100)
y = Contrato("15GB", 84, "987654321", 150)

c.inserir(x)
c.inserir(y)
print(c)
for contrato in c.listar(): print(contrato)
print(c.tempo())
print(c.total())



