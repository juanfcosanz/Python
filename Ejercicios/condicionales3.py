vel = int (input ("Ingresa tu velocidad actual: "))

if vel > 70:
	print("\n Multado !")
	multa = (vel - 70 )* 20
	print("\n Tu multa es de: %.2f" %multa)