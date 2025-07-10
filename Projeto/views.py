from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaitem import VendaItem, VendaItens

class View:
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return { "id" : c.get_id(), "nome" : c.get_nome() }
        return None
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.get_email() == "admin" : return
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
        c = Cliente(id, "texto", "texto", "", "")
        Clientes.excluir(c)
    def cliente_iniciar_carrinho(id_cliente):   
        # procura um carrinho para o cliente
        for v in Vendas.listar():
            if v.id_cliente == id_cliente and v.carrinho:
                return v.id
        # insere um carrinho novo
        v = Vendas.inserir()
        v.id_cliente = id_cliente
        return v.id



    def categoria_listar():
       return Categorias.listar()

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

      
