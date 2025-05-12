from datetime import datetime
class Atleta:
    def __init__(self, id, nome, nascimento):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento
    def set_nome(self, nome):
        self.__nome == nome
    def get_nome(self):
        return self.__nome
    def set_nascimento(self, nascimento):
        self.__nascimento == nascimento
    def get_nascimento(self):
        return self.__nascimento
    def __str__(self):
        return f"{self.__id} - {self.__nome} nasceu em {self.__nascimento.strftime("%d/%m/%Y")}"

a = Atleta(1, "Oscar", datetime.strptime("10/04/1970", "%d/%m/%Y"))
print(a)

    

