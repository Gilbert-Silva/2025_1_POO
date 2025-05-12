#import datetime
from datetime import datetime, timedelta
import pytz

# modulo.classe
#x = datetime.datetime(2025, 5, 12)
#print(x)
#y = datetime.datetime(2025, 5, 12, 16, 48)
#print(y)

# classe
x = datetime(2025, 5, 12)
print(x)
y = datetime(2025, 5, 12, 16, 48)
print(y)
#z = datetime(2025, 2, 30)
#print(z)
c = datetime.today()
d = datetime.now()
print(c)
print(d)

brasilia_tz = pytz.timezone('America/Sao_Paulo')
hoje_em_brasilia = datetime.now(brasilia_tz)
print(type(brasilia_tz))
print(hoje_em_brasilia)

#x = input("Informe sua data de nascimento no formato dd/mm/yyyy: ")
#d = datetime.strptime(x, "%d/%m/%Y")
x = "12/05/2025 16:30"
d = datetime.strptime(x, "%d/%m/%Y %H:%M")
print(d)
print(d.day, d.month, d.year)
print(d.date())
print(d.time())
print(d.weekday())
print(d.strftime("%d/%m/%Y"))
print(d.strftime("%d/%m/%Y %H:%M"))
print(d.strftime("%A, %d/%B/%Y"))

y = timedelta(hours=1, minutes=30)
print(y) # timedelta
print(d) # datetime
print(d + y) # datetime + timedelta -> datetime

x = input("Informe sua data de nascimento no formato dd/mm/yyyy: ")
d = datetime.strptime(x, "%d/%m/%Y")
hoje = datetime.today()
dif = hoje - d
print(dif)
dif = d - hoje
print(dif)

d1 = datetime(2025, 5, 1)
d2 = datetime(2025, 6, 1)
print(d2 - d1)









# parâmetro com valor padrão
def funcao(x = 0, y = 0):
    print(x, y)

funcao()
funcao(10)
funcao(10, 20)


