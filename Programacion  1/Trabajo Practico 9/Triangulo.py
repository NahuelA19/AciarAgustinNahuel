class Triangulo:
    def __init__(self, side1, side2, side3):
        self.side1 = side1                         #Lados de un triangulo
        self.side2 = side2
        self.side3 = side3

    def print_longest_side(self):
        sides = [self.side1, self.side2, self.side3]
        longest_side = max(sides)
        print(f"El lado más largo es {longest_side}")

    def determine_type(self):              #Determinar el tipo de triangulo que es 
        if self.side1 == self.side2 == self.side3:
            print("El triángulo es equilátero")
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")

# Se solicita al usuario las longitudes: 
side1 = float(input("Ingrese la longitud del primer lado del triángulo: "))      
side2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
side3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

triangle = Triangulo(side1, side2, side3)

triangle.print_longest_side()    #Lado mas largo
triangle.determine_type()    #Tipo de triangulo 