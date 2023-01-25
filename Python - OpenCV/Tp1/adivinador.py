import random

def adivina(intentos):
	rdn = random.randint(0,100)
	
	i=0
	while i<intentos :
	
		numero= int(input("ingrese un numero entre 0 y 100: "))
		
		if numero==rdn:
			print("adivinaste")
			print("el numero de intentos fue {}".format(i))
			break
		else:
			print("segui participando")
			i+=1
	else:
		print("se acabaron los intentos")
	
	
	

intentos=int(input("Ingrese un numero de intentos: "))
adivina(intentos)
