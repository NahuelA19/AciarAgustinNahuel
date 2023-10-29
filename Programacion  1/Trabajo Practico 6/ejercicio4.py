

list = [1,2,5,6,10,11,55,22,10,19,7]



num = int(input('Ingrse un numero : '))


new_list=[aux for aux in list if aux<num]


print(f'Los elementos menor que el numero {num} son: ')


for aux in new_list:
    print(aux)