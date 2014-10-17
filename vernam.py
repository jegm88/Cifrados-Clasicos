def convertir_cadena_a_binario(cadena):
	resultado = ''
	for c in cadena:
		ascii = ord(c)
		bin = "{0:08b}".format(ascii)
		resultado += bin+' '
	return resultado[:-1]

def convertir_binario_a_cadena(binario):
	letras = binario.split(' ')
	cadena = ''
	for letra in letras:	
			entero = int(letra,2)
			ascii = chr(entero)	
			cadena += ascii
	return cadena

def cifrar(mensaje,key,tipo):
	if(tipo == 1):
		mCl = convertir_cadena_a_binario(mensaje)
	else:
		mCl = mensaje
	k = convertir_cadena_a_binario(key)

	criptograma = ''

	if (len(mCl.split(' '))<=len(k.split(' '))):
		
		for i in range(len(mCl)):
			if (mCl[i]!= ' '):
				c = int(mCl[i])
				ll = int(k[i])
				xor = (bool(c) != bool(ll))
				criptograma +=str(int(xor))
			else:
				criptograma += ' '
		return criptograma
	else:
		if(tipo == 1):
			print("Error: La clave es mas pequeña que el tamaño del mensaje")
		else:
			print("Error: La clave es mas pequeña que el tamaño del criptograma")
		return


#Inicio del programa

#Carga de mensaje
archivo = open('mensaje.txt','r')
mensaje = archivo.read()
archivo.close()

#Carga de clave
archivo = open('clave.txt','r')
clave = archivo.read()
archivo.close()

archivo = open('criptograma.txt','r')
criptograma = archivo.read()
archivo.close()

print('======================')
print('Cifrado Vernam')
print('======================')
print('Presione:')
print('1. para cifrar')
print('2. para descifrar')
print('Cualquier tecla para salir')
opc = input()
if(opc == '1'):
	criptograma = cifrar(mensaje,clave,1)
	if(criptograma != None):
		archivo = open('criptograma.txt','w')
		archivo.write(criptograma)
		archivo.close()
		print ('Archivo criptograma.txt creado correctamente!!!')
	else:
		print ('Error: No se pudo crear el criptograma!!!')
elif(opc == '2'):
	mensaje = convertir_binario_a_cadena(cifrar(criptograma,clave,2))
	if(mensaje != None):
		archivo = open('mensaje.txt','w')
		archivo.write(mensaje)
		archivo.close()
		print('Archivo mensaje.txt creado correctamente!!!')
	else:
		print ('Error: No se pudo crear el mensaje!!!')