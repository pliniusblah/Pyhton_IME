def fatorial(numero):
  if numero > 1:
     return numero * fatorial(numero-1)
  else:
    return 1

numero = 1

while numero > 0:
  numero = int(input("Digite um número: "))
  print(fatorial(numero))