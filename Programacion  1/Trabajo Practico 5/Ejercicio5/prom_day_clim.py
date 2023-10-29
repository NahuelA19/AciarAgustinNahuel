def prom_day_clim(days):
     num=0
     while True:
          if num<=days:
            max_temp=int(input('Ingrese la temperatura maxima del dia:'))
            min_temp= int(input('Ingrese la temperatura minima del dia:'))
            prom_temp = (max_temp+min_temp)/2
            num = num+1
            print(f'El clima promedio del dia {num} es de: {prom_temp}')