import enum

class EstadoCivil(enum.Enum):
    Solteiro = 1
    Casado = 2
    Divorciado = 3
    Viuvo = 4

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.estado_civil = EstadoCivil.Solteiro

x = Pessoa()
print(x.nome)
print(x.estado_civil)
            