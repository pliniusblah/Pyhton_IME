numero = int(input())

resto5 = numero % 5
resto3 = numero % 3

if ((resto3 == 0) and (resto5 == 0)):
    print("FizzBuzz")
else:
    print(numero)