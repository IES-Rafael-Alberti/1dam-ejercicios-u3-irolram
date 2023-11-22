"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato"""


def preguntar_articulo_precio():

    cesta = {}
    articulo = input("Que articulo quiere añadir a la lista: ")
    precio = float(input(f"Que precio tiene {articulo}: "))
    

    cont = True

    while cont:
        cesta[articulo]= precio
        cont = input("Quiere seguir llenando la lista? si no quiere escriba 'no'") == 'no'
    else: 
        print ("vale")

    

def main():

    preguntar_articulo_precio()


if __name__ == "__main__":
    main()

