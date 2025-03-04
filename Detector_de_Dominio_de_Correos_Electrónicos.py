# Solicitar al usuario el correo electrónico
correo = input("Ingresa tu correo electrónico: ")

# Verificar el dominio usando endswith()
if correo.endswith("@gmail.com"):
    print("El proveedor del correo es Gmail.")
elif correo.endswith("@outlook.com"):
    print("El proveedor del correo es Outlook.")
elif correo.endswith("@yahoo.com"):
    print("El proveedor del correo es Yahoo.")
else:
    print("El proveedor del correo es Otro.")
