num1= int(input('Ingrese un numero:'))
num2= int(input('Ingrese otro numero:'))

if num1 == num2 :
  mult_nums= (num1*num2)
  print('Ambos numeros son iguales: El resultado de multiplicarlos es:', mult_nums)
else:
   if num1>num2:
      rest_nums= num1-num2
      print('El numero 1 es mas grande que el numero 2: El resultado de restar el primero con el segundo es de:' , rest_nums)