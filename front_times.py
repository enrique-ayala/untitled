__author__ = 'enrique'

'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
    string=''
    for x in range(1,n+1):
        if len(str)>2:
            string=string+str[:3]
        else:
            string=string+str

    return string

print (front_times('Chocolate', 3))
print (front_times('A', 4))
print (front_times('Ab', 4))