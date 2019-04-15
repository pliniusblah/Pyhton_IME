def fizzbuzz(numero):
  if ((numero % 3) == 0) and ((numero % 5) == 0):
    return "FizzBuzz"
  else:
    if ((numero % 3) == 0) or ((numero % 5) == 0):
      if ((numero % 3) == 0):
        return "Fizz"
      else:
        return "Buzz"
    else:
      return numero

def test_func0():
  assert fizzbuzz(3) == "Fizz"

def test_func1():
  assert fizzbuzz(5) == "Buzz"

def test_func2():
  assert fizzbuzz(15) == "FizzBuzz"

def test_func3():
  assert fizzbuzz(4) == 4