#!/usr/bin/python

from random import randint
mes = "\0"

for x in range(6):
    mes = mes + str(randint(0,9))
    
print "Lotto number is >> %s <<" % mes
mes1 =[]

for x in range(4):
    mes2 = ""
    for y in range(3):    
        mes2 = mes2 + str(randint(0,9))
        
        
    mes1.append(mes2)
    mes2 = ""
print "Lotto number is >> %s <<" % mes1