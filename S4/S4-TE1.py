valor = int(input("Digite um número inteiro: "))
aux = 0
adjacenciaNumero = False

while (valor % 10) > 0 and (not adjacenciaNumero):
    if (valor % 10) == aux:
        adjacenciaNumero = True
    aux = valor % 10
    valor = valor // 10

if adjacenciaNumero:
    print("sim")
else:
    print("não")