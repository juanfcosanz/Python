def pig_lating(word):
	vocales = ["a", "e","i","o","u"]
	n = 0
	pal = word[0]
	encontrado = False

	if pal.isalpha() != True:
		encontrado = "num"
		print(" --> Error.. ingresaste un valor incorrecto !!")
	else:
		while n<=4:
			if pal == vocales[n]:
				encontrado = True
			n = n + 1
	return encontrado


def init():
	word = ""
	word = input("Ingresa una Palabra: ").lower()
	encontrado = pig_lating(word)
	if encontrado == "num":
		word=""
		init()
	elif encontrado == True:
		word = word + "way"
	else:
		word = word + "ay"
	print(word)

init()