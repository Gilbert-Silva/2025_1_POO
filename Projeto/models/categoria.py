import json

class Categoria:
    def __init__(self, id, descricao):
        self.id = id       
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"

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
    
