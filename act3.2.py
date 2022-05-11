import math 
import numpy as np
class vector:
    def __init__(self, coordenadas):
      self.__coordenadas = coordenadas

    def coordenadas(self):
        return self.__coordenadas 
    
    def coordenadas(self, valor):
        self.__coordenadas = valor

    def dimension():
        n = int(input("Por favor ingrese la dimension del vector que desea (1,2 o 3): "))
        #if n>3 | n<1:
        #    print("Elija un número entre 1 y 3")
        return n

    def vectores(n):
        vector1 = np.array([0])
        vector2 = np.array([0,0])
        vector3 = np.array([0,0,0])
        if(n==1):
            vector1[0] = int(input("Por favor ingrese X: "))
            return vector1

        if(n==2):
            vector2[0] = int(input("Por favor ingrese X: "))
            vector2[1] = int(input("Por favor ingrese Y: "))
            return vector2

        if(n==3):
            vector3[0] = int(input("Por favor ingrese X: "))
            vector3[1] = int(input("Por favor ingrese Y: "))
            vector3[2] = int(input("Por favor ingrese Z: "))
            return vector3

class operaciones():

    def sumaVectores():
        n = vector.dimension()
        v1 = vector.vectores(n)
        v2 = vector.vectores(n)
        total1= []
        for i in range(np.size(v1)):
            total1.append(v1[i] + v2[i])

        print(v1, " + ", v2, " = ", total1)

    def restaVectores():
        n = vector.dimension()
        v1 = vector.vectores(n)
        v2 = vector.vectores(n)
        total1= []
        for i in range(np.size(v1)):
            total1.append(v1[i] - v2[i])

        print(v1, " - ", v2, " = ", total1)

    def productoEscalar():
        n = vector.dimension()
        v1 = vector.vectores(n)
        e = int(input("Por favor ingrese el escalar: "))
        total1= []

        for i in range(np.size(v1)):
            total1.append(v1[i] * e)

        print(e, " * ", v1, " = ", total1)

    def productoCruz(): 
        n = vector.dimension()
        v1 = vector.vectores(n)
        v2 = vector.vectores(n)

        if n == 1:
            print("Esta operación no se puede realizar")

        if n == 2:
            total = (v1[0] * v2[1]) - (v1[1] * v2[0])
            print ("El producto cruz entre ", v1, " y ", v2, " es ", total)
        
        if n == 3:
            x = (v1[1]*v2[2]) - (v2[1]*v1[2])
            y = - ((v1[0]*v2[2]) - (v2[0]*v1[2]))
            z = (v1[0]*v2[1]) - (v2[0]*v1[1])
            total = [x, y, z]
            print ("El producto cruz entre ", v1, " y ", v2, " es ", total)


    def productoPunto(): 
        n = vector.dimension()
        v1 = vector.vectores(n)
        v2 = vector.vectores(n)
        total = 0

        for i in range (np.size(v1)):
            total = (v1[i]*v2[i]) + total
        
        print ("El producto punto entre ", v1, " y ", v2, " es ", total)


    def divisionEscalar():
        n = vector.dimension()
        v1 = vector.vectores(n)
        e = int(input("Por favor ingrese el escalar: "))
        total1= []

        for i in range(np.size(v1)):
            total1.append(v1[i] / e)

        print(e, " / ", v1, " = ", total1)
    
    def normal():
        n = vector.dimension()
        v1 = vector.vectores(n)
        total = 0

        for i in range (np.size(v1)):
            total = math.pow(v1[i], 2) + total
        
        total = math.sqrt(total) 

        print ("La normal del vector ", v1, " es de ", total)
        
    
    def angulo():
        n = vector.dimension()
        v1 = vector.vectores(n)
        v2 = vector.vectores(n)
        divisor = 0
        dividendo1 = 0
        dividendo2 = 0

        #Producto punto de los vectores
        for i in range (np.size(v1)):
            divisor = (v1[i]*v2[i]) + divisor

        #Multiplicación de la normal de los dos vectores

        #normal del vector 1
        for i in range (np.size(v1)):
            dividendo1 = math.pow(v1[i], 2) + dividendo1
        
        dividendo1 = math.sqrt(dividendo1)

        #normal del vector 2
        for i in range (np.size(v1)):
            dividendo2 = math.pow(v2[i], 2) + dividendo2
        
        dividendo2 = math.sqrt(dividendo2)

        dividendo = dividendo1 * dividendo2

        total = round(math.degrees(math.acos(divisor / dividendo)))

        print ("El angulo entre los vectores ", v1, " y ", v2, " es ", total, " grados")

class main():

    def inicio():
        num = int(input ("Selecciones la operación que desea realizar \n1. Suma de vectores\n2. Resta de vectores\n3. Multiplicación por un escalar\n4. Producto cruz\n5. Producto punto\n6. Division por un escalar\n7. Normal de vector\n8. Angulo entre dos vectores\n"))
        
        if num == 1:
            operaciones.sumaVectores()

        if num == 2:
            operaciones.restaVectores()

        if num == 3:
            operaciones.productoEscalar()
        
        if num == 4:
            operaciones.productoCruz()
        
        if num == 5:
            operaciones.productoPunto()
        
        if num == 6:
            operaciones.divisionEscalar()

        if num==7:
            operaciones.normal()

        if num == 8:
            operaciones.angulo()
        
    inicio()