import json
class Cliente:   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, fone):
        self.id = id       # atributo da instância
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

#x = Cliente(1, "Alex", "alex@email.com", "987654321")
#print(x)

class Clientes:    # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []   # atributo de classe / estático - Não tem instância

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar() 

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("clientes.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

class UI:  # Visão/Apresentação - Não tem instância
    @staticmethod
    def menu():
        print("Cadastro de Clientes")
        return int(input("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim: "))

    @staticmethod
    def main():    
        op = 0
        # clientes = []
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir() # clientes)
            if op == 2: UI.cliente_listar() # clientes)

    @staticmethod
    def cliente_inserir(): # clientes):
        id = int(input("Informe o id do cliente: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Cliente(id, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar(): # clientes):
        for c in Clientes.listar(): print(c)

UI.main()            