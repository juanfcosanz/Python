#!/usr/bin/env python
# encoding: utf-8
# Este archivo usa el encoding: utf-8

#Ejmplo de condiciones

#Retorna verdadero si el año es biciesto

def es_ano_bisiseto(ano):
	if (ano % 400) == 0:
		return True
	elif (ano % 100) == 0:
		return False
	elif (ano  % 4) == 0:
		return True
	else: 
		return False

ano = 2014
ano_bisiesto =  es_ano_bisiseto(ano)
if ano_bisiesto:
	print (ano , " is año bisiesto")
else:
	print (ano , " no es año bisiesto")