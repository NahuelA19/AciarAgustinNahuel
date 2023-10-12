import random #Import para randomizar la seleccion de la palabra 


words=["armani","rulli","martinez","molina","montiel","romero","pezzella","otamendi","acuña","tagliafico","foyth"," de paul","paredes","mac allister","rodriguez","gomez","fernandez","palacios","almada","di maria","alvarez","dybala","correa","messi" ]

# Funcion para poder seleccionar de manera aleatoria un apellido de la lista
def select_word(words):
    return random.choice(words) #Retorna un apellido seleccionado de la lista de manera aleatoria 

# Función Juego ahorcado 
def juego_ahorcado():
    secret_word = select_word(words) #La palabra secreta es la palabra seleccionada previamente por la funcion select
    trys_max = 6  # Número máximo de intentos para poder adivinar las palabras del apellido del jugador
    letters_guessed = [] #Se guardan las letras adivinadas del apellido del jugador

    print("Bienvenido al juego del ahorcado version Campeones del Mundo Qatar 2022: (Adivine el apellido del jugador) ")
    
    while trys_max > 0: #Mientras los intentos maximos no sean 0 
        showed_letter = "" #En un comienzo letras mostradas sera un espacio vacio.
        for letter in secret_word: #Para letra en palabra secreta
            if letter in letters_guessed: #Si letra en letras adivinadas
                showed_letter += letter #letras mostradas  +1 
            else:
                showed_letter += "_" #Si no se queda como estaba.
        
        print(showed_letter)
        letter = input("Adivina una letra del apellido: ").lower() #Letras es igual a la letra ingresada por el usuario 
 
        if letter in secret_word:  #Si la letra ingresada por el usuario esta en la palabra secreta
            letters_guessed.append(letter) 
            print("¡Adivinaste una letra!") #Se mostrara un mensaje 
        else:                                                #Si no se restara un intento y se mostrara por pantalla
            trys_max -= 1 
            print("La letra ingresada no esta en el apellido del jugador, te quedan {} intentos.".format(trys_max))

        if set(letters_guessed) == set(secret_word):           #Si la letras adivinadas son iguales a la palabra secreta 
            print("¡Felicidades! ¡Has adivinado el apellido.El campeon del mundo es: '{}'".format(secret_word))  #Se mostrara un mensaje de felicitaciones con el apellido del jugador
            break

    if trys_max == 0:
        print("¡Has perdido! el campeon del mundo  era: '{}'".format(secret_word)) #Si se acaban los intentos se mostrara un mensaje.

#Se llama a la funcion para iniciar el juego
juego_ahorcado()