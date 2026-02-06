import math, os


os.system("cls")

triangulo =0
cuadrado =0
circulo =0
pentagono =0


print("area de figuras:\n1.- triangulo\n2.- cuadrado\n3.- circulo\n4.- pentagono\n5.- salir")

menu=int(input("ingrese la figura a realizar (1/2/3//4/5/): "))


if menu==1:
    base=int(input("Ingresa la base: "))
    altura=int(input("Ingresa la altura: "))
    
    triangulo=(base * altura)/2
    
    print("el area es: ", triangulo)

if menu==2:
    base=int(input("Ingresa la base: "))
    altura=int(input("Ingresa la altura: "))
    
    cuadrado= base * altura
    
    print("el area es: ", cuadrado)


    
if menu==3:
    radio=int(input("Ingresa el radio: "))
    
    
    circulo=3.1416 * (radio ** 2)
    
    print("el area es: ", circulo)
    
 
if menu==4:
    perimetro=int(input("ingresa el perimetro: "))
    apotema=int(input("ingresa el apotema: "))
    
    pentagono = (perimetro * apotema)/2
    
    print("el area es: ", pentagono)
    
    
if menu==5:
    input("bye")
        