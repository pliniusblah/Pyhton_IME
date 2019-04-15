def vogal(letra):
  letra = letra.upper()
  if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
    return True
  else:
    return False

def test_func0():
  assert vogal("a") == True

def test_func1():
  assert vogal("B") == False

def test_func2():
  assert vogal("c") == False

def test_func3():
  assert vogal("U") == True