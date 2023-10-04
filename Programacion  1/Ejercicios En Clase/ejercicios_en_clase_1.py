print('Bienvenido al instituto de ingles') 

date = input('Ingrese la fecha en formato "dia, DD/MM": ').lower()
day = date[0 : date.find(',')]
day_number = int(date[date.find(' ') + 1 : date.find('/')])
month = int(date[date.find('/') + 1 :])

list_days= ['lunes','martes','miercoles','jueves','viernes'] #Lista de los dias de la semana

if day in list_days:
    if(day_number<=31 and month<=12):
        if (day=='lunes' or day == 'martes' or day== 'miercoles'): #Dias del nivel inicial,intermedio y avanzado
            students = int(input('Ingrese la cantidad de alumnos: ')) 
            exam=input('Se tomo examenes? Ingrese S en caso de que si o N en caso contrario')
            if(exam=='S'):
                approved_students=int(input('Ingrese la cantidad de alumnos que aprobaron:'))
                failing_students=int(input('Ingrese la cantidad de alumnos que desaprobaron:'))
                students_evaluated= (approved_students+failing_students)

                if(students<students_evaluated):
                    print('Hay mas alumnos que aprobaron/desaprobaron que la cantidad de alumnos que ingreso.')
                else:
                    students_percentage_approved= (approved_students/failing_students)*100
                    print('El porcentaje de alumnos que aprobo fue de: {students_evaluated}%')
            elif(exam=='N'):
                print('No se tomaron examenes.')
            else:
                print("La opcion no es correcta.")
        elif (day=='jueves'): # Jueves es dia de practica hablada.
            porcentage_attendance= float(input('Ingrese el porcentaje de asistencia:'))
            if (porcentage_attendance)>50.0:
                print("Asistio la mayoria.")
            else:
                print('No asistio la mayoria.')
        else: 
            if (day_number <=7):
                print('Comienzo de nuevo ciclo')
                new_students= int(input('Ingrese la cantidad de nuevos alumnos:'))
                cost_per_course= int(input('Ingrese el costo del arrancel:'))

                cost_per_all_new_students= new_students*cost_per_course
                print('Los ingresos totales por este nuevo ciclo son de :', cost_per_all_new_students,'$') 
    else:
        print('El dia o mes ingresado es incorrecto.')
else:
    print('El dia de la semana ingresado es incorrecto.')
