"""Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""

def dar_vuelta_por_comas():

    numeros = list(range(1,11))
    
    inverso = sorted(numeros, reverse = True)

