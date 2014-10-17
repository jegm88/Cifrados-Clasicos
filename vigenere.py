def cifrar(alfabeto,mensaje,clave):
	criptograma = ''
	mensaje = mensaje.upper()
	clave = clave.upper()
	for c in range(len(mensaje)):
		if((len(clave)<len(mensaje))):
			cl = c%len(clave)
		else:
			cl = c

		t = len(alfabeto)
		if(mensaje[c] in alfabeto):
			xi = alfabeto.index(mensaje[c].upper())
			zi = alfabeto.index(clave[cl].upper())
			yi = (xi+zi)%t
			criptograma += alfabeto[yi]
		else:
			criptograma += mensaje[c]
	return criptograma

def descifrar(alfabeto,criptograma,clave):
	mensaje = ''
	criptograma = criptograma.upper()
	clave = clave.upper()

	for c in range(len(criptograma)):
		if((len(clave)<len(criptograma))):
			cl = c%len(clave)
		else:
			cl = c

		t = len(alfabeto)
		if(criptograma[c] in alfabeto):
			xi = alfabeto.index(criptograma[c].upper())
			zi = alfabeto.index(clave[cl].upper())
			yi = (xi-zi)%t
			mensaje += alfabeto[yi]
		else:
			mensaje += criptograma[c]
	return mensaje


#Inicio del programa
archivo = open('alfabeto1.txt','r')
alfabeto = archivo.read().split(',')
archivo.close()


print('======================')
print('Cifrado Vigenere')
print('======================')
print('Presione:')
print('1. para cifrar')
print('2. para descifrar')
print('Cualquier tecla para salir')
opc = input()

if(opc == '1'):
	print('Digite el mensaje:')
	m = input()
	print('Digite la clave:')
	k = input()
	print ('Criptograma: '+cifrar(alfabeto,m,k))
elif(opc == '2'):
	print('Digite el criptograma:')
	cr = input()
	print('Digite la clave:')
	k = input()
	print ('Mensaje: '+descifrar(alfabeto,cr,k))
	