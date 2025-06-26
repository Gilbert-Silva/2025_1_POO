class Aluno(object):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    def comparar(self, x, y):
        if x.nome > y.nome: return True
        else: return False    
    def __str__(self):
        return f"{self.nome} - {self.matricula}"

a = Aluno("Eduardo", "1234")
b = Aluno("Bruno", "4321")
lista = [a, b]
#lista.sort()
print(*lista)


x = [1, 4, 2]
x.sort()
print(x)
