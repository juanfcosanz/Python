# encoding: utf-8

import random

def num_gen_tilka():
	num1 = random.randrange(1 , 59)
	num2 = random.randrange(1 , 59)
	num3 = random.randrange(1 , 59)
	num4 = random.randrange(1 , 59)
	num5 = random.randrange(1 , 59)
	num6 = random.randrange(1 , 35)
	mensaje = "Hoy los números son %d, %d, %d, %d, %d " %(num1,num2,num3,num4,num5) + " y el número mágico final es %d " %num6
	return mensaje


tk = num_gen_tilka()
print(tk)