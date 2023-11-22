"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70"""

def preguntar_usuario_fruta():
    fruta = input("Qué fruta quieres?: ")
    kilos = input(f"Cuantos kilos de {fruta} quieres")
    return fruta

    


def precio_fruta(fruta):
    Plátano = "Plátano"
    Manzana = "Manzana"
    Pera = "Pera"
    Naranja = "Naranja"

    precio = {Plátano: "1.35", Manzana: "0.80", Pera: "0.85", Naranja: "0.70"}

    return precio

def main():

    precio = precio_fruta()
    preguntar_usuario_fruta()




    if __name__ == "__main__":
        main()

