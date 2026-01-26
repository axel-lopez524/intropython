import math, os


os.system("cls")


print("calificaciones")

contador=1
suma=0
while contador<=5:
    calificacion =int(input("ingrese la calificacion {contador}: "))
    suma= suma + calificacion
    contador+=1
    
    
promedio = suma /5
print("promedio:",promedio)



