def validate_ID(number):
    if number.isdigit() and 7 <= len(number) <= 8:
        return True
    else:
        return False




number = input("Ingrese su número de DNI sin puntos: (Ej: 40923045)")

if validate_ID(number):
    print(f'El DNI ingresado es válido y es: {number}')
else:
    print('El número ingresado no es válido')
