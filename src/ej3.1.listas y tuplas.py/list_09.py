"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

def contar_letras(palabra):
    a_count = e_count = i_count = o_count = u_count = 0

    for letra in palabra:
        if letra.lower() == "a":
            a_count += 1
        elif letra.lower() == "e":
            e_count += 1
        elif letra.lower() == "i":
            i_count += 1
        elif letra.lower() == "o":
            o_count += 1
        elif letra.lower() == "u":
            u_count += 1

    print(f"Numero de veces que la letra 'a' aparece son: {a_count}")
    print(f"Numero de veces que la letra 'e' aparece son: {e_count}")
    print(f"Numero de veces que la letra 'i' aparece son: {i_count}")
    print(f"Numero de veces que la letra 'o' aparece son: {o_count}")
    print(f"Numero de veces que la letra 'u' aparece son: {u_count}")

def main():

    palabra_usuario = input("Escribe una palabra: ")
    contar_letras(palabra_usuario)
    

if __name__ == "__main__":
    main()