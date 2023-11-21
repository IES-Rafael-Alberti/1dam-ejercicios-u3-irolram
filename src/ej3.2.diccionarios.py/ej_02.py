"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""


def main():

    nombre = input("Introduzca nombre: ")
    edad = int(input("Introduzca edad: "))
    direccion = input("Introduzca direccion: ")
    telefono = input("introduzca telefono: ")


    info_usuario ={

        "nombre" : nombre,
        "edad" : edad,
        "direccion" : direccion,
        "telefono": telefono
    }

    print(f"{info_usuario["nombre"]} tiene {info_usuario["edad"]} años, vive en {info_usuario["direccion"]} y su telefono es {info_usuario["telefono"]}")  



if __name__ == "__main__":
    main()