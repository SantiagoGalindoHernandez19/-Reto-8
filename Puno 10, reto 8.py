
import math # Importamos libreria math

def arctan_aprox(x, n): # Se llama a la funcion 
    if x < -1 or x > 1:
        raise ValueError("rango pedido [-1, 1]") # En caso de que no se registre el tando solicitado    
    aproximacion = 0 # Girando entorno al valor 0
    for i in range(n):
        estimado = ((-1)**i) * (x**(2*i+1)) / (2*i+1) #Formula de serie segun Maclaurin
        aproximacion += estimado  
    return aproximacion # Devulta la funcion 


if __name__ == "__main__":

    x = float(input("Ingresar el valor de x entre un rango de [-1, 1]:  "))    
    n = int(input("Ingrese el número de términos de la serie:  ")) # Establecemos parametros a pedir 

    real = math.atan(x) # Funcion acortangente 
    resultado = arctan_aprox(x, n) # Funcion aproximacion seno
    print("El valor real es:",real) #Impresion resultados 
    print("Su aproximación es:",resultado)
    print("La diferencia es:",(real - resultado))     
