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
        if self.__socio == None: return self.__limite
        return self.__limite + self.__socio.__limite
    def set_socio(self, c):     # c1.set_socio(c2)
        if self.__socio != None:
            x = self.__socio
            x.__socio = None
        if c.__socio != None:
            y = c.__socio
            y.__socio = None
        self.__socio = c        # c1.__socio = c2
        c.__socio = self        # c2.__socio = c1
    def get_socio(self):
        return self.__socio    
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome}, seu limite individual é R$ {self.__limite}" 
        else:
            s = f"{self.__nome}, seu limite individual é R$ {self.__limite}"
            s += f", seu limite total é {self.get_limite()}"
            s += f", seu sócio é {self.__socio.__nome}" 
            return s

class UI:
    @staticmethod
    def menu():
        return int(input("Menu: 1-Criar Empresa, 2-Inserir cliente, 3-Listar clientes, 4-Definir sociedade, 9-Fim: "))

    @staticmethod
    def main():
        op = 0
        x = None
        while op != 9:
            op = UI.menu()
            if op == 1: x = UI.criar_empresa()
            if op == 2: 
                if x == None: print("Crie uma empresa antes!")
                else: UI.inserir_cliente(x)
            if op == 3: 
                if x == None: print("Crie uma empresa antes!")
                else: UI.listar_clientes(x)
            if op == 4:    
                if x == None: print("Crie uma empresa antes!")
                else: UI.definir_sociedade(x)

    @staticmethod
    def criar_empresa(): # método da classe
        nome = input("Informe o nome da empresa: ")
        x = Empresa(nome)
        return x

    @staticmethod
    def inserir_cliente(x): # método da classe
        nome = input("Informe o nome do cliente: ")
        limite = float(input("Informe o limite: "))
        cliente = Cliente(nome, limite)
        x.inserir(cliente)

    @staticmethod
    def listar_clientes(x): # método da classe
        print(x)
        for cliente in x.listar():
            print("  ", cliente)

    @staticmethod
    def definir_sociedade(x): # método da classe
        print(x)
        n = 0
        clientes = x.listar()
        for cliente in clientes:
            print(n, "-", cliente)
            n += 1
        a = int(input("Informe o nº do 1º cliente: ")) 
        b = int(input("Informe o nº do 2º cliente: ")) 
        clientes[a].set_socio(clientes[b])

UI.main()    



