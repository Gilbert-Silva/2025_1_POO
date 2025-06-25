x = int(input("Informe um número: "))
print(x)

def func(x):
    print(x)
    func(x+1)

func(1)

