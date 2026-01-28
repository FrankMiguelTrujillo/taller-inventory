nombre = input("Cual es tu nombre: ")

print(nombre, "bienvenido al juego! Tienes 8 intentos para adivinar un numero del 1 al 100!")



from random import randint


aleatorio = randint (1,101)
print (aleatorio)

lista = list(range(1,101))
intento_max=8

intentos=0
    
for intento in range(1, intento_max + 1):
    try: 
     numero = int(input(f" Intento {intento}:  Escribe el numero: "))
     
     if numero == aleatorio:
         print("ganaste!")
         break
     elif intento == intento_max:
         print("Perdiste! La respuesta era:", aleatorio)
     elif numero not in lista:
         print("Elige un numero valido")
     elif numero > aleatorio:
         print("tu numero es mayor a la respuesta")
     elif numero < aleatorio:
         print("tu numero es menor a la respuesta")
     elif numero not in lista:
         print("Elige un numero valido")
    except ValueError:
        print("Por favor, ingresa un número válido.")
