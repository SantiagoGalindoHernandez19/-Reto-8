
x = int(input("Ingresa un numero mayor o igual a 2: ")) #Solicitamos al usuario
if x % 2 != 0:  # Cuando el residuo no sea par 
    x -= 1  # Restaremos uno

for i in range (x,1,-2):
        print(x) 