def numero_primo(n):
  i = n - 1
  while i > 1:
    if (n % i) == 0:
      return False
    i -= 1

  return True


def n_primos(numero):
  total = 0
  while numero > 1:
    if numero_primo(numero):
      total += 1
    numero -= 1
  return total
