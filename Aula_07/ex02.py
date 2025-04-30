class Triangulo:
    def __init__(self):
        self.b = 1.0
        self.h = 1.0

print("iniciar")
input()

l = []
for k in range(10000001):
    x = Triangulo()
    l.append(x)
    if k % 1000000 == 0: print(k)

print("parar")
input()
print("fim")
input()
