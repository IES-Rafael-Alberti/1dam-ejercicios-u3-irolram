"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""



def notas_aprobadas_suspendidas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas_suspendidas = []

    for asignatura in asignaturas:
        nota_asignatura = float(input("¿Qué nota has sacado en" + asignatura + ":"))
        if nota_asignatura < 5:
            notas_suspendidas.append(asignatura)

    print("Tienes suspensas estas asignaturas: " + ", ".join(notas_suspendidas))

def main():
    notas_aprobadas_suspendidas()

if __name__ == "__main__":
    main()

