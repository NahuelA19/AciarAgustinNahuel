name = input('Ingrese su nombre por favor: ') #Se pide el nombre y lo guarda en name
print('Bienvenido', name)  #Saluda con el nombre
 
while True:  #Mientras la condicion sea verdadera 
    print('Menu de opciones:')
    print('1- Juego de Numeros.')    #Se imprime el menu de opciones para que el usuario seleccione una 
    print('2- Juego de Palabras.')
    print('3- Para salir.')

    option = input(f"Por favor {name}, seleccione una de las opciones (1, 2 o 3): ")  #Se guarda en option la opcion elegida por el usuario 

    if option == '1':  #Si la opcion es uno 
        numbers = []  #Se crea una lista vacia para almacenar los numeros 
        while True:   #Mientras la condicion sea verdadera 
            number = int(input(f'{name}, ingrese un número entero, 0 para terminar: ')) #Se pide al usuario que ingrese un numero entero que sera guardado en number 
            if number == 0:  
                break              #Si numero es 0 se rompe el bucle 
            numbers.append(number)  #Se añade los numeros ingresados por el usuario a la lista numbers que empieza vacia

        even_numbers = [num for num in numbers if num % 2 == 0]  #Lista de numeros que cumplen la condicion para ser pares
        odd_numbers = [num for num in numbers if num % 2 != 0]  #Lista de numeros que cumplen la condicion par ser impares

        if even_numbers:   #Si los numeros son pares
            max_pair = max(even_numbers) #El numero mayor es el numero mas grande de la lista de numeros pares 
            print(f'{name},el número par más grande es: {max_pair}')  #Se muestra al usuario el numero mas grande 

        if odd_numbers:  #Si los numeros son impares: 
            average_odd = sum(odd_numbers) / len(odd_numbers) #El promedio de los numeros impares es igual a la suma de los mismos dividiendolos por la cantidad de elementos que hay en la lista de impares
            print(f'{name},el promedio de todos los números impares es de:', average_odd) #Se muestra al usuario el promedio 

    elif option == '2':        #Si la opcion es 2: 
        phrase = input(f'Por favor {name}, ingrese una frase: ')   #Se pide al usuario que ingrese una frase 
        phrase = phrase.lower()                                    #Se pasa a minusculas toda la frase.

        vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}         # Tupla con las vocales con valor inicial 0 
        for letter in phrase:                                          #Para letra en la frase
            if letter in vocals:
                vocals[letter] += 1                                  #Si la letra es vocal se suma un valor a la letra en la tupla

        print(f'{name},la cantidad de esa vocal en la frase es:')
        for vocal, cant in vocals.items():                           #Se imprime la cantidad de vocales que hay en la lista 
            print(vocal, cant)

    elif option == '3':                                              #Si la opcion es 3 se imprime un mensaje y asi se cierra el juego:
        print(f'Bien jugado {name}. Adios.')
        break

    

    





