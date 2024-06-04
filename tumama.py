from functions import *

print("Bienvenido al pali detector!")
print("Escribe una palabra y revisaremos si es palíndromo:")
xd = input("Escribe una palabra: ")
if pal_detect(xd):
    print(xd + " es un palíndromo!")
else:
    print("muerete pedazo de basura")
