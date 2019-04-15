def maximo(a,b,c):
  if a > b:
    if a > c:
      return a
    else:
      return c
  else:
    if b > c:
      return b
    else:
      return c

def test_func0():
  assert maximo(30,14,10) == 30

def test_func1():
  assert maximo(0,-1,1) == 1