
x=int(input("ingrese un numero: ")) #Exponente
n=int(input("ingrese un numero: ")) #Base
producto = 1 # Empezamos comandando la variable 1
for i in range(x): #Defiinicion del rango
    producto = n**i #Elevamos la potencia
    print ("La base", n ,"elevado a la potencia", x , "da como resultado", producto) #Impresion de resultado

