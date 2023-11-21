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