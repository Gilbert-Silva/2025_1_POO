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
        m = 0
        for x in cls.objetos:
            if x.id > m: m = x.id
        obj.id = m + 1    
        cls.objetos.append(obj)
        cls.salvar() 

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None            
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

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
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

    @staticmethod
    def cliente_inserir(): # C - create
        # id = int(input("Informe o id do cliente: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod # R - read
    def cliente_listar(): 
        for c in Clientes.listar(): print(c)

    @staticmethod # U - update
    def cliente_atualizar(): 
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")        
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    @staticmethod # D - delete
    def cliente_excluir(): 
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

UI.main()            