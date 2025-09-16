'''
Caso 1 – Biblioteca escolar – Préstamos de libros

La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles. Se pide 
desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). 
Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar 
un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.

Ejemplo:
•	títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
•	ejemplares[] = [5, 3, 7]
En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias, y "Matar un Ruiseñor" tiene 7 
copias.

Opciones del Menú:
1.	Ingresar lista de títulos:
    o	Permite al usuario introducir los títulos de los libros en la biblioteca.
    o	Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
2.	Ingresar lista de ejemplares disponibles (por título):
    o	Permite al usuario introducir el número de copias disponibles para cada título de libro.
    o	Ejemplo: Si el título es "1984", el usuario podría introducir "4" (lo que significa que hay 4 copias).
3.	Mostrar catálogo con stock:
    o	Muestra una lista de todos los títulos y el número de copias disponibles para cada uno.
    o	Ejemplo de salida:
        	"El Señor de los Anillos: 5 copias"
        	"Orgullo y Prejuicio: 3 copias"
        	"Matar un Ruiseñor: 7 copias"
4.	Consultar disponibilidad de un título específico:
    o	Permite al usuario introducir un título y ver cuántas copias están disponibles.
    o	Ejemplo: El usuario introduce "Orgullo y Prejuicio", y el programa muestra "3 copias disponibles".
5.	Listar agotados (0 ejemplares):
    o	Muestra una lista de todos los títulos que tienen 0 copias disponibles.
6.	Agregar título:
    o	Permite al usuario añadir un nuevo título al catálogo y especificar el número inicial de copias.
7.	Actualizar ejemplares (préstamo/devolución):
    o	Permite al usuario actualizar el número de copias cuando un libro es prestado (préstamo) o devuelto (devolución).
    o	Ejemplo: Si alguien toma prestada una copia de "El Señor de los Anillos", el usuario puede actualizar el conteo de 5 a 4.
8.	Ver catálogo:
    o	Muestra el catálogo entero de los títulos de libros.
9.	Salir:
    o	Sale del programa.
'''

titulos = []
ejemplares = []

menu = '''\n-- Menu Biblioteca --
1. Ingresar lista de títulos
2. Ingresar ejemplares disponibles por titulo
3. Mostrar catálogo con stock
4. Consultar disponibilidad
5. Mostrar catálogo sin stock
6. Agregar título
7. Actualizar ejemplares
8. Mostrar catálogo
0. Salir
'''

opcion = 1

while opcion != 0:
    print(menu)
    opcion = input("Ingresar opción: ")

    if not (opcion.isdigit()) or not (0 <= int(opcion) <= 8):
        print("Opción inválida")
        continue
    
    opcion = int(opcion)

    if (opcion == 1):
        while True:
            print("\nIngresar '.M' para volver al menu principal")
            titulo = input("Ingresar título: ")
            if (titulo == ".M"):
                break
            if not (titulo in titulos):
                titulos.append(titulo)
                ejemplares.append(0)
                print("Título agregado")
            else:
                print("El título ya se encuentra en el catálogo")
    elif (opcion == 2):
        while True:
            print("\nIngresar '.M' para volver al menu principal")
            titulo = input("Ingresar título: ")
            if (titulo == ".M"):
                break
            elif (titulo in titulos):
                cant_ejemplares = input(f"Ingresar cantidad de ejemplares para '{titulo}' (actualmente {ejemplares[titulos.index(titulo)]}): ")
                if (cant_ejemplares.isdigit() and int(cant_ejemplares) >= 0):
                    ejemplares[titulos.index(titulo)] = int(cant_ejemplares)
                    print(f"{ejemplares[titulos.index(titulo)]} ejemplares disponibles para '{titulo}'")
                else:
                    print("Opción inválida")
            else:
                print("No se encuentra el título")
    elif (opcion == 3):
        print("\nCatálogo con Stock: ")
        for titulo in titulos:
            if (ejemplares[titulos.index(titulo)] != 0):
                print(f"{titulo}, {ejemplares[titulos.index(titulo)]} ejemplares")
    elif (opcion == 4):
        while True:
            print("\nIngresar '.M' para volver al menu principal")
            titulo = input("Ingresar título: ")
            if (titulo == ".M"):
                break
            if (titulo in titulos):
                print(f"{ejemplares[titulos.index(titulo)]} ejemplares disponibles para '{titulo}'")
            else:
                print("El título no se encuentra en el catálogo")
    elif (opcion == 5):
        print("\nCatálogo sin Stock: ")
        for titulo in titulos:
            if (ejemplares[titulos.index(titulo)] == 0):
                print(titulo)
    elif (opcion == 6):
        while True:
            print("\nIngresar '.M' para volver al menu principal")
            titulo = input("Ingresar título: ")
            if (titulo == ".M"):
                break
            if not (titulo in titulos):
                cant_ejemplares = input(f"Ingresar ejemplares de '{titulo}': ")
                if (cant_ejemplares.isdigit() and 0 <= int(cant_ejemplares)):
                    titulos.append(titulo)
                    ejemplares.append(int(cant_ejemplares))
                    print("Título agregado")
                    break
                else:
                    print("Opción inválida")
            else:
                print("El título ya se encuentra en el catálogo")
    elif (opcion == 7):
        while True:
            print("\nIngresar '.M' para volver al menu principal")
            opcion = input("Ingresar prestamo o devolución (P/D): ").upper()
            if (opcion == "P"):
                titulo = input("Ingresar título a prestar: ")
                if (titulo in titulos):
                    print(f"{ejemplares[titulos.index(titulo)]} ejemplares disponibles")
                    if (ejemplares[titulos.index(titulo)] != 0):
                        prestamo = input("Ingresar cantidad de ejemplares a prestar: ")
                        if (prestamo.isdigit() and 
                            1 <= int(prestamo) <= ejemplares[titulos.index(titulo)]):
                            ejemplares[titulos.index(titulo)] -= int(prestamo)
                            print(f"{prestamo} ejemplares de '{titulo}' prestados")
                        else:
                            print("Opción inválida")
                else:
                    print("No se encuentra el título")
            elif (opcion == "D"):
                titulo = input("Ingresar título a devolver: ")
                if (titulo in titulos):
                    devolucion = input("Ingresar cantidad de ejemplares a devolver: ")
                    if (devolucion.isdigit() and int(devolucion) >= 1):
                        ejemplares[titulos.index(titulo)] += int(devolucion)
                        print(f"{devolucion} ejemplares de '{titulo}' devueltos")
                    else:
                        print("Opción inválida")
                else:
                    print("No se encuentra el título")
            elif (opcion == ".M"):
                break
            else:
                print("Opción inválida")
    elif (opcion == 8):
        if (titulos == []):
            print("\nEl catálogo se encuentra vacío")
        else:
            print("\nCatálogo completo:")
            for titulo in titulos:
                print(f"{titulo}, {ejemplares[titulos.index(titulo)]} ejemplares")
    elif (opcion == 0):
        print("\nSaliendo...")