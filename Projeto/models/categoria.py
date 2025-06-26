import json
from models.modelo import Modelo

class Categoria:
    def __init__(self, id, descricao):
        self.id = id       
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"

class Categorias(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
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
    
