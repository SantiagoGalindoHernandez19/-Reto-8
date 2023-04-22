
import math # Importamos libreria math

def exp_aprox(x, n): # Llamamaos a la funcion Exponencial
    aproximacion = 0  # Girando entorno al valor 0
    for i in range(n): # Definimos el rango i

        estimado = (x**i) / math.factorial(i) # Comparacion aproximacion obtenida con el valor real 
        aproximacion += estimado
    return aproximacion # Devulta la funcion 

if __name__ == "__main__":

    x = float(input("Ingresar el valor de x: "))    
    n = int(input("Ingrese el número de términos de la serie:  ")) # Establecemos parametros a pedir 

    
    real = math.exp(x) # Funcion exponencial

    
    resultado = exp_aprox(x, n) # Funcion aproximacion exponencial 

   
    print("El valor real es:",real)
    print("Su aproximación es:",resultado)
    print("La diferencia es:",(real - resultado))     



    

