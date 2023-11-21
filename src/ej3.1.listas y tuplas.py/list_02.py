"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio 
<asignatura>, donde <asignatura> sobre cada una de las asignaturas 
de la lista."""


def mostrar_mensaje(asignatura):
    print("Yo estudio {}".format(asignatura))



def main():
    
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    for asignatura in asignaturas:
        mostrar_mensaje(asignatura)


if __name__ == "__main__":
    main()