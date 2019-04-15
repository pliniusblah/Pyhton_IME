import math

a = int(input())
b = int(input())
c = int(input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raiz = (-b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("a raiz desta equação é",raiz)
    else:
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        if raiz < raiz2:
            print("as raízes da equação são",raiz,"e",raiz2)
        else:
            print("as raízes da equação são",raiz2,"e",raiz)