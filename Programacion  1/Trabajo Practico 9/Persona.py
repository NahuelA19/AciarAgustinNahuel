class Persona:
    def __init__(self, name='', age=0, dni=''):
        self.name = name
        self.age = age
        self.dni = dni

    
    
    
    #Getter Nombre
    def get_name(self):
        return self.name

    #Setter Nombre
    def set_name(self, name):
        self.name = name


     #Getter y Setter Edad 
    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print('La edad no puede ser negativa.')

  
    #Getter y Setter de DNI
    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni


  
    #Funcion para mostrar 
    def show(self):
        print(f'Nombre: {self.name}')
        print(f'Edad: {self.age}')
        print(f'DNI: {self.dni}')

    
    #Funcion si es mayor
    def is_older_than_age(self):
        return self.age >= 18



#Prueba: 

pers1 = Persona('Raul', 40, '31373045')
pers1.show()

print('¿Es mayor de edad?', pers1.is_older_than_age())
