def remove_repetidos(lista):
  listaNova = []
  for item in lista:
    if not item in listaNova:
      listaNova.append(item)
  listaNova.sort()
  return listaNova
