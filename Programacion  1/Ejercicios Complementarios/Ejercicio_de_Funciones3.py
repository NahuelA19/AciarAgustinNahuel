
#Programa con error:
#def most(a,b):
   # if (x<y):
       #return x
     #else:
       #return y


#def least(a,b):
    #if (x<y):
        #return x
    #else:
        #return y
    


#x= int(input('Un numero: '))
#y= int(input('Otro numero'))


#print(most(x-3,least(x+2,y-5)))

#Programa solucionado:
def most(x, y):  #cambio de (a,b) por (x,y)
    if (x < y):
        return x
    else:
        return y

def least(x, y): #cambio de (a,b) por (x,y)
    if (x < y):
        return x
    else:
        return y

x = int(input('Un numero: '))
y = int(input('Otro numero: '))

print(most(x - 3, least(x + 2, y - 5)))
