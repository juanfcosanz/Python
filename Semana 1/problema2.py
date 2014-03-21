def pig_lating(word):
	vocales = ["a", "e","i","o","u"]
	n = 0
	pal = word[0]
	encontrado = False
	
	while n<=4:
		if pal == vocales[n]:
			encontrado = True
		n = n + 1
	return encontrado

word = input("Ingresa una Palabra: ")
encontrado = pig_lating(word)

if encontrado:
	word = word + "way"
else:
	word = word + "ay"

print("\n --> ",word)