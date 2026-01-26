import math, os


os.system("cls")


print("-----grupos ICO201_9, ICO201_14-----")


edad1=int(input("Ingresa la edad de la primera persona: "))
edad2=int(input("Ingresa la edad de la segunda persona: "))

temp1=edad1>edad2 #False
temp2=edad1==edad2 #False
temp3=edad1<edad2 #True


if edad1>edad2:
    print("La primera persona es la mayor")
    
elif edad1<edad2:
     print("La segunda persona es la mayor")
     
else:
    print("Las edades son iguales")





  
    