age= int(input('Ingrese la edad de la persona que solicita la jubilacion:'))
ages_worked= int(input('Ingrese la cantidad de años trabajados:'))



if  age>60 and ages_worked<25:
    print("La jubilacion es por edad")
elif age<60 and ages_worked>25:
    print("La jubilacion es por antiguedad joven")
elif age>60 and ages_worked>25:
    print('La jubilacion es por antiguedad adulta')