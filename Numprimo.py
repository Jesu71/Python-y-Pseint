def primos(inicio, fin):
  for i in range(inicio, fin+1):
    if i > 1:
      for j in range(2, i):
          if (i%j) == 0:
              break
      else:
          print(i)

primos(1, 100) 