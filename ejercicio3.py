'''
Ejercicio 3
Programa que calcula  la hipotenusa a partir  de los dos catetos
Entradas:
catetoA: int-> a
catetoB: int-> b
Salidas:
hipotenusa: float -> c

Analisis
Se utiliza el teorema de pitagoras 
'''
import math
a=input("Escribe el valor del cateto A:")
a=int(a)
b=input("Escribe el valor del cateto B")
b=int(b)
c=(a*a+b*b)**(1/2)
c=math.sqrt(a*a+b*b)
print("El valor de la hipotenusa es:",c)