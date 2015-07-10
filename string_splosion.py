__author__ = 'enrique'

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

'''

def string_splosion(str):
    splosion =''
    for x in range(0,len(str)):
        splosion=splosion+str[:x+1]

    return splosion

print (string_splosion('Code'))
print (string_splosion('There') )
print (string_splosion('ab') )
