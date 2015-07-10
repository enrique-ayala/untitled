__author__ = 'enrique'

# Program to ask the user for a range and display all Armstrong numbers in that interval
#http://www.programiz.com/python-programming/examples/armstrong-interval
# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for number in range(lower,upper+1):
    coc=number
    suma=0
    while coc > 0:
        residuo= coc%10
        suma= suma+pow(residuo,3)
        coc= coc // 10
    if suma == number:
        print ("Numero armstrong",number)
