# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 

'''
Entrada:
    Numero:int->num
Salida:
Raiz cubica

'''
import math
num = int(input("Dime el número:"))
print("Raíz cuadrada:",math.sqrt(num))
print("Raíz cúbica:",num ** (1 / 3))
