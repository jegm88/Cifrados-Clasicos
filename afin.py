#Cifrado afin
cr = ''
print("Digite el mensaje a cifrar:")
mensaje = input().lower()
print("Digite la constante de decimación:")
a = int(input())
print("Digite el nro. desplazamiento:")
b = int(input())
print("Digite el nro. caracteres del alfabeto:")
m = int(input())

for c in mensaje:
	nc = (ord(c)-97)
	if (nc >= 0 and nc < m) or c == ' ':
		if c != ' ':
			val = (nc*a+b)%m
			cr += chr(val+97)
		else:
			cr += ' '
print(cr)