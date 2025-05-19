import enum

class Dia(enum.IntFlag):
    Domingo = 1       # 0000.0001
    Segunda = 2       # 0000.0010
    Terca = 4         # 0000.0100
    Quarta = 8        # 0000.1000
    Quinta = 16       # 0001.0000
    Sexta = 32        # 0010.0000
    Sabado = 64       # 0100.0000

x = Dia.Domingo
print(x, x.name)
y = Dia(0)
print(y, y.name)
z = Dia.Sabado | Dia.Domingo
print(z, z.name)

#    Domingo = 1       # 0000.0001
#    Sabado = 64       # 0100.0000
#    z                 # 0100.0001

