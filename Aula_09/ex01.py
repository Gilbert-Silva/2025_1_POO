x = []
y = list()
z = [1, 2, 3, 4, "Texto"]

print(type(x), len(x))
print(type(y), len(y))
print(type(z), len(z))

print(z[0])
print(z[-1])

print(z)
print(*z)

for elem in z:
    print(elem)

#int("Teste")
#print(z[5])

l = z
l.append("Tads")
print(z)
print(id(l), id(z))

l2 = z[:]
l2.append("POO")

print(z)
print(l2)
