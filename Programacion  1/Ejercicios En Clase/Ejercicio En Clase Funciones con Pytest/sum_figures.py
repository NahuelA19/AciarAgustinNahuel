def sum_figures(num):
    aux=0
    num_add=0
   
    while num!=0:
     aux= num%10
     num //=10
     num_add+=aux
    
    return num_add