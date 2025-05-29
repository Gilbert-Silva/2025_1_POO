from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas

class UI:  # Visão/Apresentação - Não tem instância
    carrinho = None   # atributo de classe
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
        print("| 13-Iniciar um carrinho de compra               |")
        print("| 14-Listar as compras                           |")
        print("| 15-Inserir produto no carrinho                 |")
        print("| 16-Confirmar a compra                          |")
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

            if op == 13: UI.venda_inserir()
            if op == 14: UI.venda_listar()
            if op == 15: UI.vendaitem_inserir()

    # Operações de Venda
    @classmethod
    def venda_inserir(cls): # C - create
        v = Venda(0)
        Vendas.inserir(v)
        cls.carrinho = v

    @staticmethod # R - read
    def venda_listar(): 
        for v in Vendas.listar(): print(v)

    @classmethod 
    def vendaitem_inserir(cls): 
        print("O produto vai ser inserido nesse carrinho: ", cls.carrinho)

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