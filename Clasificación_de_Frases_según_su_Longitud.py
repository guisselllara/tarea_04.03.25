# Solicitar una frase al usuario
frase = input("Ingresa una frase: ")

# Obtener la longitud de la frase
longitud = len(frase)

# Clasificar la frase según su longitud
if longitud < 20:
    print("La frase es Corta.")
elif 20 <= longitud <= 50:
    print("La frase es Media.")
else:
    print("La frase es Larga.")
