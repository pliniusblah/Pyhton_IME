valor = int(input("Digite o valor de n: "))

fatorial = 1

while valor > 1:
    fatorial *= valor
    valor -= 1

print(fatorial)