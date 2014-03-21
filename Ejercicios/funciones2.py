#Modulo aritmetico 


num = 49
tens = num // 10
ones = num % 10
print (tens,ones)
print(10 * tens + ones , num)


#aplicaion - 24 horas

hour = 20
shift = 8
print((hour + shift) % 24)

#aplicaion wraparound

width = 800
position = 797
move = 5
position =  (position +move) % width
print(position)

#converciones
#convetir un entero a string con str
hour = 3
ones = hour % 10
tens = hour // 10
print (tens,ones,":00")
print (str(tens), str(ones),":00")
print (str(tens) + str(ones) + ":00")


#python modulos

#import simplegui -> no sirve aki

import math

import random


print (math.pi)