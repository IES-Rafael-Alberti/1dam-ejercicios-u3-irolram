"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""

def abecedario_lista():

    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    filtro_abecedario = [letra for i, letra in enumerate(abecedario, start = 1)if i %3 != 0]

    print(filtro_abecedario)


def main():
    abecedario_lista()

if __name__ == "__main__":
    main()
