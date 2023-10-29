# A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.


mylist= [10,5,16,7,10,9,8,40,11,44,19]



num= int(input('Ingrese un numero:'))

if num in mylist:
    mylist.remove(num)
    print(mylist)
else:
    print('El numero ingresado no esta en la lista, por lo tanto no puede ser eliminado. :( ')