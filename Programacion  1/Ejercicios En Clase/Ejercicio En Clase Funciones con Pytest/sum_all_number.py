import sum_figures



while True:
     num= int(input('Ingrese un numero o ingrese 0 para finalizar.'))

     sum_numbers= 0

     if num!=0:
          sum_numbers+=num
          print('La suma de los digitos de',num, 'es:', sum_figures(num))
     else:
          break
     

print('La suma de todos los numeros ingresados es:' , sum_numbers)

print('La suma de los digitos es: ', sum_figures(sum_numbers))