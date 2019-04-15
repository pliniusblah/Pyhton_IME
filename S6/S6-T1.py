def boas_vindas():
  print("\nBem-vindo ao jogo do NIM! Escolha:")
  print("\n1 - para jogar uma partida isolada")
  return int(input("2 - para jogar um campeonato "))

def computador_escolhe_jogada(n,m):
  jogada = 1
  jogadaComputador = False
  
  while (jogada <= m) and (not jogadaComputador):
    if ((n - jogada) % (m + 1)) == 0 or jogada == n:
      n -= jogada
      jogadaComputador = True
      break
    jogada += 1

  if not jogadaComputador:
    jogada = m
    n -= m
  
  if jogada == 1:
    print("\nO computador tirou uma peça.")
  else:
    print("\nO computador tirou",jogada,"peças.")

  return jogada

def usuario_escolhe_jogada(n,m):
  usuarioJoga = False

  while not usuarioJoga:
    jogada = int(input("\nQuantas peças você vai tirar? "))

    if jogada > m or jogada < 1 or jogada > n:
      print("\nOops! Jogada inválida! Tente de novo.")
    else:
      usuarioJoga = True

  if jogada == 1:
    print("Você tirou uma peça.")
  else:
    print("Você tirou",jogada,"peças.")

  return jogada

def partida():
  computadorJoga = False
  computadorVence = True

  n = int(input("Quantas peças? "))
  m = int(input("Limite de peças por jogada? "))

  if n % (m+1) == 0:
    print("\nVoce começa!")
  else:
    print("\nComputador começa!")
    computadorJoga = True
  
  while n > 0:
    if computadorJoga:
      computadorJoga = False
      n -= computador_escolhe_jogada(n,m)
      computadorVence = True
    else:
      computadorJoga = True
      n -= usuario_escolhe_jogada(n,m)
      computadorVence = False
    
    if n > 0: 
      if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
      else:
        print("Agora restam",n,"peças no tabuleiro.")

  if computadorVence:
    print("Fim do jogo! O computador ganhou!")
  else:
    print("Fim do jogo! Você ganhou!")

  return computadorVence

def campeonato():
  rodada = 0
  VC = 0
  PC = 0

  while rodada < 3:
    print("\n**** Rodada",rodada+1,"****\n")
    if partida():
      PC += 1
    else:
      VC += 1

    rodada += 1
  print("\n**** Final do campeonato! ****")
  print("\nPlacar: Você",VC,"X",PC,"Computador")

def main():
  escolha = 0
  while escolha != 1 and escolha != 2:
    escolha = boas_vindas()

  if escolha == 1:
    print("\nVocê escolheu uma partida!\n")
    partida()
  else:
    print("\nVocê escolheu um campeonato!")
    campeonato()

main()