import math, os


os.system("cls")

suma =0
resta=0
multiplicacion=0
divicion=0



print("operaciones basicas:\n1.- suma\n2.- resta\n3.- multiplicacion\n4.- divicion\n")

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

menu=int(input("ingrese la operacion a realizar (1/2/3//4/): "))


if menu==1:
    suma =num1+num2
print("La suma es: ", suma)

if menu==2:
    resta = num1 - num2
print("La resta es: ",resta)

if menu==3:
    multiplicacion = num1 * num2
print("La multiplicacion es: ", multiplicacion)

if menu==4:
    divicion = num1 / num2
print("La divicion es: ", divicion)
