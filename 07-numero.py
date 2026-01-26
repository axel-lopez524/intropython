import math, os


os.system("cls")



numero=int(input("ingresa un numero entre 1 y 100"))



while numero < 1 or numero > 100:
   
       print("el numero es incorrecto  ")
       numero = int(input("intenta de nuevo y elige un numero entre el 1 y 100: "))
       
    
    
print("numero valido: ",numero)  

    