"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""


def ingresar_numeros_ganadores():

    numeros = []
    for i in range(6):
        numero = int(input(f"Ingrese el numero ganador {i + 1} de la loteria: "))
        numeros.append(numero)
    return numeros

def numeros_ordenados(numeros):

    numeros_ordenado = sorted(numeros)
    print("Estos son los numeros ordenados de menor a mayor: ")
    for numero in numeros_ordenado:
        print(numero)


def main():
    numeros_ganadores = ingresar_numeros_ganadores() 
    numeros_ordenados(numeros_ganadores)

if __name__ == "__main__":
    main()