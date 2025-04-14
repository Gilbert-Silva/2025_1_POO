x = 1
while x <= 10:
  print(x, end = " ")
  x += 1
print()

for x in range(1, 11):
  print(x, end = " ")
print()

def print_range(x, limite):
  if x == limite: return
  print(x, end = " ")
  print_range(x + 1, limite)

print_range(1, 11)
print()
