lista = []

lista.append(int(input("Digite um número: ")))

while lista[-1] != 0:
  lista.append(int(input("Digite um número: ")))

lista.reverse()

for item in lista:
  if item == 0:
    print()
  else:
    print(item)