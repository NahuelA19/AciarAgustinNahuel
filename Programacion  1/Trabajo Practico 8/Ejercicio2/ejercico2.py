from is_power import is_power


n= int(input('Ingrese el primer numero:'))
b= int(input('Ingrese el segundo  numero:'))




if is_power(n,b):

 print(f'{n} es una potencia de {b}')

else:
 print(f'{n} no es una potencia de {b}')