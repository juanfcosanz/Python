minutos = int ( input(" -> Minutos utlizados: "))

if minutos < 200:
	precio = 0.20
elif minutos <= 400:
	precio = 0.18
elif minutos <=800:
	precio = 0.15
else:
	precio = 0.08

print("\n Total a pagar P/. %6.2f " %(minutos * precio))