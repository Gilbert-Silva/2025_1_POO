from datetime import datetime

class Venda:
    def __init__(self, id):
        self.id = id       
        self.data = datetime.now()
        self.carrinho = True
        self.total = 0
        self.id_cliente = 0
    def __str__(self):
        return f"{self.id} - {self.data.strftime("%d/%m/%Y %H:%M")} - R$ {self.total:.2f}"
    
