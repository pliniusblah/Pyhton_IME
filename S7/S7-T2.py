largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

n = largura
m = altura

while altura > 0:
  while largura > 0:
    if(altura == 1 or altura == m or largura == 1 or largura == n) :
      print("#", end = "")
    else:
      print("", end = " ")
    largura -= 1
  print()
  largura = n
  altura -= 1