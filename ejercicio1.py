for i in range(100):
    numero= i + 1
    if numero % 3 == numero % 5 == 0:
        print("fizzbuzz")
    elif numero % 3 == 0:
        print ("fizz")
    elif numero % 5 == 0:
        print ("buzz")
    else:
     print(numero)