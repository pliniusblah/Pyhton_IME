def numero_primo(n):
  i = n - 1
  while i > 1:
    if (n % i) == 0:
      return False
    i -= 1

  return True


def maior_primo(n):
  while n > 0:
    if numero_primo(n):
      print(n)
      return n
    n -= 1

maior_primo(100)

def test_func0():
  assert numero_primo(7) == True

def test_func1():
  assert numero_primo(8) == False

def test_func3():
  assert numero_primo(97) == True

def test_func4():
  assert numero_primo(16) == False

def test_func5():
  assert maior_primo(100) == 97

def test_func6():
  assert maior_primo(7) == 7

def test_func7():
  assert maior_primo(10) == 7

def test_func8():
  assert maior_primo(6) == 5