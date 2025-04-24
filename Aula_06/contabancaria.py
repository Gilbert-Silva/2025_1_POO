class ContaBancaria:
    def __init__(self):
        self.__titular = "titular"
        self.__numero = "0000-0"
        self.__saldo = 0
    def set_titular(self, v):
        if v == "": raise ValueError("Titular não pode ser vazio")
        self.__titular = v
    def get_titular(self):
        return self.__titular
    def set_numero(self, v):
        if v == "": raise ValueError("Número da conta não pode ser vazio")
        self.__numero = v
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def depositar(self, v):
        if v <= 0: raise ValueError("Valor não pode ser negativo")
        self.__saldo += v
    def sacar(self, v):
        if v <= 0: raise ValueError("Valor não pode ser negativo")
        if v > self.__saldo: raise ValueError("Saldo insuficiente")
        self.__saldo -= v

        
            