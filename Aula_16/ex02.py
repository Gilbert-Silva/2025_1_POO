import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

lista = []    
with open("clientes.json", mode="r") as arquivo:
    s = json.load(arquivo)
    for dic in s: 
        c = Cliente(dic["id"], dic["nome"])
        lista.append(c)
        print(dic, c)

  
