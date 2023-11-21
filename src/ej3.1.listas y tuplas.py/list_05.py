"""Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""

def generar_lista_numeros():

    numeros = list(range(1,11))
    return numeros
    
def invertir_y_poner_comas(lista):

    # Utilizamos sorted con reverse = True para ordenar la lista en orden inverso
    inverso = sorted(lista, reverse = True)
    # Utilizamos join para concatenar los elementos de la lista con comas
    resultado = ", ".join(map(str, inverso))
    print(resultado)

def main():
    
    numeros = generar_lista_numeros()

    invertir_y_poner_comas(numeros)

if __name__ == "__main__":
    main()

