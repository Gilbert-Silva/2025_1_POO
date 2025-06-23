from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaitem import VendaItem, VendaItens

class View:
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return { "id" : c.id, "nome" : c.nome }
        return None
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.email == "admin" : return
        View.cliente_inserir("admin", "admin", "1234", "1234")        
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)
    def cliente_listar():
       return Clientes.listar()
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    def inserir_produto_no_carrinho(id_carrinho, id_produto, qtd):
        # Consultar preço do produto
        preco = Produtos.listar_id(id_produto).preco
        # Instanciar o item da venda
        vi = VendaItem(0, qtd, preco)
        vi.id_venda = id_carrinho
        vi.id_produto = id_produto
        # Inserir o item da venda
        VendaItens.inserir(vi)
        # Atualizar o total da venda (carrinho)
        carrinho = Vendas.listar_id(id_carrinho)
        subtotal = qtd * preco
        carrinho.total += subtotal
        Vendas.atualizar(carrinho)

      
