from functions import *

while True:
    print("Bienvenido al pali detector!")
    print("Escribe una palabra y revisaremos si es palíndromo")
    print("Presiona [1] y enter para salir")
    xd = input("Escribe una palabra: ")
    if xd == 1:
        pass
    elif pal_detect(xd):
        print(str(xd) + " es un palíndromo!")
    else:
        print("muerete pedazo de basura")
