
landslide = int(input("Ingrese el corrimiento deseado: ")) #Se ingresa la cantidad de lugar a correr

# Ciclo for para encriptar los 5 numeros
for i in range(5):
    message = input(f"Ingrese el mensaje {i + 1}: ")
    encrypted_message = ''
    
    for letter in message:
        if letter.isalpha():  # Verifica si es una letra
            mayus = letter.isupper()  # Verifica si es mayúscula o minúscula
            letter = letter.upper() 
            alfabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z') #Tupla alfanumerica
            if letter >= 'A' and letter <= 'Z':  #Si esta entre la A-Z
                index = alfabet.index(letter) 
                encrypted_index = (index + landslide) % 27  #Asegura que esta en el rango alfabetico 
                encrypted_letter = alfabet[encrypted_index]
                if not mayus:     
                    encrypted_letter = encrypted_letter.lower()
                encrypted_message += encrypted_letter
        else:
            encrypted_message += letter  # Conserva otros caracteres sin cambios

    print(f"Mensaje encriptado: {encrypted_message}") #Muestra el mensaje ya encriptado



total_pairs = 0
odd_totals = 0

while True:  #Mientras el numero sea  distinto 0 se pedira otro numero
    number = int(input("Ingrese un número entero positivo (o 0 para salir): "))

    if number == 0:
        break

    pairs = 0  #Cantidad inicial de pares y impares
    odds = 0

    # Calcular la cantidad de dígitos pares e impares en el número
    while number > 0:
        digit = number % 10  #Se obtiene el primer digito

        if digit % 2 == 0:
            pairs += 1
        else:
            odds += 1

        number //= 10  # Elimina el último dígito

    print(f"Dígitos pares: {pairs}, Dígitos impares: {odds}")

    # Actuliza la cantidad total 
    total_pairs += pairs
    odd_totals += odds

# Muestra  la cantidad total de dígitos pares e impares
print(f"Total de dígitos pares: {total_pairs}")
print(f"Total de dígitos impares: {odd_totals}")