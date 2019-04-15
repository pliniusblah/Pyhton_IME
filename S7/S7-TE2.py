import math

def é_hipotenusa(hip,cat):
  if hip > cat and (math.sqrt((hip**2)-(cat**2)) % 1) == 0 and (math.sqrt((hip**2)-(cat**2))) != 0:
    return True
  else:
    return False

def soma_hipotenusas(n):
  hip = 1
  cat = 1
  total = 0
  while hip <= n:
    while cat <= n:
      if é_hipotenusa(hip,cat):
        total += hip
        #print(hip)
        break
      cat += 1
    hip += 1
    cat = 1
  return total

print(soma_hipotenusas(25))