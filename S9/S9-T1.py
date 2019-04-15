import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
  i = 1
  textos = []
  texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  while texto:
    textos.append(texto)
    i += 1
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

  return textos

def separa_sentencas(texto):
  '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
  sentencas = re.split(r'[.!?]+', texto)
  if sentencas[-1] == '':
    del sentencas[-1]
  return sentencas

def separa_frases(sentenca):
  '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
  return frase.split()

def n_palavras_unicas(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      if freq[p] == 1:
        unicas -= 1
      freq[p] += 1
    else:
      freq[p] = 1
      unicas += 1

  return unicas

def n_palavras_diferentes(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
  freq = dict()
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      freq[p] += 1
    else:
      freq[p] = 1

  return len(freq)

##############
def total_palavras(lista_palavras):
  total = 0

  for palavra in lista_palavras:
    total += len(palavra)

  return total

def tam_medio(texto):
  arraypalavras = separa_palavras(texto)

  total = total_palavras(arraypalavras)

  return total / len(arraypalavras)

def type_token(texto):
  arraypalavras = separa_palavras(texto)
  numPalavras = n_palavras_diferentes(arraypalavras)

  return numPalavras / len(arraypalavras)

def hapax_legomana(texto):
  arraypalavras = separa_palavras(texto)
  numPalavrasUnicas = n_palavras_unicas(arraypalavras)

  return numPalavrasUnicas / len(arraypalavras)

def tam_medio_setenca(texto):
  sentencas = separa_sentencas(texto)
  num_sentencas = len(sentencas)
  total = 0

  for sentenca in sentencas:
    total += total_palavras(removePontuacao(sentenca, ""))

  return total / num_sentencas

def complexidade_sentenca(texto):
  sentencas = separa_sentencas(texto)
  num_sentencas = len(sentencas)

  total_frases = 0
  for sentenca in sentencas:
    total_frases += len(separa_frases(sentenca))

  return total_frases / num_sentencas

def tam_medio_frase(texto):
  sentencas = separa_sentencas(texto)
  
  total_frases = 0
  total_caracteres = 0
  for sentenca in sentencas:
    total_frases += len(separa_frases(sentenca))
    for frase in separa_frases(sentenca):
      total_caracteres += len(frase)

  return total_caracteres / total_frases

def compara_assinatura(as_a, as_b):
  '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
  pass

def calcula_assinatura(texto):
  '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
  pass

def avalia_textos(textos, ass_cp):
  '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
  pass

x = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."

def removePontuacao(texto, remover):
  novoTexto = texto
  for x in remover:
    novoTexto = novoTexto.replace(x, '')
  return novoTexto

print(tam_medio(removePontuacao(x,",.!?:;")))
print(type_token(removePontuacao(x,",.!?:;")))
print(hapax_legomana(removePontuacao(x,",.!?:;")))

print(tam_medio_setenca(x))
print(complexidade_sentenca(x))
print(tam_medio_frase(x))