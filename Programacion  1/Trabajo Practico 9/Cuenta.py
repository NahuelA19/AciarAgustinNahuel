class Cuenta:
    def __init__(self, titular, amount=0.0):
        self.titular = titular                  
        self.amount = amount



    #Getter and Setter de Titular
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular
    

    #Getter and Setter de Cantidad
    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    #Funcion mostrar saldo y titular
    def show(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.amount} euros")

    #Funcion ingreso y retiro de dinero:

    def ingresar(self, amount):
        if amount > 0:
            self.amount += amount

    def retirar(self, amount):
        if amount > 0:
            self.amount -= amount

#Clase en uso:
cuenta = Cuenta("Juan Pérez", 700.0)
cuenta.show()
cuenta.ingresar(70.0)
cuenta.show()
cuenta.retirar(7.0)
cuenta.show()
