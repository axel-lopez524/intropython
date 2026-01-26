import math, os


os.system("cls")


print("-----grupos ICO201_9, ICO201_14-----")


num1=input("Ingresa el primer numero: ")
num2=input("Ingresa el segundo numero: ")

suma = int(num1) +int(num2)
print("La suma es : ", suma)

print("operaciones basicas:\n1.- suma\n2.- resta\n3.- multiplicacion\n4.- divicion\n")


opcion=input("ingrese la operacion a realizar (1/2/3//4/): ")

numero1 = 5
numero2 = 3

suma = numero1 + numero2

print("La suma es: ", suma)

resta = numero1 - numero2
print("La resta es: ",resta)
multiplicacion = numero1 * numero2
print("La multiplicacion es: ", multiplicacion)
divicion = numero1 / numero2
print("La divicion es: ", divicion)

Val1=3 
Val2=5

temp=Val1>Val2 #False
temp=Val1==Val2 #False
temp=Val1<Val2 #True
temp=Val1>=Val2 #False
temp=Val1>=Val2 #True
temp=Val1=Val2 #True

print("el valor de la comparacion es: ", temp)

tem2= not (Val1>Val2) #true

print("el valor de la compararcion con NOT es: ", tem2)