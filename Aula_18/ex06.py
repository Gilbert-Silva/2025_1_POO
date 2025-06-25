from datetime import datetime, timedelta

erro = True
while erro:
    s = input("Informe uma data no formato dd/mm/aaaa: ")
    try:
        d = datetime.strptime(s, "%d/%m/%Y")
        t = timedelta(days = 1)
        d += t
        print(d)
        erro = False
    except:
        print("Você não digitou uma data válida")    




