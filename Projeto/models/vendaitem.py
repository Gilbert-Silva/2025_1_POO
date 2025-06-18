import json

class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id       
        self.qtd = qtd
        self.preco = preco
        self.id_venda = 0
        self.id_produto = 0
    def __str__(self):
        return f"{self.id} - {self.qtd} - R$ {self.preco:.2f}"

class VendaItens:    # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []     # atributo de classe / estático - Não tem instância
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
            with open("vendaitens.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                    obj.id_venda = dic["id_venda"]
                    obj.id_produto = dic["id_produto"]
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

