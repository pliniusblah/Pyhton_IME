def maximo(x, y):
  if x > y:
    return x
  else:
    return y
    
def test_maximo0():
  assert maximo(0,1) == 1

def test_maximo2():
  assert maximo(10,2) == 10

def test_maximo3():
  assert maximo(-3,-5) == -3

def test_maximo4():
  assert maximo(5,5) == 5
