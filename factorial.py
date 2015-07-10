__author__ = 'enrique'


def factorial(number):
    if (number < 0):
        print("No numeros negativos")
    elif number == 0:
        print (1)
    else:
        facto=1
        for x in range(1,number+1):
            facto=facto*x
        print(facto)

factorial()
