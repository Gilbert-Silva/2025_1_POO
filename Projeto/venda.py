import json
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
    def to_json(self):
        dic = {}
        dic["id"] = self.id       
        dic["data"] = self.data.strftime("%d/%m/%Y %H:%M")
        dic["carrinho"] = self.carrinho
        dic["total"] = self.total
        dic["id_cliente"] = self.id_cliente
        return dic
    
class Vendas:      # Persistência - Armazena os objetos em um arquivo/banco de dados
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
            with open("vendas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Venda(dic["id"])
                    obj.data = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
                    obj.carrinho = dic["carrinho"]
                    obj.total = dic["total"]
                    obj.id_cliente = dic["id_cliente"]
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Venda.to_json)

