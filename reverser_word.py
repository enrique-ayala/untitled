__author__ = 'enrique'

'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Michele

Then I would see the string:

Michele is name My

http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

'''

def reverse(str):
    lista=str.split(" ")
    length= len(lista)
    rever=[]
    while length > 0:
        rever.append(lista[length-1])
        length-=1

    print(" ".join(rever))



x=input("Ingresa string:")
reverse(x)
