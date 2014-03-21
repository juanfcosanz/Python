#Funciones


#area de un triangulo
def area_triangulo(base,altura):
	area = (base * altura) / 2
	return area;


a1 = area_triangulo(3,8)
print(a1)
a2 = area_triangulo(14,2)
print(a2)


#Convetir oF a oC
def fahrenheitTocelsius(fahrenheit):
	celcius = (5.0 / 9) * (fahrenheit - 32)
	return celcius

c1 = fahrenheitTocelsius(32)
c2 = fahrenheitTocelsius(212)

print (c1,c2)


#Convertir oF a oK
def fahrenheistToKelvin(fahrenheit):
	celcius = fahrenheitTocelsius(fahrenheit)
	kelvin = celcius + 273.15
	return kelvin

k1 = fahrenheistToKelvin(32)
k2 = fahrenheistToKelvin(212)

print(k1,k2)


#saludo
def hello():
	return "Hola a todos"

s1 = hello()
print(s1)