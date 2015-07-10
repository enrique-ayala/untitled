__author__ = 'enrique'


while True:
    num = int(input("Enter a number: "))

    if num > 1:
        for x in range(2,num):
            residuo= num%x
            if residuo == 0:
                print(x)
                print("No es numero primo ")
                break

        else:
            print("Si es primo")
