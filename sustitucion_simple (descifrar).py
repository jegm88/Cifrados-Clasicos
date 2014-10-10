#Descifrado sustitucion simple
cr = ''
archivo = open('alfabeto1.txt','r')
alfabeto1 = archivo.read().split(',')
archivo.close()

archivo = open('alfabeto2.txt','r')
alfabeto2 = archivo.read().split(',')
archivo.close()

if len(alfabeto1)!=len(alfabeto2):
	print("Los alfabetos deben tener la misma cantidad de letras!!!")
else:
	print("Digite el mensaje a descifrar:")
	m = input()

	for c in m:
		if c.upper() in alfabeto2:
			nc = (alfabeto2.index(c.upper()))
			if c != ' ':
				if c.isupper():
					cr += alfabeto1[nc].upper()
				else:
					cr += alfabeto1[nc].lower()
			else:
				cr += ' '
		else:
			cr += c
	print(cr)