class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade  

    @property
    def idade(self):
        """Getter: retorna a idade."""
        return self._idade

    @idade.setter
    def idade(self, valor):
        print("teste")
        """Setter: define a idade com validação."""
        if valor < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = valor

p = Pessoa("João", 30)

print(p.idade)       # 30  (chama o getter)
p.idade = 35         # chama o setter
print(p.idade)       # 35
# p.idade = -5       # ValueError: Idade não pode ser negativa
