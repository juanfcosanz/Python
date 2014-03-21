def saludar(amigo,dinero):
	if amigo and (dinero > 20):
		print ("Hi!")
		dinero = dinero - 20
	elif amigo:
		print ("Hello!")
	else:
		print("Ha Ha")
		dinero = dinero + 10
	return dinero


dinero = 15
dinero = saludar(True, dinero)
print ("Dinero: ", dinero)
print ("")

dinero = saludar(False,dinero)
print("Dinero: ", dinero)
print("")

dinero = saludar(True, dinero)
print("Dinero: ", dinero)
print("")