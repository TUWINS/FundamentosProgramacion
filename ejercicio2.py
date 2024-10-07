'''
programa que calcule el area y el perimetro de un rectangulo apartir de su base y altura

Entradas:
   base: integer
   altura:integer

Salidas:
    perimetro: integer
    area: integer

Analisis
 se require calcular con las formulas para
  area y perimetro
'''
# input siempre regresa un string
#para tratarlo como otro dato se debe convertir
print("Programa que calcula area y perimetro de un rectangulo")
base=input("Escribe la base del rectangulo: ")
base=int(base)
altura=input("Escribe la altura del rectangulo: ")
altura=int(altura)
area=base*altura
perimetro=base+base+altura+altura
print("El area es: ",area)
print("El perimetro es: ",perimetro)
