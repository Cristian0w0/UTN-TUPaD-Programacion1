CONTINENTES = ["África", "Asia", "Europa", "América", "Oceanía"]

#formato paises.csv: nombre,poblacion,superficie,continente

import csv
import sys

def main():
    while True:
        print("\n--- Menú Principal ---\n"
        "1. Filtrar países\n"
        "2. Ordenar países\n"
        "3. Mostrar estadísticas\n"
        "0. Salir")
        opcion = ingresar_opcion(rango_max=3)
        match opcion:
            case 0:
                print("\nSaliendo...")
                break
            case 1:
                filtrar()
            case 2:
                ordenar()
            case 3:
                estadisticas()

def filtrar():
    while True:
        print("\n--- Menú Filtrar ---\n"
        "1. Filtrar países por Continente\n"
        "2. Filtrar países por rango de Población\n"
        "3. Filtrar países por rango de Superficie\n"
        "0. Volver al Menú Principal")
        opcion = ingresar_opcion(rango_max=3)
        match opcion:
            case 0:
                break
            case 1:
                filtrar_continente()
            case 2:
                filtrar_poblacion_o_superficie("Población", 1)
            case 3:
                filtrar_poblacion_o_superficie("Superficie", 2)

def filtrar_continente():
    while True:
        print("\n--- Filtrar por Continente ---\n"
        "1. África\n"
        "2. Asia\n"
        "3. Europa\n"
        "4. América\n"
        "5. Oceanía\n"
        "0. Volver al menú filtrar")
        opcion = ingresar_opcion(rango_max=5)
        with open("./paises.csv", "r", encoding="utf-8-sig") as archivo:
            if (opcion == None):
                continue
            elif (1 <= opcion <= 5):
                continente = CONTINENTES[opcion-1]
                print(f"\n--- Paises de {continente} ---")
                for linea in archivo:
                    if (get_atributo(linea, 3) == continente):
                        pais = get_atributo(linea, 0)
                        print(pais)
            elif (opcion == 0):
                break

def filtrar_poblacion_o_superficie(opcion:str, indice:int):
    while True:
        min = ingresar_opcion(f"\nIngresar mínimo de {opcion} (al menos 1, o 0 " \
        "para volver al Menú Filtrar): ")
        if (min == 0):
            return
        elif (min != -1):
            break
    while True:
        max = ingresar_opcion(f"\nIngresar máximo de {opcion} (mayor o igual " \
        "al mínimo, 0 para volver al Menú Filtrar, -1 para máximo Infinito): ")
        if (1 <= max < min):
            print("El máximo debe ser mayor o igual al mínimo " \
            f"(mínimo actual: {min})")
        elif (max >= min):
            with open("paises.csv", "r", encoding="utf-8-sig") as archivo:
                print(f"\n--- Paises con {opcion} entre {min} y {max} ---")
                for linea in archivo:
                    atributo = int(get_atributo(linea, indice))
                    if (min <= atributo <= max):
                        pais = get_atributo(linea, 0)
                        print(f"{pais}", end="")
                        print_vacio(len(pais))
                        print(f"{atributo}")
            break
        elif (max == 0):
            break

def ordenar():
    while True:
        print("\n--- Menú Ordenar ---\n"
        "1. Ordenar países por Nombre\n"
        "2. Ordenar países por Población\n"
        "3. Ordenar países por Superficie\n"
        "0. Volver al menú principal")
        opcion = ingresar_opcion(rango_max=3)
        match opcion:
            case 0:
                break
            case 1:
                asc_desc("nombre")
            case 2:
                asc_desc("población")
            case 3:
                asc_desc("superficie")

def ordernar_nombre():
    while True:
        opcion = ""
        pass

def ordernar_poblacion():
    pass

def ordernar_superficie():
    pass

def estadisticas():
    print("\n--- Menú Estadísticas ---\n"
    "1. Mostrar país con mayor y menor Población\n"
    "2. Mostrar promedio de Población\n"
    "3. Mostrar promedio de Superficie\n"
    "4. Mostrar cantidad de países por Continente\n"
    "0. Volver al menú principal")
    opcion = ingresar_opcion(rango_max=4)

def ingresar_opcion(texto:str = "\nIngresar opción: ", 
                    rango_max:int = sys.maxsize, rango_min:int = 0):
    try:
        opcion = int(input(texto))
        if (not rango_min <= opcion <= rango_max):
            raise ValueError
    except ValueError:
        print("Opción inválida")
        opcion = None
    finally:
        return opcion

def get_atributo(linea:str, indice:int):
    return linea.strip().split(",")[indice]

def print_vacio(recorte:int):
    print(" " * (36-recorte), end="")

def asc_desc(campo:str):
    while True:
        opcion = input("\nOrdenar de forma Ascendente o Descendente? (A/D) (0 " \
        "para volver al menú anterior): ").upper()
        if (opcion in ["A", "D"]):
            break
        elif (opcion == "0"):
            return
        else:
            print("Opción inválida")
    with open("paises.csv", "r", encoding="utf-8-sig", newline="") as archivo:
        contenido = csv.reader(archivo)
        header = next(contenido)
        print(f"\n--- Paises ordenados por {campo.capitalize()} de forma " \
        f"{"Ascendente" if opcion == "A" else "Descendente"} ---")
        orden = True if opcion == "D" else False
        if (campo in ("población", "superficie")):
            contenido_ordenado = sorted(contenido, key=lambda 
                                    x: int(x[header.index(campo)]), reverse=orden)
        else:
            contenido_ordenado = sorted(contenido, key=lambda 
                                    x: x[header.index(campo)], reverse=orden)
        for line in contenido_ordenado:
            print(line)

main()