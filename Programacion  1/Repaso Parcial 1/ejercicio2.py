import random 

lista = ['boca','copa','libertadores','fluminense','cuatro','noviembre']


word = random.choice(lista) #Randomizar la seleccion de la palabra.

max_trys= 7 #Cantidad maxima de intentos para advinarla

letters_adivinadas=["_"] * len(lista) #Se pone un _ por la cada palabra que tenga que advinar el usuario

print("Bienvenido al juego de adivinar la palabra (Version Final Copa Libertadores)")

while max_trys> 0 and "_" in letters_adivinadas:  #Mientras los intentos no se acaben y haya palabras que adivinar
    
    print("Palabra:" + " ".join(letters_adivinadas)) #Muesta el estado de la palabra a adivinar ej: a_ecedar_o 


    letter=input("Ingrese una letra: ").lower() #La pasa del formato en que este a minusculas.


    if letter in word:
        #Ciclo for para actualizar las letras adivinadas:
        for i in range(len(word)): #Para i hasta len de la palabra
            if word[i]==letter:
                letters_adivinadas[i]=letter   
    else:
        #Si la letra no esta en la palabra resta los intentos maximos
        max_trys-=1
        print('Letra incorrecta.Te quedan' ,max_trys,'intentos')
 
 #Si no quedan espacios para adivinar has acertado si no no.
if "_" not in letters_adivinadas:
    print('Has adivinado la palabra. La cual era:', word)
else:
    print('No has adivinado la palabra la palabra era:', word)