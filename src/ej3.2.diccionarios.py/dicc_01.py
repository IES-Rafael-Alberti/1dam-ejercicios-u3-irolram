"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

def diccionario():
    return {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}


def preguntar_divisa(diccionario):
    moneda = input("Cual es su divisa? (solo hay metida Euro, Dollar, Yen): ")
    if moneda in diccionario:
        print(f"El simbolo de {moneda} es {diccionario[moneda]}")
    else:
        print("Error")



def main():

    diccionario_divisas = diccionario()
    preguntar_divisa(diccionario_divisas)



if __name__ == "__main__":
    main()