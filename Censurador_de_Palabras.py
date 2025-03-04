# Solicitar una frase y la palabra a censurar
frase = input("Ingresa una frase: ")
palabra_censurada = input("Ingresa la palabra a censurar: ")

# Reemplazar la palabra prohibida por asteriscos
frase_censurada = frase.replace(palabra_censurada, '**')

# Imprimir la frase censurada
print("Frase censurada:", frase_censurada)
