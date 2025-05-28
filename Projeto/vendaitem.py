class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id       
        self.qtd = qtd
        self.preco = preco
        self.id_venda = 0
        self.id_produto = 0
    def __str__(self):
        return f"{self.id} - {self.qtd} - R$ {self.preco:.2f}"
