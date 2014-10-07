#Cifrado cesar
cr = ''
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = 1
m = len(alfabeto)

print("Digite el mensaje a cifrar:")
mensaje = input()
print("Digite el nro. desplazamiento:")
b = int(input())

for c in mensaje:
	if c.upper() in alfabeto:
		nc = (alfabeto.index(c.upper()))
		if (nc >= 0 and nc < m) or c == ' ':
			if c != ' ':
				val = (nc*a+b)%m
				if c.isupper():
					cr += alfabeto[val].upper()
				else:
					cr += alfabeto[val].lower()
			else:
				cr += ' '
	else:
		cr += c
print(cr)