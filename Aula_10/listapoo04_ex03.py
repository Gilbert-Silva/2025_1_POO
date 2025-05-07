class Empresa:
    def __init__(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
        self.__clientes = []  # 1 --- * uma empresa pode ter vários clientes
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def get_nome(self):
        return self.__nome  
    def inserir(self, c):
        self.__clientes.append(c) 
    def listar(self):
        return self.__clientes            
    def __str__(self):
        return f"{self.__nome} tem {len(self.__clientes)} cliente(s)"
    
class Cliente:
    def __init__(self, nome, limite):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        if limite <= 0: raise ValueError("Limite tem que ser positivo")
        self.__nome = nome
        self.__limite = limite
        self.__socio = None
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def get_nome(self):
        return self.__nome            
    def set_limite(self, limite):
        if limite <= 0: raise ValueError("Limite tem que ser positivo")
        self.__limite = limite
    def get_limite(self):
        return self.__limite
    def set_socio(self, c):     # 53: c1.set_socio(c2)
        self.__socio = c        # c1.__socio = c2
        c.__socio = self        # c2.__socio = c1
    def get_socio(self):
        return self.__socio    
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome}, seu limite de crédito é R$ {self.__limite}" 
        else:
            s = f"{self.__nome}, seu limite de crédito é R$ {self.__limite}"
            s += f", seu sócio é {self.__socio.__nome}" 
            return s


x = Empresa("IFRN")
print(x)
c1 = Cliente("Eduardo", 1000)
c2 = Cliente("Lucas", 2000)
c3 = Cliente("Julia", 1500)
c4 = Cliente("Daniele", 2500)
c1.set_socio(c2)  # self -> c1    c -> c2
c3.set_socio(c4)
#c2.set_socio(c1)
x.inserir(c1)
x.inserir(c2)
x.inserir(c3)
x.inserir(c4)

print(x)
for c in x.listar(): print(" ", c)

c1.set_socio(c3)
for c in x.listar(): print(" ", c)


