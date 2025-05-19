import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
x = Cliente(1, "Braulio")    
y = Cliente(2, "Silvia")

clientes = [x, y]

#arquivo = open("clientes.json", mode="w")
#json.dump(clientes, arquivo, default = vars)
#arquivo.close()

with open("clientes.json", mode="w") as arquivo:
    json.dump(clientes, arquivo, default = vars)


print(x)
print(x.__dict__)
print(vars(x))
print(y)
print(y.__dict__)
print(vars(y))
