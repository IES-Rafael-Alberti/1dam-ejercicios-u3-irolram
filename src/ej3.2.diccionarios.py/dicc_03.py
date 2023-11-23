"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70"""

def preguntar_usuario_fruta():
    fruta = input("Qué fruta quieres?: ")
    kilos = float(input(f"Cuantos kilos de {fruta} quieres: "))
    return fruta, kilos

    


def precio_fruta(fruta):
    

    precios = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

    return precios.get(fruta)

def main():
    fruta, kilos = preguntar_usuario_fruta()
    precio_unitario = precio_fruta(fruta)

    
    if precio_unitario is not None:
        precio_total = precio_unitario * kilos
        print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total}")
    else:
        print(f"Lo siento, la fruta {fruta} no está en la lista.")

if __name__ == "__main__":
    main()

