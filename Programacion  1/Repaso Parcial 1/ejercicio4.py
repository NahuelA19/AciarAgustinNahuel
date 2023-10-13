assist_all_month=input('Ingrese si el empleado trabajo todo el mes: (S para si) (N para no)')

hours_worked_on_sunday= int(input(('Ingrese la cantidad de horas que trabajo el dia domingo:')))

salario=7000



if ((hours_worked_on_sunday>=3 and hours_worked_on_sunday<=5) and assist_all_month=='S'):

   print("El salario del empleado es: " , (salario+(salario*0.03)))
 
 
elif ((hours_worked_on_sunday>=6 and hours_worked_on_sunday<=10) and assist_all_month=='S'):

   print("El salario del empleado es: " , (salario+(salario*0.1)))
else:
   if ((hours_worked_on_sunday>=3 and hours_worked_on_sunday<=10) and assist_all_month=='N'):
    print("El salario del empleado es: " , (salario+(salario*0.03)))