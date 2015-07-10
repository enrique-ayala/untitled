__author__ = 'enrique'
#Maximo comun divisor # Python program to find ighest common factor (H.C.F) or greatest common divisor (G.C.D)

def mcd(numero1,numero2):
     menor=numero2
     if numero1 < numero2:
         menor=numero1

     for divisor in range(1,menor+1):
         if (numero1%divisor==0 and numero2%divisor==0):
             hcf=divisor
     return hcf

print (mcd(54,24))