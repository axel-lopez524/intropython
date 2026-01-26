import math, os

os.system("cls")

sueldo=0

print("sueldo de la persona: ")

sueldo=int(input("ingresa tu sueldo: "))

if sueldo < 1000:
    print("no paga impuestos ")
    
if sueldo >=1000 and sueldo <= 2000 :
    print("paga el 10% de impuestos ")
    sueldo = (sueldo /100) * 90
    
    print("el sueldo neto es : ",sueldo)
    
    
if sueldo > 2000:
    print("paga el 20% de impuestos ")
    sueldo = (sueldo / 100) * 80
    
    print("el sueldo neto es: ",sueldo)
    
    