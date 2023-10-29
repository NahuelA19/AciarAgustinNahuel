# Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.



my_num_list= []

while True:

 num =int (input('Ingrese numeros (Para finalizar ingrese 0 : ') )
 
 my_num_list.append(num)
 
 

 if num == 0 :
  my_num_list.remove(0)
  print(my_num_list)
  break



