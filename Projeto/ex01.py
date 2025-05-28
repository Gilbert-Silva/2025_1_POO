import json
from datetime import datetime

class Cliente:   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, fone):
        self.id = id       # atributo da instância
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Categoria:
    def __init__(self, id, descricao):
        self.id = id       
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class Produto:
    def __init__(self, id, descricao, preco, estoque):
        self.id = id       
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = 0
    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.preco:.2f} - estoque: {self.estoque}"

class Venda:
    def __init__(self, id):
        self.id = id       
        self.data = datetime.now()
        self.carrinho = True
        self.total = 0
        self.id_cliente = 0
    def __str__(self):
        return f"{self.id} - {self.data.strftime("%d/%m/%Y %H:%M")} - R$ {self.total:.2f}"
    
class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id       
        self.qtd = qtd
        self.preco = preco
        self.id_venda = 0
        self.id_produto = 0
    def __str__(self):
        return f"{self.id} - {self.qtd} - R$ {self.preco:.2f}"

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
        try:     
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)


class Categorias:    # Persistência - Armazena os objetos em um arquivo/banco de dados
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
        try:    
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Categoria(dic["id"], dic["descricao"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)



class Produtos:    # Persistência - Armazena os objetos em um arquivo/banco de dados
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
        try:   
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"])
                    obj.id_categoria = dic["id_categoria"]
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)


class UI:  # Visão/Apresentação - Não tem instância
    @staticmethod
    def menu():
        print("|------------------------------------------------|")
        print("| Cadastro de Clientes                           |")
        print("| 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir    |")
        print("|------------------------------------------------|")
        print("| Cadastro de Categorias                         |")
        print("| 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir    |")
        print("|------------------------------------------------|")
        print("| Cadastro de Produtos                           |")
        print("| 9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir |")
        print("|------------------------------------------------|")
        print("| 99-FIM                                         |")
        print("|------------------------------------------------|")
        print()
        op = int(input("Selecione uma opção: "))
        print()
        return op

    @staticmethod
    def main():    
        op = 0
        # clientes = []
        while op != 99:
            op = UI.menu()
            if op == 1: UI.cliente_inserir() 
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

            if op == 5: UI.categoria_inserir() 
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()

            if op == 9: UI.produto_inserir() 
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()

    # CRUD de Clientes
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

    # CRUD de Categorias
    @staticmethod
    def categoria_inserir(): # C - create
        descricao = input("Informe a descrição: ")
        c = Categoria(0, descricao)
        Categorias.inserir(c)
    @staticmethod # R - read
    def categoria_listar(): 
        for c in Categorias.listar(): print(c)
    @staticmethod # U - update
    def categoria_atualizar(): 
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        c = Categoria(id, descricao)
        Categorias.atualizar(c)
    @staticmethod # D - delete
    def categoria_excluir(): 
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        c = Categoria(id, "")
        Categorias.excluir(c)

    # CRUD de Produtos
    @staticmethod
    def produto_inserir(): # C - create
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        c = Produto(0, descricao, preco, estoque)
        c.id_categoria = id_categoria
        Produtos.inserir(c)
    @staticmethod # R - read
    def produto_listar(): 
        for c in Produtos.listar(): print(c)
    @staticmethod # U - update
    def produto_atualizar(): 
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da nova categoria: "))
        c = Produto(id, descricao, preco, estoque)
        c.id_categoria = id_categoria
        Produtos.atualizar(c)
    @staticmethod # D - delete
    def produto_excluir(): 
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        c = Produto(id, "", "", "")
        Produtos.excluir(c)

UI.main()            