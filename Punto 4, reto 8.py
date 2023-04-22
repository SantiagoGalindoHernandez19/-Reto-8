
from math import factorial # Llamamos la biblioteca usando math para el factorial

x = int(input("Ingrese un Numero: ")) #Pedimos ingreso del numero
range(1, x+1) #Definimos el rango para que empiece desde el 1
for n in range(1, x+1): # Definicion variable n
    print(n, factorial(n)) # Impresion valores con ayuda de la funcion factorial

