'''
imprimir 5 sueldos, agregar a la lista e imprimir
'''
import math, os

sueldos=[]
promedio=0
cont=0
total=0


while  cont<=4:
    temp = float(input("dame el sueldo"+str({cont +1})))
    sueldos.append(temp)
    cont+=1
    total += temp
    

    
print("los sueldos son: ", str (sueldos))

promedio = promedio + total / 5
print("promedio:",promedio)


mayor=max(sueldos)
menor=min(sueldos)

print("el sueldo mas alto es: ",mayor)
print("el sueldo menos es : ",menor)



