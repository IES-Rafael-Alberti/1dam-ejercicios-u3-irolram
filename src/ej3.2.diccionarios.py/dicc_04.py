"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma 
fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes"""

def dar_nombre_mes(mes):
    meses = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
             9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
    return meses.get(mes, "mes no válido")

def formatear_fecha(fecha):
    # Dividir la fecha en partes
    partes_fecha = fecha.split('/')

    # Verificar que haya tres partes
    if len(partes_fecha) == 3:
        dia, mes, año = map(int, partes_fecha)
        nombre_mes = dar_nombre_mes(mes)

        # Formatear la fecha
        fecha_formateada = f"{dia} de {nombre_mes} de {año}"
        return fecha_formateada
    else:
        return "Formato de fecha incorrecto. Por favor, usa dd/mm/aaaa."

def main():
    fecha = input("Dime la fecha de tu cumpleaños en formato dd/mm/aaaa: ")
    fecha_formateada = formatear_fecha(fecha)
    print(f"Fecha formateada: {fecha_formateada}")

if __name__ == "__main__":
    main()