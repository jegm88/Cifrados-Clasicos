#Cifrado cesar
def ejecutar_cesar(alfabeto,ta,m,k):
	cr = ''
	a = 1

	for c in m:
		if c.upper() in alfabeto:
			nc = (alfabeto.index(c.upper()))
			if (nc >= 0 and nc < ta) or c == ' ':
				if c != ' ':
					val = (nc*a+k)%ta
					if c.isupper():
						cr += alfabeto[val].upper()
					else:
						cr += alfabeto[val].lower()
				else:
					cr += ' '
		else:
			cr += c
	print(cr)


archivo = open('alfabeto1.txt','r')
alfabeto = archivo.read().split(',')
archivo.close()
p_ciclo = False
ta = len(alfabeto)

print("Digite el mensaje a cifrar:")
m = input()
print("Digite clave de cifra (K):")
k = int(input())

if(k>=0):
	if k>=ta:
		if p_ciclo:
			k = k%ta
			ejecutar_cesar(alfabeto,ta,m,k)
		else:
			print("La clave no puede ser superior a la cantidad de digitos del alfabeto!!!")
	else:
		ejecutar_cesar(alfabeto,ta,m,k)
else:
	print("La clave debe ser mayor a 0")