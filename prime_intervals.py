__author__ = 'enrique'

# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for x in range(lower,upper+1):
    for y in range(2,x):
        if x%y == 0:
            #print "Numero no primo",x," ",y
            break
    else:
        print x


