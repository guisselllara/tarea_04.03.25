# Solicitar la palabra al usuario
palabra = input("Ingresa una palabra: ").lower()

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
