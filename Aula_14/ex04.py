x = {"RN" : "Natal", "PE" : "Recife", "PB" : "João Pessoa"}
y = [1, 2, 3, 4]
z = (1, 2, 3, 4)
x["AM"] = "Manuas"

print(type(x), type(y), type(z))
print(x)
print(y)
print(z)
print(x["PE"], y[2], z[1])
print(len(x), len(y), len(z))

#x[5] = y
#print(x)

# print(x["RJ"])             # KeyError
x["RJ"] = "Rio de Janeiro" # append

del x["RN"]
print(x)

for item in x.items(): print(item)
for chave, valor in x.items(): print(chave, valor)

