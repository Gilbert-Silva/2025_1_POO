import json

class Cliente:   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)       # atributo da instância
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id): 
        self.__id = id
    def set_nome(self, nome): 
        self.__nome = nome
        if nome == "": raise ValueError("Nome não pode ser vazio")
    def set_email(self, email): 
        self.__email = email
        if email == "": raise ValueError("E-mail não pode ser vazio")
    def set_fone(self, fone): 
        self.__fone = fone
    def set_senha(self, senha): 
        self.__senha = senha

    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["nome"] = self.__nome
        dic["email"] = self.__email
        dic["fone"] = self.__fone
        dic["senha"] = self.__senha
        return dic

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
class Clientes:    # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []   # atributo de classe / estático - Não tem instância
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        if len(cls.objetos) > 0:
            m = max(cls.objetos, key=lambda c: c.get_id()).get_id()
        #for x in cls.objetos:
        #    if x.id > m: m = x.id
        obj.set_id(m + 1)    
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
            if obj.get_id() == id: return obj
        return None               
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
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
                    obj = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Cliente.to_json)
