# Hola Mundo con concatenación
message = "CLASE 15 de Marzo de 2022"

print(message, "- Daniel", "LQ")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in number: # Equivalente a un FOREACH se almacena en X lo que contenga NUMBER
	print(x)
''' 
- Generar los número naturales menores o iguales a 10
- Utilizar FOR
- Salida 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
'''
result = ""

for i in range(0, 10, 1): # FOR variable IN RANGE(inicio, limite, incremento)
	if i == 9:
		result = result + str(i + 1) + "."
	else:
		result = result + str(i + 1) + ", "

print("=> ", result)

''' 
EJERCICIO 1
- Generar los número pares menores o iguales a 20
- Utilizar FOR
- Salida 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
'''
print("CLASS EXERCISE 1")
result = ""
for i in range(2, 21, 2):
	if i == 20:
		result = result + str(i) + "."
	else:
		result = result + str(i) + ", "

print("=> ", result)

''' 
EJERCICIO 1
- Generar los N número naturales
- Utilizar FOR
- Salida 1, 2, 3, 4, 5, ..., N
'''

n = int(input("Ingrese un número: "))
count = 1
result = ""
while count <= n:
	if count == n+1:
		result = result + str(count) + "."
	else:
		result = result + str(count) + ", "

	count += 1

print("=> ", result)

