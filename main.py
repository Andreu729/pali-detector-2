from functions import *

while True:
    print("Bienvenido al pali detector!")
    print("Escribe una palabra y revisaremos si es palíndromo")
    print("Presiona [1] y enter para salir")
    xd = input("Escribe una palabra: ")
    if str(xd) == "1":
        break
    elif pal_detect(xd):
        print(str(xd) + " es un palíndromo!")
    else:
        print("no es un palíndromo")
