largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

n = largura

while altura > 0:
  while largura > 0:
    largura -= 1
    print("#", end = "")
  print()
  largura = n
  altura -= 1