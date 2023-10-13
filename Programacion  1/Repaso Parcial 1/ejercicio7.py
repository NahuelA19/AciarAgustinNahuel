age_utility= int(input("Ingrese la antiguedad en meses:"))

salary=7000

if age_utility<12:
 salary= salary+(salary*0.05)
 print("La utilidad con menos de un año es de:", salary)
elif age_utility>=12 and age_utility<24:
 salary= salary+(salary*0.07)
 print("La utilidad con menos de un año es de:", salary)
elif age_utility>=24 and age_utility>60:
 salary= salary+(salary*0.1)
 print("La utilidad con menos de un años es de:", salary)
else:
 salary= salary+(salary*0.2)
 print("La utilidad con mas  de 10 años es de:", salary)