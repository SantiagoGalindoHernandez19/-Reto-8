
import math # Importamos libreria math
def sin_aprox(x, n): # Llamamaos a la funcion seno 
    aproximacion = 0 # Girando entorno al valor 0
    for i in range(n): # Definimos el rango i
        estimado = ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i+1) #Formula de serie segun Maclaurin
        aproximacion += estimado  
    return aproximacion # Devulta la funcion 


if __name__ == "__main__":

    x = float(input("Ingresar el valor de x: "))    
    n = int(input("Ingrese el número de términos de la serie:  ")) # Establecemos parametros a pedir 

    real = math.sin(x) # Funcion seno
    resultado = sin_aprox(x, n) # Funcion aproximacion seno
    print("El valor real es:",real) #Impresion resultados 
    print("Su aproximación es:",resultado)
    print("La diferencia es:",(real - resultado))     


    