"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso"""


def main():
    total = 0
#Mates en asignaturas y el 6 en credits
    asignaturas ={"Mates": 6, "Fisica": 4, "Quimica": 5}
    for asignatura,credits in asignaturas.items():
        print(f"{asignatura} = {credits}")
        total += credits
    print(f"total = {total}")


if __name__ == "__main__":
    main()