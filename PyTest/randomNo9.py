#!/usr/bin/python

from random import randint
mes = "\0"
print "Lotto with 9 at last digit"

for x in range(5):
    mes = mes + str(randint(0,9))
mes = mes + "9"
    
print "First prize Lotto number is >> %s <<" % mes
mes1 =[]

for x in range(4):
    mes2 = ""
    for y in range(2):    
        mes2 = mes2 + str(randint(0,9))
        
    mes2 = mes2 + "9"
    mes1.append(mes2)
    mes2 = ""
print "3 digits Lotto number are >> %s <<" % mes1

for y in range(1):    
    mes2 = mes2 + str(randint(0,9))
mes2 = mes2 + "9"
print "Last 2 digits Lotto number is >> %s <<" % mes2
