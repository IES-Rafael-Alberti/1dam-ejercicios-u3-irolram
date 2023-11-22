"""Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""


def datos_persona(diccionario_info):
    clave = input("Dime información sobre ti (o 'salir' para finalizar): ")

    while clave.lower() != "salir":
        valor = input(f"Ingrese {clave}: ")
        diccionario_info[clave] = valor

        print("Contenido del diccionario actualizado:")
        for key, valor in diccionario_info.items():
            print(f"{key}: {valor}")

        clave = input("Ingresa el tipo de información (o 'salir' para finalizar): ")

def main():
    diccionario_info = {}
    datos_persona(diccionario_info)

if __name__ == "__main__":
    main()










def diccionario_vacio():
    info = {}