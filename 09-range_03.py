import os


os.system ("cls")

resultado = 0
contador = 0


a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

while contador < b:
    resultado = resultado + a
    contador = contador + 1

print("Resultado:", resultado)