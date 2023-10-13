phrase_or_word=input('Ingrese una frase o palabra: ')

caracter_under_four= '?'

caracter_four= '!'

if len(phrase_or_word)==4:
    print((phrase_or_word+caracter_four))
else:
    print((phrase_or_word + caracter_under_four))

