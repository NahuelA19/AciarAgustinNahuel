def long_last_word(w):
    
    w = w.strip()   #.strip elimina los espacios en blanco tanto al comienzo como al  final 

    if not w:
        return 0  # Si el string está vacío, retorna 0

  
    last_space = w.rfind(' ')   #Encuentra el ultimo espacio en el texto 

    if last_space == -1:  
        
        return len(w)    #Retorna -1 si es una sola palabra :(
    else:
        print(len(w))
        print(last_space)
        return len(w) - last_space - 1 

