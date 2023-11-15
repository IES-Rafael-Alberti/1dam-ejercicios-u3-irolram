"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre 
por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es 
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas 
introducidas por el usuario."""

def ingresar_nota(asignaturas):

    notas = []


    for asignatura in asignaturas:
        nota = float(input(f"Qué nota ha sacado en {asignatura}: "))
        notas.append(nota)
    return notas

def mostrar_nota(asignaturas, notas):
    for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado {notas[i]} ")

def main():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = ingresar_nota(asignaturas)
    mostrar_nota(asignaturas, notas)


if __name__ == "__main__":
    main()