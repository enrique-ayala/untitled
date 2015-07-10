__author__ = 'enrique'

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for number_ in range(lower,upper+1):
    cociente=number_
    suma=0
    while cociente > 0:
        residuo=cociente%10
        suma=suma+pow(residuo,3)
        cociente = cociente // 10

    if suma == number_:
        print("numero armstrong",number_)
