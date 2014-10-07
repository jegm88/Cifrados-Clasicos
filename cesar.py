#Cifrado cesar
cr = ''
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = 1
ta = len(alfabeto)

print("Digite el mensaje a cifrar:")
m = input()
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