__author__ = 'enrique'
# Python Program to find the factors of a number

def factors(number):
    if number > 0:
        for x in range(1,number+1):
            if number%x == 0:
                print(x)

factors(320)