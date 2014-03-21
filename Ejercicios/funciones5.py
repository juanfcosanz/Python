import math
import random

def volumen_cubo(lado):
	return lado ** 3

s = 2
print("Volumen de un cubo por lado ",s," is ", volumen_cubo(s),".")

def random_dice():
	die1 = random.randrange(1, 7)
	die2 = random.randrange(1, 7)
	return die1 + die2

print("Suma de dos numeros random : ",random_dice())
print("Suma de dos numeros random : ",random_dice())
print("Suma de dos numeros random : ",random_dice())

def volumen_esfera(radio):
	return (4.0/3.0) * math.pi * (radio ** 3)

r = 2
print("El volumen de la esfera de radio: ",r," es ", volumen_esfera(r))

def  es_maty(nombre):
	if nombre == "Mary":
		print("Entontramos a mary")
	else:
		print("No es Mary")

es_maty("Mary")
es_maty("Fred")