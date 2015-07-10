__author__ = 'enrique'
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

'''
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
  str_time=''
  for x in range(1,n+1):
     str_time= str_time + str
  return str_time

print (string_times('Hi', 2))
print (string_times('Hi', 0) )

x= list(range(1,1))
print (x)
