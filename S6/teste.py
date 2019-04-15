def partida():

  m=int(input("Quantas peças? "))

  n=int(input("Limite de peças por jogada? "))

  if n%(m+1)!=0 and m>n:
    computador_escolhe=True

    print("computador começa")

  if n%(m+1)==0 and m>n:

    computador_escolhe=False

    print("você começa")

  elif n>m:

    print("jogada inválida")

  while m>n and n>0:

    if (computador_escolhe):
      jogada=computador_escolhe_jogada(n,m)
      print("computador tirou", jogada, "peças")

    else:
      jogada=usuario_escolhe_jogada(n, m)
      print("você tirou", jogada, "peças")

    n=n-jogada