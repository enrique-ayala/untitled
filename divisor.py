__author__ = 'enrique'
#http://www.practicepython.org/solution/2014/07/25/13-fibonacci-solutions.html

def getDivisor(num):
    for x in range(1,num+1):
        if num%x==0:
            print(x)

getDivisor(10)