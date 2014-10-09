#Cifrado afin
archivo = open('alfabeto1.txt','r')
#alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto = archivo.read().split(',')
archivo.close()
ta = len(alfabeto)
cr = ''

print("Digite el mensaje a cifrar:")
m = input()
print("Digite la constante de decimación:")
a = int(input())
print("Digite clave de cifra (K):")
k = int(input())

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