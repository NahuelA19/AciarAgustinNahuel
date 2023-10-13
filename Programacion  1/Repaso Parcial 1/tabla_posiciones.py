print('---------TABLA DE POSICIONES FASE DE GRUPOS---------\n')

amount_qualy = int(input('¿Cuantos equipos clasifican a la siguiente fase?: '))
# El programa inicia con esta pregunta y guardando el valor en la variable

dict_teams = {}  # se inicia un diccionario vacío para almacenar los equipos
counter = 1
while True:
    team = input(f'Ingrese el equipo {counter} (deje en blanco para finalizar la carga): ')
    if not team:                   # Se guarda el nombre dentro del equipo como Key de un valor List en el diccionario.
        break                      # Esta última se inica con dos valores en 0, y representan la cantidad inicial de
    dict_teams[team] = [0, 0]      # puntos y goles que tiene cada equipo. El bucle finaliza cuando el usuario no
    counter += 1                   # ingresa nada.


print('\nLos equipos que integran el grupo son:')
position = 1
for i in dict_teams:               # Se muestran en pantalla los equipos ingresados anteriormente
    print(f'{position}- {i}')
    position += 1

# Se crea un List con los nombres de los equipos para poder acceder a los valores del diccionario
list_teams = list(dict_teams.keys())

print('\nIngrese los resultados de los partidos con el siguiente formato:\n            golesEquipo1:golesEquipo2\n')
for i in range(len(dict_teams)):
    for j in range(i+1, len(dict_teams)):
        while True:   # Se ingresa el resultado de los partidos y se evalúan.....
            result = input(f'Resultado de {list_teams[i]}:{list_teams[j]} ---> ')

            if int(result[0:result.find(':')]) < 0 or int(result[result.find(':')+1:]) < 0:
                print('ERROR. No se puede ingresar una cantidad de goles negativa. Reintente\n')
                continue  # Si al menos una cantidad de goles es negativa, el programa pedirá de nuevo el resultado

            #  de acuerdo al resultado del partido, se le sumarán 3 puntos al equipo que gane
            #  y un punto a cada uno en caso de empate. En todos los casos se suman los goles de cada equipo
            if int(result[0:result.find(':')]) > int(result[result.find(':')+1:]):
                dict_teams[list_teams[i]][0] += 3
                dict_teams[list_teams[i]][1] += int(result[0:result.find(':')])
                dict_teams[list_teams[j]][1] += int(result[result.find(':')+1:])
                break
            elif int(result[0:result.find(':')]) < int(result[result.find(':')+1:]):
                dict_teams[list_teams[j]][0] += 3
                dict_teams[list_teams[i]][1] += int(result[0:result.find(':')])
                dict_teams[list_teams[j]][1] += int(result[result.find(':')+1:])
                break
            else:
                dict_teams[list_teams[i]][0] += 1
                dict_teams[list_teams[j]][0] += 1
                dict_teams[list_teams[i]][1] += int(result[0:result.find(':')])
                dict_teams[list_teams[j]][1] += int(result[result.find(':')+1:])
                break
#  Se ordena el diccionario, primero por goles y despues por puntos
dict_teams = dict(sorted(dict_teams.items(), key=lambda item: (item[1][1]), reverse=True))
dict_teams = dict(sorted(dict_teams.items(), key=lambda item: (item[1][0]), reverse=True))

# Se muestran las posiciones finales
print('\n---------TABLA DE POSICIONES FINAL---------\n')

print('Equipo           Puntos          Goles')
for teams, teams_points_goals in dict_teams.items():
    needed_spaces = 19 - len(teams)
    for i in range(needed_spaces):
        teams += ' '
    print(teams, end='')
    print(teams_points_goals[0], '             ', teams_points_goals[1])

# Imprime finalmente los equipos clasifi
print('')
list_teams = list(dict_teams.keys())
for i in range(min(amount_qualy, len(list_teams))):
    print(f'Equipo clasificado {i+1}: {list_teams[i]}')







